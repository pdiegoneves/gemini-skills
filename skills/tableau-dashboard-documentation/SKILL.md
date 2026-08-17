---
name: tableau-dashboard-documentation
description: >-
  Gera ou atualiza a documentação técnica completa de um dashboard/workbook Tableau (.twb
  ou .twbx), extraindo TODOS os campos calculados com a fórmula completa, parâmetros,
  fontes de dados, planilhas e dashboards, além do grafo de dependência entre fórmulas. Use
  sempre que o usuário enviar/mencionar um .twb/.twbx, ou pedir para "documentar esse
  dashboard", "extrair as fórmulas desse workbook", "mapear os campos calculados", "listar
  os cálculos do dashboard" ou "rodar o tvdoc" — mesmo de forma abreviada. Geração e
  atualização são fluxos diferentes: geração escreve do zero; atualização compara um novo
  .twbx contra a documentação existente e registra o que mudou. Não é para análise dos
  DADOS/números do dashboard — é para a ESTRUTURA e as FÓRMULAS do workbook.
---

# tvdoc — Documentação Técnica de Dashboards Tableau

Esta skill gera (ou atualiza) a documentação técnica oficial de um workbook Tableau a
partir do próprio arquivo `.twb`/`.twbx`, sempre seguindo a mesma estrutura fixa. O
objetivo é o mesmo da `technical-documentation` (tdoc) para software: qualquer pessoa —
outro analista, um dev que vai dar manutenção no dashboard, ou um stakeholder de negócio —
consegue entender o que cada número da tela realmente calcula lendo um único documento,
sem precisar abrir o Tableau e caçar fórmula por fórmula na interface.

## Por que extrair via XML em vez de descrever de memória

Um `.twb` é XML puro, e um `.twbx` é esse mesmo XML dentro de um `.zip` (junto com
extratos de dados e imagens). Toda fórmula de campo calculado, parâmetro, planilha e
dashboard está literalmente escrita nesse XML — então a única forma de documentação
confiável é ler o arquivo, nunca inferir ou "lembrar" o que uma fórmula provavelmente faz
pelo nome do campo. Um campo chamado `Profit Ratio` pode calcular qualquer coisa; só a
fórmula real importa.

## Passo 1 — Determinar o modo: geração ou atualização

Igual à tdoc, decida isso antes de qualquer coisa:

- **Geração (do zero)**: o usuário pede para "gerar"/"criar" a documentação, ou não existe
  ainda nenhum documento de dashboard no formato desta skill para esse workbook.
- **Atualização**: o usuário envia uma nova versão do mesmo `.twbx` e pede para
  "atualizar"/"revisar"/"sincronizar" a documentação, ou já existe um documento no formato
  desta skill (reconhecível pelo cabeçalho `# Documentação Técnica - Dashboard ...`).

Se for ambíguo, assuma **atualização** quando já existir um documento anterior para o
mesmo workbook — reescrever do zero descartaria anotações manuais (ex.: contexto de
negócio sobre por que uma fórmula existe) que o XML sozinho não recupera.

## Passo 2 — Extrair os dados do workbook

Use o script bundlado em vez de ler o XML manualmente linha a linha — um workbook real
pode ter dezenas de campos calculados e milhares de linhas de XML, e regex livre nesse
volume é onde erros de leitura acontecem.

```bash
python3 scripts/extract_twb.py caminho/para/arquivo.twbx > /tmp/extracao.json
```

Funciona tanto para `.twbx` (empacotado) quanto para `.twb` (solto). A saída é um JSON
com:

- `datasources`: cada fonte de dados, sua classe de conexão, e todos os campos (calculados
  ou não).
- `parametros`: nome, tipo, valor padrão e valores permitidos de cada parâmetro.
- `campos_calculados`: fórmula bruta, fórmula **resolvida** (com os IDs internos tipo
  `[Calculation_123...]` já substituídos pelo nome/caption legível — inclusive quando um
  cálculo referencia outro cálculo), e uma classificação automática (padrão / LOD / cálculo
  de tabela).
- `grafo_dependencias`: para cada campo calculado, quais outros campos calculados ele usa
  (`depende_de`) e por quais ele é usado (`usado_por`) — a base do diagrama do Passo 4.
- `worksheets` e `dashboards`: planilhas, campos usados em cada uma, filtros, e quais
  planilhas compõem cada dashboard.

**O que o script não cobre com confiança** (leia o `.twb` bruto se precisar preencher
isso): grupos, conjuntos (sets) e bins têm uma estrutura de XML própria (`<groupfilter>`)
diferente de `<calculation>`, então não aparecem automaticamente na lista de campos
calculados — se o workbook usa algum, procure por eles manualmente e documente à parte. O
posicionamento exato de cada campo nas prateleiras (linhas/colunas/marcas) também não é
reconstruído pixel a pixel — o que importa para documentação técnica é *quais* campos cada
planilha usa, não o layout visual exato. E o script nunca lê o extrato de dados (`.hyper`)
em si — só a definição do workbook, o que já é suficiente para documentação "a nível de
fórmula".

**Cuidado com dados sensíveis**: o XML de conexão pode conter hostname de banco, usuário de
conexão, ou nome de servidor. Inclua só o que for útil para quem for dar manutenção (tipo
de banco, se é live ou extract) — não copie strings de conexão completas para o documento
final.

## Passo 3A — Fluxo de geração (do zero)

1. Rode a extração (Passo 2).
2. Preencha **todas** as seções do template (Passo 4).

## Passo 3B — Fluxo de atualização

