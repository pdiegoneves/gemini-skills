# As Três Escolas de Pensamento Lean — e Quando Usar Cada Uma

Use este arquivo quando o usuário confundir Lean tradicional com Lean Startup ou Lean Agile/DevOps, ou quando precisar escolher qual escola aplicar a uma situação.

## Escola 1 — Lean Tradicional (Toyota Production System)
**Foco:** eliminação de desperdício em processos repetitivos, manufatura, fluxo linear.
**Referências:** Taiichi Ohno, Shigeo Shingo, Jeffrey Liker (*The Toyota Way*).
**Método:** VSM, 5S, Kanban, Jidoka, SMED, PDCA.
**Prescrição:** vá ao Gemba, observe, padronize, melhore.
**Quando usar:** processo já conhecido, repetitivo, com histórico — a incerteza é baixa/moderada.

## Escola 2 — Lean Startup (Eric Ries, Steve Blank)
**Foco:** eliminação de desperdício em contextos de **incerteza extrema** (mercado novo, tecnologia nova).
**Método:** Build-Measure-Learn, MVP, pivotar rápido.
**Prescrição:** não planeje demais — teste hipóteses com clientes reais o mais rápido possível.

## Escola 3 — Lean Agile / DevOps (Mary Poppendieck, Gene Kim, Jez Humble)
**Foco:** fluxo contínuo em software e operações de TI.
**Método:** CI/CD, WIP limitado em boards digitais, métricas DORA (Deployment Frequency, Lead Time for Changes, Change Failure Rate, Time to Restore Service — referência: *Accelerate*, Forsgren/Humble/Kim, 2018).
**Prescrição:** automatize o repetitivo, mantenha humanos para decisão e criatividade.

## Como escolher entre as três
A escolha da escola é **contingente ao nível de incerteza da situação** — não ideológica. Incerteza baixa/moderada (processo conhecido, negócio estabelecido, versão 2.0 de produto existente) → Lean Tradicional. Incerteza extrema (mercado desconhecido, hipótese central não validada) → Lean Startup. Fluxo de entrega de software/TI → Lean Agile/DevOps, com Lean Tradicional fornecendo o framework de fluxo por baixo.

## Crítica Fundamentada ao Uso Indevido de Lean Startup

Lean Startup é a escola mais popular — e a mais perigosamente mal compreendida. Quatro pontos de crítica a ter prontos quando o usuário citar "MVP" ou "fail fast" fora de contexto:

1. **Confusão entre "desperdício" e "incerteza".** Lean tradicional define desperdício como atividade que não cria valor para o cliente. Lean Startup define como "esforço que não gera aprendizado validado" — conceitos diferentes e às vezes conflitantes. Trabalho de infraestrutura e padronização sem feedback imediato do cliente não é desperdício no sentido tradicional, mas pode ser rotulado como tal no vocabulário Lean Startup.
2. **O culto do MVP.** "Mínimo" é subjetivo; produtos lançados minimalistas demais queimam reputação de marca. MVP deve ser "mínimo viável", não "mínimo vergonhoso" — e Lean Startup não oferece critério claro para distinguir um do outro.
3. **A fetichização da velocidade.** "Fail fast" virou desculpa para falta de estratégia. A maioria das startups falha por falta de diferenciação, não por falta de velocidade — pivotar rápido é inútil sem direção.
4. **Apropriação do termo "Lean".** Milhares de empresas fazem "Lean Startup" sem nunca ter mapeado um fluxo de valor ou entendido o que é muda — o termo virou buzzword esvaziado da profundidade do sistema Toyota.

**Contraponto justo:** Lean Startup é valioso quando aplicado corretamente, em contextos de incerteza extrema. O erro é aplicá-lo a contextos de incerteza moderada (abrir uma padaria, lançar v2.0 de produto existente), onde Lean tradicional é superior.

## Fronteiras Atuais em Debate (sem consenso — apresente como debate, não como fato fechado)
- **Lean vs. Agile vs. DevOps são complementares ou concorrentes?** Visão emergente (DORA/*Accelerate*): Lean dá o framework de fluxo, Agile o ritmo de iteração, DevOps a automação — mas muitos consultores ainda vendem um como substituto do outro.
- **Lean em economia de plataforma (Amazon, Uber, Airbnb):** plataformas digitais têm rede de valor, não cadeia de valor. Desperdício aqui é latência de API, matching ineficiente, fricção de onboarding — pesquisadores (ex: John Hagel) argumentam que Lean precisa ser reescrito para economia de rede, sem consenso de como.
- **Lean e sustentabilidade:** Lean reduz desperdício de material/energia/transporte, mas críticos (ex: Paul Hawken) argumentam que Lean apenas otimiza o modelo de negócio existente (ex: fast fashion) — "faz o errado mais eficiente". Debate aberto sobre compatibilidade real com economia circular.

## Consensos Desatualizados (corrija se o usuário repetir)
- **"Lean é só para manufatura"** — desmentido há 20 anos: Lean Healthcare (Virginia Mason), Lean Startup, Lean Software (Poppendieck), Lean Construction (LCI) são campos maduros.
- **"Lean elimina empregos"** — mito. Lean redistribui trabalho (de inspeção 100% para resolução de problema na fonte). O desafio é reskilling, não demissão.
- **"5S é o primeiro passo do Lean"** — parcialmente verdadeiro. 5S é pré-requisito para visualização e padronização, mas não é o primeiro passo se a empresa não sabe o que é valor para o cliente. 5S sem VSM é arrumação vazia.
