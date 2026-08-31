# Template — TPM (Total Productive Maintenance) e OEE

**Quando usar:** medir e melhorar a saúde de um equipamento/recurso crítico. **Cuidado com a armadilha:** OEE mede a máquina isolada; use sempre junto com uma métrica de fluxo (Dock-to-Dock Time, lead time) para não cair no Paradoxo da Eficiência Local (`fundamentos-e-pilares.md`).

## Cálculo do OEE
**OEE = Disponibilidade × Performance × Qualidade**

| Componente | Fórmula | O que revela |
|---|---|---|
| Disponibilidade | Tempo de operação ÷ Tempo planejado de produção | Perdas por parada (quebra, setup, falta de material) |
| Performance | (Nº de peças produzidas × Tempo de ciclo ideal) ÷ Tempo de operação | Perdas por micro-paradas e velocidade reduzida |
| Qualidade | Peças boas ÷ Total de peças produzidas | Perdas por retrabalho/refugo |

**Meta de referência (mundo Lean):** OEE > 85% é considerado classe mundial — mas trate como norte, não como meta cega desconectada do fluxo real.

## As 6 Grandes Perdas (mapeadas nos 3 componentes acima)
1. Quebra de equipamento (Disponibilidade)
2. Setup e ajustes (Disponibilidade)
3. Pequenas paradas / operação em vazio (Performance)
4. Velocidade reduzida (Performance)
5. Defeitos no processo (Qualidade)
6. Perdas de start-up / rendimento reduzido (Qualidade)

## Os 8 Pilares do TPM (visão geral — aprofunde o pilar relevante ao caso)
1. Manutenção Autônoma — operador cuida da limpeza/inspeção/lubrificação básica do próprio equipamento.
2. Manutenção Planejada — manutenção preventiva/preditiva com cronograma, não reativa.
3. Melhoria Específica (Kaizen focado nas 6 grandes perdas).
4. Manutenção da Qualidade — atacar defeito na fonte do equipamento, não só na inspeção final.
5. Controle Inicial — projetar novos equipamentos já pensando em manutenibilidade.
6. Treinamento e desenvolvimento de habilidades.
7. TPM em áreas administrativas.
8. Segurança, saúde e meio ambiente.

## Template de análise
- **Equipamento/recurso:** ______
- **OEE atual:** Disponibilidade ___% × Performance ___% × Qualidade ___% = ___%
- **Maior das 6 grandes perdas neste caso:** ______ (priorize por impacto, não pela mais visível)
- **Pilar do TPM mais relevante para atacar essa perda:** ______
- **Métrica de fluxo a acompanhar em paralelo** (para não otimizar a máquina às custas do sistema): ______
