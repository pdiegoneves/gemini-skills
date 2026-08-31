# Template — DMAIC (Six Sigma / Lean Six Sigma)

**Quando usar:** problema de qualidade ou processo com **variação estatística relevante**, dados suficientes para análise quantitativa, e necessidade de rigor maior que um A3. Mais pesado que A3 — reserve para problemas que justifiquem o investimento de tempo.

## Define (Definir)
- **Declaração do problema:** específica, mensurável, sem apontar causa ou solução ainda.
- **Voz do cliente (VOC):** o que o cliente considera crítico para qualidade (CTQ).
- **Escopo:** onde começa e termina o processo em análise.
- **Equipe e patrocinador (sponsor).**

## Measure (Medir)
- **Métrica(s) primária(s)** e como são coletadas hoje.
- **Baseline atual** (com tamanho de amostra e período).
- **Sistema de medição validado?** (Gage R&R se aplicável — se a medição em si não é confiável, nada abaixo disso é confiável).
- **Mapa do processo atual** (SIPOC ou VSM).

## Analyze (Analisar)
- **Hipóteses de causa** geradas com Ishikawa/Brainstorming.
- **Validação estatística das causas** (Pareto, correlação, teste de hipótese — conforme dado disponível). Não aceite "achamos que é X" sem teste, se há dado disponível para testar.
- **Causa(s) raiz confirmada(s)**, priorizada(s) por impacto.

## Improve (Melhorar)
- **Soluções propostas** para cada causa raiz confirmada.
- **Piloto controlado** (não implante direto em escala plena).
- **Resultado do piloto** vs. baseline, com significância (não só "parece melhor").

## Control (Controlar)
- **Plano de controle:** o que será monitorado, com que frequência, por quem, e o que dispara ação se sair do controle (limites de controle, não achismo).
- **Trabalho Padrão atualizado** (ver `trabalho-padrao.md`).
- **Transferência de ownership** ao dono do processo — DMAIC de projeto termina, mas o controle é permanente.

---

**Quando DMAIC é overkill:** se o problema não tem variação estatística relevante (é binário: "acontece" ou "não acontece" por causa óbvia), ou os dados disponíveis são insuficientes para análise quantitativa, prefira A3 ou PDCA — DMAIC mal aplicado em problema simples desperdiça tempo de engenharia (mesmo raciocínio da matriz de Kaizen da Danaher).