1. Leia o documento existente por completo.
2. Rode a extração (Passo 2) na nova versão do `.twbx`.
3. Compare o que mudou:
   - **Campos calculados**: algum `technical_name` novo apareceu? Algum sumiu? Para os que
     continuam existindo, a `formula_resolvida` é a mesma que está documentada, ou mudou?
   - **Parâmetros**: novos, removidos, ou valor padrão/permitido alterado.
   - **Planilhas e dashboards**: novos, removidos, ou mudança em quais campos/filtros uma
     planilha usa.
   - **Fontes de dados**: nova conexão adicionada ou removida.
3. Aplique ajustes **apenas nos pontos que mudaram** — não reescreva descrições de campos
   que continuam idênticos, e principalmente não descarte anotações manuais de contexto de
   negócio que alguém tenha adicionado a um campo (o "por quê" de uma fórmula raramente
   está no XML).
4. Adicione linha(s) novas na tabela **Alterações**, com a data de hoje, o campo/elemento
   afetado, e o que mudou (ex.: "fórmula de `Profit Ratio` passou a excluir devoluções").

## Passo 4 — Preencher o template

Use **exatamente** esta estrutura:

```markdown
# Documentação Técnica - Dashboard [Nome do Workbook]

## Visão Geral

### Objetivo do dashboard

### Fontes de dados

| Fonte | Tipo de conexão | Live / Extract | Observações |
|-------|------------------|-----------------|-------------|

### Diagrama de dependência de fórmulas

```mermaid
[diagrama aqui — ver orientação abaixo]
```

## Parâmetros

| Nome | Tipo | Valor padrão | Valores permitidos | Onde é usado |
|------|------|---------------|----------------------|--------------|

## Campos Calculados

### [Nome do campo]

- **Fonte de dados:** [nome da datasource]
- **Fórmula:** `[formula_resolvida]`
- **Tipo de cálculo:** Padrão / LOD (Level of Detail) / Cálculo de tabela
- **Depende de:** [outros campos calculados referenciados, se houver]
- **Usado por:** [outros campos calculados que o referenciam, se houver]
- **Usado nas planilhas:** [planilhas onde aparece]

(repita um bloco `###` por campo calculado)

## Grupos, Conjuntos e Bins

[liste manualmente se o workbook usar algum — não são extraídos automaticamente. Se não
houver nenhum, deixe uma nota objetiva dizendo isso.]

## Planilhas (Worksheets)

### [Nome da planilha]

- **Fonte de dados:**
- **Campos usados:**
- **Filtros aplicados:**

## Dashboards

### [Nome do dashboard]

- **Planilhas que compõem:**
- **Ações:** [ações de filtro/destaque/URL, se identificáveis no XML]

## Troubleshooting

- Descrição do problema:
- Causa raiz:
- Solução aplicada:

## Alterações

| Data | Campo/Elemento | Alteração | Motivo |
|------|-----------------|-----------|--------|
```

Orientações por seção:

- **Nome do Workbook**: use o `caption`/nome do arquivo do workbook.
- **Objetivo do dashboard**: 2-4 frases sobre que decisão de negócio ele apoia e para quem
  — puxe isso da conversa com o usuário se ele explicar o contexto; o XML não tem essa
  informação.
- **Fontes de dados**: uma linha por `datasource` do JSON extraído (ignorando a datasource
  interna `Parameters`, que já tem seção própria).
- **Diagrama de dependência de fórmulas**: monte um `flowchart LR` a partir de
  `grafo_dependencias` — uma seta de cada campo para os campos que ele usa. Inclua também os
  campos "folha" (não calculados) que alimentam diretamente algum cálculo, para que o
  diagrama mostre a cadeia completa até o dado bruto. Se o workbook tiver muitos campos
  calculados (dezenas), um único diagrama fica ilegível — nesse caso, divida em um diagrama
  por fonte de dados, ou substitua o diagrama por uma coluna "Depende de" na tabela e avise
  o usuário por que optou por isso.
- **Campos Calculados**: um `###` por campo, usando `formula_resolvida` (nunca a fórmula
  bruta com IDs internos tipo `[Calculation_...]` — isso não tem valor de leitura para
  ninguém revisando o documento).
- **Planilhas/Dashboards**: liste os campos e filtros reais encontrados em
  `worksheets`/`dashboards`; se uma planilha usa muitos campos, priorize os que aparecem em
  algum cálculo documentado.
- **Troubleshooting**: só preencha com problemas reais relatados pelo usuário ou pela
  versão anterior do documento — nunca invente incidentes.
- **Alterações**: na primeira geração, uma linha inicial registrando a criação do
  documento; nas atualizações, sempre adicione linha nova em vez de editar as antigas.

## Passo 5 — Salvar e entregar

- Se houver uma ferramenta de apresentação de arquivos disponível no ambiente (ex.:
  `present_files`), salve o documento em `/mnt/user-data/outputs/` com o nome
  `[nome-do-workbook]-documentacao.md` e entregue com essa ferramenta.
- Caso contrário, salve como `[nome-do-workbook]-documentacao.md` na mesma pasta do
  arquivo `.twb`/`.twbx` de origem.

Ao final, informe rapidamente ao usuário:

- **Se foi geração**: quantos campos calculados, parâmetros, planilhas e dashboards foram
  documentados, e quais seções ficaram com lacunas por falta de informação (ex.: grupos ou
  sets que precisam de revisão manual).
- **Se foi atualização**: quais campos/elementos mudaram desde a última versão e o que foi
  mantido como estava.