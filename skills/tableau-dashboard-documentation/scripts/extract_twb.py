#!/usr/bin/env python3
"""
extract_twb.py — Extrai a definição de um workbook Tableau (.twb ou .twbx)
para uma estrutura JSON: data sources, campos calculados (com formula bruta
e formula resolvida), parametros, planilhas, dashboards e o grafo de
dependencia entre campos calculados.

Uso:
    python3 extract_twb.py caminho/para/arquivo.twbx > saida.json
    python3 extract_twb.py caminho/para/arquivo.twb > saida.json

Isso NAO le os dados do extrato (.hyper) — apenas a definicao do workbook
(metadados, formulas, estrutura). Formulas de campos calculados vivem no
XML do .twb, entao isso e suficiente para documentacao "a nivel de formula".
"""

import json
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

TABLE_CALC_FUNCS = {
    "WINDOW_SUM", "WINDOW_AVG", "WINDOW_MEDIAN", "WINDOW_COUNT", "WINDOW_MAX",
    "WINDOW_MIN", "WINDOW_STDEV", "WINDOW_STDEVP", "WINDOW_VAR", "WINDOW_VARP",
    "RUNNING_SUM", "RUNNING_AVG", "RUNNING_COUNT", "RUNNING_MAX", "RUNNING_MIN",
    "RANK", "RANK_DENSE", "RANK_MODIFIED", "RANK_PERCENTILE", "RANK_UNIQUE",
    "INDEX", "FIRST", "LAST", "LOOKUP", "TOTAL", "SIZE", "PREVIOUS_VALUE",
}

FIELD_REF_RE = re.compile(r"\[[^\[\]]+\]")


def load_twb_root(path: Path) -> ET.Element:
    """Aceita .twb direto ou .twbx (zip) e retorna a raiz do XML do workbook."""
    if path.suffix.lower() == ".twbx":
        with zipfile.ZipFile(path) as z:
            twb_names = [n for n in z.namelist() if n.lower().endswith(".twb")]
            if not twb_names:
                raise ValueError(f"Nenhum arquivo .twb encontrado dentro de {path}")
            # Se houver mais de um, pega o de nivel mais raso (menos '/')
            twb_names.sort(key=lambda n: n.count("/"))
            with z.open(twb_names[0]) as f:
                data = f.read()
        return ET.fromstring(data)
    else:
        return ET.parse(path).getroot()


def classify_calc(formula: str) -> str:
    if formula is None:
        return "desconhecido"
    if "{" in formula and "}" in formula and any(
        kw in formula.upper() for kw in ("FIXED", "INCLUDE", "EXCLUDE")
    ):
        return "LOD (Level of Detail)"
    upper = formula.upper()
    if any(re.search(rf"\b{fn}\s*\(", upper) for fn in TABLE_CALC_FUNCS):
        return "Calculo de tabela (table calculation)"
    return "Calculo padrao (row/aggregate level)"


def display_name(col: ET.Element) -> str:
    caption = col.get("caption")
    if caption:
        return caption
    name = col.get("name", "")
    return name.strip("[]")


def resolve_formula(formula: str, name_to_caption: dict) -> str:
    if not formula:
        return formula

    def _sub(match):
        token = match.group(0)  # inclui colchetes, ex: [Calculation_12345]
        caption = name_to_caption.get(token)
        if caption and caption != token.strip("[]"):
            return f"[{caption}]"
        return token

    return FIELD_REF_RE.sub(_sub, formula)


def extract_fields_from_datasource(ds: ET.Element) -> list:
    fields = []
    for col in ds.findall("./column"):
        calc = col.find("./calculation")
        field = {
            "technical_name": col.get("name"),
            "caption": display_name(col),
            "role": col.get("role"),
            "datatype": col.get("datatype"),
            "type": col.get("type"),
            "is_calculated": calc is not None,
        }
        if calc is not None:
            field["calc_class"] = calc.get("class")
            field["formula_raw"] = calc.get("formula")
        fields.append(field)
    return fields


def extract_parameters(root: ET.Element) -> list:
    params = []
    for ds in root.findall("./datasources/datasource"):
        if ds.get("name") != "Parameters":
            continue
        for col in ds.findall("./column"):
            calc = col.find("./calculation")
            default_value = calc.get("formula") if calc is not None else None
            allowed = None
            range_el = col.find("./range")
            members_el = col.find("./members")
            if range_el is not None:
                allowed = {
                    "tipo": "range",
                    "min": range_el.get("min"),
                    "max": range_el.get("max"),
                    "granularity": range_el.get("granularity"),
                }
            elif members_el is not None:
                allowed = {
                    "tipo": "lista",
                    "valores": [m.get("value") for m in members_el.findall("./member")],
                }
            params.append({
                "nome": display_name(col),
                "technical_name": col.get("name"),
                "tipo_dominio": col.get("param-domain-type"),
                "datatype": col.get("datatype"),
                "valor_padrao": default_value,
                "valores_permitidos": allowed,
            })
    return params


def build_instance_to_column_map(root: ET.Element) -> dict:
    """Mapeia o `name` de cada <column-instance> (ex: '[none:Calculation_123:qk]',
    uma instancia/agregacao salva de um campo) para o `column` real que ela
    representa (ex: '[Calculation_123]'). Necessario porque filtros e algumas
    referencias em worksheets apontam para a instancia, nao para o campo em si."""
    mapping = {}
    for ci in root.findall(".//column-instance"):
        inst_name = ci.get("name")
        real_col = ci.get("column")
        if inst_name and real_col:
            mapping[inst_name] = real_col
    return mapping


