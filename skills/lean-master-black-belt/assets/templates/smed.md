# Template — SMED (Single-Minute Exchange of Die)

**Quando usar:** setup/troca de ferramenta, pedido, configuração ou contexto está demorado o suficiente para inviabilizar lotes menores ou Heijunka. Meta: setup abaixo de 10 minutos ("single-minute" = dígito único de minutos).

## Passo 1 — Filmar/medir o setup atual
Cronometre do fim da última unidade do lote anterior até a primeira unidade boa do lote novo. Não estime — meça (ver nota em `vsm.md` sobre subestimação de tempo).

## Passo 2 — Listar todas as atividades do setup, na ordem
Uma linha por atividade, com tempo individual.

## Passo 3 — Classificar cada atividade
| Atividade | Interna (só com máquina/processo parado) | Externa (pode ser feita com máquina/processo rodando) |
|---|---|---|
| ... | | |

## Passo 4 — Converter interna → externa (a maior alavanca do SMED)
Para cada atividade interna, pergunte: "isso realmente precisa da máquina parada, ou só precisamos preparar/organizar antes?" Ex.: separar ferramentas, pré-aquecer, pré-configurar parâmetros — tudo isso pode, em geral, virar externo.

## Passo 5 — Simplificar o que continua interno
Elimine ajustes por tentativa-e-erro (use batentes, marcações, padronização de posição); elimine fixação por parafuso onde encaixe rápido resolve; padronize ferramentas usadas.

## Passo 6 — Simplificar o que virou externo
Organize com 5S (shadow board, kit pré-montado) para que a preparação externa também seja rápida e sem busca.

## Passo 7 — Medir o novo tempo e documentar como Trabalho Padrão
Atualize `trabalho-padrao.md` com a nova sequência — sem isso, o ganho regride com o tempo.

---

**Lembrete de dependência:** se o objetivo de fundo é viabilizar Heijunka (nivelamento), o SMED não é opcional — é pré-condição (ver caso Dana Corporation em `casos-reais.md`).
