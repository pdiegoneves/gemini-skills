# Casos Reais e Cenários de Diagnóstico

Banco de casos para usar como analogia, evidência ou estrutura de raciocínio. Sempre cite o caso pelo nome quando usá-lo ("como na Alcoa de Paul O'Neill...") — nunca apresente o raciocínio do caso como se fosse genérico sem dar o crédito à fonte.

## Alcoa — Paul O'Neill (1987–2000)

Paul O'Neill assumiu o CEO da Alcoa e escolheu **segurança** — não lucratividade — como métrica-alvo número um. Racional: lucratividade depende de variáveis fora do controle local (preço de commodity, câmbio, demanda global); segurança é 100% controlável localmente e é um **sintoma universal de processo quebrado**. Cada acidente revela máquina mal calibrada, procedimento confuso, falta de padronização ou treinamento insuficiente. Corrigir a segurança corrige a eficiência como efeito colateral. Resultado: acidentes caíram ~95%, valor de mercado multiplicou por 5 em 13 anos.

**Uso na consultoria:** quando o usuário quiser escolher uma métrica-alvo única para uma virada cultural, pergunte se a métrica proposta é controlável localmente e é sintoma de processo — não resultado de fatores externos.

## GM Fremont → NUMMI (1982–1984 / depois)

A fábrica da GM em Fremont foi fechada em 1982 por baixíssima produtividade e péssima qualidade — absenteísmo de 20%, greves, sabotagem. Reabriu como joint-venture com a Toyota (NUMMI), com **80% dos mesmos trabalhadores** e mesmos sindicatos. Em 1 ano, tornou-se a planta mais produtiva da GM nos EUA, com a menor taxa de defeitos.

**O que mudou:** não os trabalhadores — o sistema de gestão.
- **Fremont (GM sozinha):** sistema Push com metas de volume; trabalhador punido por parar a linha (Jidoka impossível); qualidade era responsabilidade do inspetor final, não do operador.
- **NUMMI (Toyota + GM):** Andon real (qualquer um parava a linha), qualidade na fonte, equipe de resposta rápida (chegava em <1 min), Kaizen com implementação rápida das sugestões.

**A lição que o fracasso ensina e o sucesso não ensina:** a GM tentou copiar Kanban/5S/Andon em outras plantas por décadas e fracassou repetidamente — porque copiou a **ferramenta**, não a **cultura de confiança e resposta**. Gestores japoneses passavam 50% do tempo na linha, ouvindo operadores. A ferramenta é fácil de copiar; a cultura é quase impossível de replicar sem liderança presente.

**Uso na consultoria:** é o caso-referência sempre que o usuário relatar "problema de gente" (resistência, desmotivação, sabotagem). Primeira hipótese: sistema de gestão, não caráter.

## O Paradoxo do OEE na Intel (anos 1990)

A Intel descobriu que sua fábrica de chips com **maior OEE individual** (máquinas mais ocupadas) era a que **mais atrasava** a entrega final — eficiência local otimizada gerava filas globais entre máquinas de velocidades diferentes. Solução: medir eficiência de fluxo (Dock-to-Dock Time), não OEE isolado.

## Matriz de Priorização de Kaizen — Danaher Corporation

A Danaher usa uma matriz de 3 critérios para aprovar ou recusar sugestões de Kaizen: **Impacto no lead time do cliente × Facilidade de implementação × Alinhamento estratégico**. Kaizen que não passa nos 3 é recusado, por mais brilhante que seja tecnicamente — evita que engenheiros bons gastem tempo em problemas irrelevantes ao gargalo real.

## Heijunka na Dana Corporation

Fornecedora automotiva implementou Heijunka numa linha com 40 modelos diferentes. Resultado: inventário caiu 70%, mas exigiu reduzir setup de 45 min para 8 min (via SMED). Investimento em troca rápida pagou-se em 14 meses. Ilustra a dependência Heijunka ⇄ SMED.

---

## Cenário de Diagnóstico 1 — "Desafio de Premissas Ocultas" (Kanban em Marketing)

**Situação:** uma empresa de software B2B implementou Kanban com limite de WIP de 3 itens por desenvolvedor; lead time caiu de 14 para 6 dias. O CEO decide expandir o mesmo limite (WIP=3) para todo o Marketing (20 pessoas), esperando reduzir o tempo de lançamento de campanha.

**Premissa oculta a desafiar:** WIP baixo reduz lead time quando o trabalho é homogêneo e o gargalo é troca de contexto (caso do dev). Em Marketing, o "lead time" de uma campanha pode não ser proporcional ao WIP — pode depender de ciclos de aprovação, criação criativa e testes de mercado que não encurtam por reduzir WIP; podem até piorar se forçados a andar em paralelo picotado. **Antes de replicar uma solução, valide se a causa raiz do problema no novo contexto é a mesma do contexto original.**

## Cenário de Diagnóstico 2 — "A Fábrica Fantasma" (Lean como sistema de controle punitivo)

**Situação:** fábrica que implementou Kanban, 5S, Andon e Kaizen — mas o 5S virou auditoria de sexta-feira ligada a bônus; ferramentas fora do lugar tiram pontos; operadores escondem ferramentas antes da auditoria.

**Diagnóstico:** o problema não é Lean — é que Lean foi implementado como **sistema de controle**, não como **sistema de aprendizado**. Kanban sem confiança = decoração. Andon sem segurança psicológica = pânico. Kaizen sem ownership local = evento vazio. 5S sem propósito = fiscalização. A variável central é a relação operador-supervisor (punitiva, competitiva, hierárquica).

**Plano de 90 dias (estrutura a reutilizar em diagnósticos análogos):**
- **Dias 1–30 — Restaurar confiança antes de tocar em ferramenta:** declarar publicamente que ninguém será punido por parar a linha, reportar defeito ou sugerir melhoria (só por esconder problema); Gemba walk diário da liderança perguntando "qual o maior problema hoje?" e resolvendo os 3 primeiros em 48h; abandonar competição entre turnos; Andon "sombra" anônimo via QR code com resposta em 5 min.
- **Dias 31–60 — Reconstrução das ferramentas:** Kanban recriado pelos próprios operadores; 5S diário de 5 min no início do turno (supervisor investiga, não inspeciona); Kaizen local com implementação em 72h e teste de 1 semana, sem culpa se não funcionar.
- **Dias 61–90 — Sustentação e métricas:** Obeya room com VSM atualizado semanalmente; métricas de confiança (nº de paradas de Andon por semana — quanto mais, melhor, significa segurança para reportar; taxa de implementação de sugestões; tempo médio de resposta); celebração pública creditada à equipe, bônus coletivo.

**Uso na consultoria:** aplique esta estrutura de 4 fases (diagnóstico → ação imediata de confiança → reconstrução de ferramentas → sustentação/métricas) sempre que o modo de consulta for "diagnosticar situação → solução".
