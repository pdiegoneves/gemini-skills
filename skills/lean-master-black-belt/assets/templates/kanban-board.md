# Template — Quadro Kanban

**Quando usar:** visualizar e limitar trabalho em progresso (WIP) em um fluxo já minimamente estável. **Não use Kanban como primeiro passo** — se o processo ainda é caótico, Kanban vira caos com post-it (ver princípio "Pull exige processo estável" em `fundamentos-e-pilares.md`).

## Passo 1 — Definir as colunas (etapas do fluxo)
Baseie-se no VSM, não em achismo. Ex.: `A Fazer → Em Andamento → Em Revisão → Concluído`. Cada coluna é uma etapa real do processo, não uma categoria administrativa.

## Passo 2 — Definir limite de WIP por coluna
Pergunta a fazer ao usuário: "Qual a capacidade real de processamento simultâneo desta etapa hoje?" O limite deve ser levemente abaixo da capacidade observada — não um número arbitrário.

| Coluna | Limite de WIP | Responsável pela etapa |
|---|---|---|
| ... | ... | ... |

## Passo 3 — Regra de puxar (Pull)
Escreva a regra explícita: "Um item só entra na próxima coluna quando há vaga (abaixo do limite de WIP)." Isso é o que torna o quadro **Pull** de fato, e não decoração visual.

## Passo 4 — Cartão-tipo
Cada cartão deve conter, no mínimo: identificação do item, data de entrada na coluna atual, bloqueio (se houver) e dono.

## Passo 5 — Sinalização de bloqueio
Defina como um item "travado" é sinalizado visualmente (ex: tag vermelha) e qual o SLA para des-bloquear — sem isso, itens travados acumulam silenciosamente e quebram o limite de WIP na prática.

## Passo 6 — Cadência de revisão
Reunião curta e recorrente (diária ou conforme o ritmo do fluxo) revisando: itens travados, colunas no limite de WIP, itens parados há mais tempo que o esperado.

---

**Kanban de peças (supermercado)**, variante para reposição de estoque/insumos: em vez de colunas de fluxo de trabalho, use um "slot" por SKU com quantidade fixa; a retirada de um item dispara o sinal de reposição do próximo. Use esta variante quando o problema é reposição/abastecimento, não fluxo de tarefas.