def resolve_display(token: str, name_to_caption: dict, instance_to_column: dict) -> str:
    """Resolve um token de campo (pode ser o nome tecnico de uma coluna, ou o
    nome de uma column-instance) para o nome legivel (caption) do campo real."""
    if not token:
        return token
    token = token if token.startswith("[") else f"[{token}]"
    # Se for uma instancia (agregacao salva), resolve para a coluna real primeiro.
    real_col = instance_to_column.get(token, token)
    return name_to_caption.get(real_col, real_col.strip("[]"))


def extract_worksheets(root: ET.Element, name_to_caption: dict, instance_to_column: dict) -> list:
    worksheets = []
    for ws in root.findall("./worksheets/worksheet"):
        deps = []
        for dep in ws.findall(".//datasource-dependencies"):
            ds_name = dep.get("datasource")
            cols_used = []
            for ci in dep.findall("./column-instance"):
                col_ref = ci.get("column", "")
                cols_used.append({
                    "campo": resolve_display(col_ref, name_to_caption, instance_to_column),
                    "technical_name": col_ref,
                    "agregacao": ci.get("derivation"),
                })
            deps.append({"datasource": ds_name, "campos_usados": cols_used})
        filtros = []
        for filt in ws.findall(".//filter"):
            col_ref = filt.get("column", "")
            # O atributo column de um <filter> costuma vir como
            # '[datasource].[nome_da_instancia_ou_campo]' — pega o ultimo segmento.
            token = col_ref.split("].[")[-1].strip("[]") if col_ref else None
            filtros.append({
                "campo": resolve_display(token, name_to_caption, instance_to_column) if token else None,
                "classe": filt.get("class"),
                "raw": col_ref,
            })
        worksheets.append({
            "nome": ws.get("name"),
            "datasource_dependencies": deps,
            "filtros": filtros,
        })
    return worksheets


def extract_dashboards(root: ET.Element) -> list:
    dashboards = []
    for dash in root.findall("./dashboards/dashboard"):
        zone_names = set()
        for zone in dash.findall(".//zone"):
            n = zone.get("name")
            if n:
                zone_names.add(n)
        dashboards.append({
            "nome": dash.get("name"),
            "planilhas_referenciadas": sorted(zone_names),
        })
    return dashboards


def build_dependency_graph(all_calc_fields: list, name_to_caption: dict) -> dict:
    """Para cada campo calculado, lista outros campos calculados que ele referencia."""
    calc_technical_names = {f["technical_name"] for f in all_calc_fields}
    graph = {}
    for f in all_calc_fields:
        refs = set(FIELD_REF_RE.findall(f.get("formula_raw") or ""))
        depends_on = sorted(r for r in refs if r in calc_technical_names and r != f["technical_name"])
        graph[f["technical_name"]] = {
            "caption": f["caption"],
            "depende_de": [
                {"technical_name": r, "caption": name_to_caption.get(r, r.strip("[]"))}
                for r in depends_on
            ],
        }
    # Preenche "usado_por" (grafo reverso)
    used_by = {tn: [] for tn in graph}
    for tn, info in graph.items():
        for dep in info["depende_de"]:
            used_by.setdefault(dep["technical_name"], []).append(
                {"technical_name": tn, "caption": info["caption"]}
            )
    for tn, info in graph.items():
        info["usado_por"] = used_by.get(tn, [])
    return graph


def main():
    if len(sys.argv) != 2:
        print("Uso: python3 extract_twb.py <arquivo.twb|.twbx>", file=sys.stderr)
        sys.exit(1)

    path = Path(sys.argv[1])
    root = load_twb_root(path)

    # 1) Mapa global technical_name -> caption (para resolver formulas)
    name_to_caption = {}
    for col in root.findall(".//column"):
        name_to_caption[col.get("name")] = display_name(col)

    # 1b) Mapa de instancias de coluna (agregacoes salvas em worksheets/filtros)
    # para o campo real que elas representam.
    instance_to_column = build_instance_to_column_map(root)

    # 2) Data sources
    datasources = []
    all_calc_fields = []
    for ds in root.findall("./datasources/datasource"):
        if ds.get("name") == "Parameters":
            continue
        connection = ds.find(".//connection")
        fields = extract_fields_from_datasource(ds)
        for f in fields:
            if f["is_calculated"]:
                f["formula_resolvida"] = resolve_formula(f["formula_raw"], name_to_caption)
                f["classificacao"] = classify_calc(f["formula_raw"])
                all_calc_fields.append(f)
        datasources.append({
            "nome": ds.get("name"),
            "caption": ds.get("caption") or ds.get("name"),
            "connection_class": connection.get("class") if connection is not None else None,
            "campos": fields,
        })

    result = {
        "arquivo_origem": str(path),
        "datasources": datasources,
        "parametros": extract_parameters(root),
        "campos_calculados": all_calc_fields,
        "grafo_dependencias": build_dependency_graph(all_calc_fields, name_to_caption),
        "worksheets": extract_worksheets(root, name_to_caption, instance_to_column),
        "dashboards": extract_dashboards(root),
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()