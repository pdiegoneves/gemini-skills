# Template — VSM (Mapeamento do Fluxo de Valor)

**Quando usar:** SEMPRE antes de recomendar qualquer outra ferramenta Lean para uma situação nova. É a ferramenta de diagnóstico mais poderosa — revela onde o tempo, o dinheiro e a energia estão sendo devorados.

## Passo 1 — Escolher a família de produto/serviço
Um VSM mapeia uma família (produtos/serviços com passos similares), não a fábrica/empresa inteira de uma vez.

## Passo 2 — Mapear o Estado Atual (Current State)
Percorra o processo do fim para o início (do cliente para o fornecedor), a pé, no Gemba — não a partir de um fluxograma de sistema.

Para cada etapa do processo, registre:
- **Tempo de Ciclo (C/T):** tempo para processar 1 unidade.
- **Tempo de Setup/Troca (C/O):** tempo de troca entre variantes.
- **Disponibilidade:** % de tempo que a etapa está disponível para produzir.
- **Nº de operadores.**
- **Tamanho do lote / WIP entre etapas.**
- **Taxa de defeito / retrabalho.**

Entre cada etapa, registre o **tempo de espera** (inventário parado, fila, aprovação pendente).

### Legenda de símbolos padrão (mínima)
| Símbolo | Significado |
|---|---|
| Caixa de processo | Uma etapa/estação de trabalho |
| Triângulo | Estoque/inventário em espera (anote a quantidade e o tempo que representa) |
| Seta larga | Fluxo de material/produto (empurrado) |
| Seta em zig-zag | Fluxo de informação eletrônica |
| Seta reta fina | Fluxo de informação manual |
| Caixa de dados abaixo do processo | C/T, C/O, disponibilidade, nº operadores |
| Linha do tempo (embaixo do mapa) | Soma o tempo de valor agregado (dentro das caixas de processo) vs. tempo de não-valor agregado (nos triângulos de espera) |

## Passo 3 — Calcular as métricas de fluxo
- **Lead Time total** = soma de todos os tempos de espera + tempos de processamento.
- **Tempo de Valor Agregado** = soma apenas dos tempos em que o cliente pagaria pela atividade.
- **% Valor Agregado** = Tempo de Valor Agregado ÷ Lead Time total. (Em processos não otimizados, é comum estar abaixo de 5%.)
- **Takt Time** = tempo disponível ÷ demanda do cliente (ver `glossario.md`).

## Passo 4 — Identificar gargalos e desperdícios
Marque no mapa (ícone de "explosão kaizen") onde há: maior acúmulo de inventário/espera, maior variação de C/T entre etapas, maior taxa de defeito, e qualquer etapa que o cliente não pagaria por ela.

## Passo 5 — Desenhar o Estado Futuro (Future State)
Não é "eliminar tudo de uma vez" — é priorizar por impacto no lead time do cliente. Para cada gargalo marcado, indique qual ferramenta Lean o ataca (Kanban para desacoplar etapas de velocidade diferente, SMED para reduzir lote, 5S/Trabalho Padrão para reduzir variação, Poka-Yoke para reduzir defeito).

## Passo 6 — Plano de ação
Lista priorizada de iniciativas para sair do Estado Atual ao Estado Futuro, cada uma com dono, prazo e a métrica de fluxo que ela deve mover.

---

**Erro comum a evitar:** mapear o estado atual em uma sala, a partir de memória ou de um SOP — vá ao Gemba. Números de memória subestimam tempo de espera em ~50%, segundo observação de campo recorrente.
