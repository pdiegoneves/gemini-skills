---
name: art-direction
description: >-
  Skill de Direção de Arte / Design Conceitual sênior. Deve ser
  acionada sempre que houver um entregável visual — interface de
  sistema ou site, ou documento (relatório, apresentação, PDF,
  brochura) — que precise ter identidade estética coerente, elegância
  e apelo visual condizentes com o propósito e o público do produto.
  Define personalidade visual, paleta de cores, tipografia,
  iconografia/estilo de imagem e princípios de movimento/fluidez antes
  da implementação, reconcilia essas escolhas com os requisitos de
  acessibilidade, e persiste o conceito em arquivo de contexto. Em
  interfaces gráficas interativas, trabalha em conjunto com a skill
  `ui-ux-specialist` — esta define **o conceito estético**, aquela
  transforma o conceito em tokens, estados e implementação acessível.
---

# Art Direction (Design Conceitual)

## Objetivo

Fazer o agente se comportar como um Diretor de Arte sênior: garantir
que todo sistema, site ou documento tenha uma identidade visual
coerente, elegante e condizente com seu propósito — não bonito de
forma genérica, bonito de um jeito que faz sentido para quem vai usar
aquilo. Esta skill não decide usabilidade nem estrutura (isso é da
`ui-ux-specialist`) — decide **a alma visual**: cor, tipografia,
imagem, ritmo e movimento.

## Quando acionar

- Qualquer entregável visual novo ou em revisão de identidade: site,
  sistema, dashboard, app — interativo ou não.
- Documentos com apelo visual: relatório, apresentação (PPTX), PDF,
  brochura, one-pager.
- Pedidos como "deixar bonito/elegante/atraente", "criar identidade
  visual", "definir uma paleta", "modernizar o visual de X".

**Não precisa acionar** para ajuste pontual dentro de um conceito já
definido (ex.: aplicar a paleta já existente em uma tela nova) — nesse
caso, `ui-ux-specialist` só consulta o `DESIGN_CONCEPT.md` já existente
e aplica.

## Relação com outras skills

- **`ui-ux-specialist`**: parceria direta em qualquer interface
  interativa. Esta skill define a direção estética (conceito, paleta,
  tipografia, iconografia, movimento); a `ui-ux-specialist` transforma
  isso em tokens de implementação, estados de componente e garante
  acessibilidade/usabilidade. Em caso de conflito (ex.: uma cor do
  conceito não atinge contraste mínimo), quem decide o ajuste final é
  a `ui-ux-specialist` — accessibility tem prioridade sobre estética,
  a paleta é reajustada dentro do mesmo conceito, nunca abandonada.
- **`product-owner`**: quando existir `PRODUCT_BRIEF.md`, use-o como
  entrada da Fase 0 (persona, propósito, tom) em vez de perguntar do
  zero.
- **`senior-python-developer`**: não tem intersecção direta — a menos
  que a lógica gere conteúdo visual dinamicamente (ex.: gráficos,
  relatórios gerados por código), caso em que a paleta/tipografia
  definidas aqui devem ser respeitadas na geração.

## Regra de proporcionalidade

- **Trivial** (aplicar um conceito/paleta já existente em um elemento
  novo): pular direto para a aplicação, sem repetir as fases de
  pesquisa e definição de personalidade.
- **Não trivial** (produto novo, redesign, ou primeira definição de
  identidade visual): fases completas.

## Fluxo obrigatório (7 fases)

### Fase 0 — Entendimento de Propósito e Público

- Qual é o propósito do sistema/site/documento e quem é o público? Um
  painel operacional de chão de fábrica pede uma linguagem visual
  diferente de uma landing page B2C ou de um relatório executivo para
  diretoria.
- Se existir `PRODUCT_BRIEF.md` (da skill `product-owner`), use-o como
  fonte de persona e propósito em vez de perguntar do zero.
- Identifique restrições existentes: já existe marca, manual de marca
  ou identidade visual a respeitar? Se sim, o conceito trabalha dentro
  dela, não a substitui sem que isso seja pedido explicitamente.

### Fase 1 — Pesquisa de Referência Visual (moodboard)

- Busque (via ferramenta de pesquisa/imagem disponível) referências
  visuais reais de produtos/documentos do mesmo setor ou com o mesmo
  tom pretendido — não para copiar, para calibrar o que já é esperado
  e o que se destacaria.
- Cite as referências usadas. Se não for possível pesquisar no
  momento, sinalize isso e baseie as escolhas em princípios de design
  amplamente conhecidos, deixando claro que não foram checados contra
  referências reais.

### Fase 2 — Definição da Personalidade Visual

- Resuma o conceito em 2-4 adjetivos (ex.: "sóbrio, confiável,
  técnico" vs. "vibrante, acolhedor, humano") — cada decisão das fases
  seguintes deve remeter a esses adjetivos.
- Declare o tom emocional pretendido e por que ele serve ao propósito
  (Fase 0), não por preferência estética isolada.

### Fase 3 — Decisões de Direção de Arte

Simule papéis especializados, cada um ancorado na personalidade
definida na Fase 2:

1. **Colorista** — paleta com papel definido para cada cor (primária,
   secundária, neutra, destaque/CTA, estados de sucesso/erro/alerta),
   usando teoria da cor (esquema monocromático, análogo, complementar
   ou tríade) e a proporção 60-30-10 (dominante / secundária / destaque)
   como guia de equilíbrio.
2. **Tipógrafo** — par tipográfico (no máximo 2 famílias: uma de
   destaque/display, uma de texto corrido) e escala tipográfica modular
   (razões comuns: 1.25 "Major Third", 1.333 "Perfect Fourth", 1.618
   "Golden Ratio") para hierarquia consistente de tamanhos.
3. **Diretor de Imagem** — estilo de iconografia (line vs. filled),
   fotografia vs. ilustração vs. 3D, e o porquê de cada escolha remeter
   à personalidade da Fase 2.
4. **Coreógrafo de Movimento** (só para interfaces interativas) —
   princípios de easing (preferir `ease-in-out` a linear), duração
   (~150-300ms para micro-interações, até ~400ms para transições de
   tela) e onde a fluidez importa (o que deve parecer "leve" vs. o que
   deve ser instantâneo).

### Fase 4 — Reconciliação com Usabilidade

- Verifique cada decisão da Fase 3 contra os critérios de acessibilidade
  da `ui-ux-specialist`: contraste mínimo AA (4.5:1 texto normal, 3:1
  texto grande), legibilidade da tipografia em tamanhos pequenos,
  alternativa estática para quem usa `prefers-reduced-motion`.
- Se uma escolha estética não passar, ajuste a paleta/tipografia
  **dentro do mesmo conceito** (ex.: escurecer/clarear um tom mantendo
  o matiz) — não abandone o conceito por causa de um valor específico.

### Fase 5 — Persistência do Conceito e Handoff

Salve em `DESIGN_CONCEPT.md` (ou
`.agents/context/<nome-do-produto>-design-concept.md`):

- Propósito, público e personalidade visual (Fases 0-2).
- Paleta com códigos hex e papel de cada cor.
- Tipografia: famílias, pesos, escala tipográfica.
- Estilo de iconografia/imagem.
- Princípios de movimento (quando interativo).
- Referências usadas (Fase 1) e ajustes feitos por acessibilidade (Fase 4).

Ao final, declare que a `ui-ux-specialist` deve consumir este arquivo
na própria Fase 1 (Decisão de Abordagem) em vez de definir tokens do
zero.

### Fase 6 — Auditoria de Coerência

Durante a implementação (feita por outras skills), audite pontualmente:
nenhuma cor fora da paleta documentada, nenhuma fonte fora do par
definido, nenhum espaçamento fora da escala, nenhuma transição "seca"
onde o conceito pedia fluidez — e vice-versa, nenhum movimento
decorativo onde o conceito pedia sobriedade.

## Boas práticas obrigatórias (citar explicitamente quando relevante)

- **Teoria da cor** — roda cromática e esquemas (monocromático,
  análogo, complementar, tríade, split-complementar); proporção 60-30-10.
- **Escala tipográfica modular** — razões (1.125, 1.25, 1.333, 1.618)
  para hierarquia de tamanhos consistente, em vez de valores soltos.
- **Máximo de 2 famílias tipográficas** por sistema, com pesos
  variáveis cobrindo a hierarquia.
- **Grid e composição** — grid de 12 colunas (web/documento),
  alinhamento consistente; regra dos terços ou proporção áurea para
  composições estáticas (capas, banners, slides).
- **Espaço negativo (whitespace)** como elemento de elegância, não só
  de respiro funcional.
- **Motion design** — easing não linear, duração curta para
  micro-interações, respeito a `prefers-reduced-motion` (liga
  diretamente ao WCAG da `ui-ux-specialist`).
- **Consistência de marca** — se existir manual de marca, ele é a
  fonte de verdade; o conceito se adapta a ele, não o contrário.

## Ferramentas de validação a considerar

- Verificador de contraste (mesmo da `ui-ux-specialist`).
- Simulador de daltonismo (ex.: Coblis) para checar a paleta em
  diferentes tipos de percepção de cor.
- "Squint test" — embaçar a visualização (ou reduzir a tela) e
  verificar se a hierarquia visual ainda se sustenta sem depender do
  detalhe.

## Regras finais

- Nunca escolher cor/fonte que quebre contraste mínimo AA só por
  estética — resolver na Fase 4, dentro do mesmo conceito.
- Nunca usar mais de 2 famílias tipográficas ou introduzir cor fora da
  paleta documentada sem atualizar o `DESIGN_CONCEPT.md`.
- Nunca aplicar movimento decorativo sem alternativa estática para
  `prefers-reduced-motion`.
- Toda decisão estética deve remeter ao propósito e público definidos
  na Fase 0 — gosto pessoal isolado não é justificativa suficiente.
- Documentos estáticos (relatório, apresentação) seguem as mesmas
  fases, exceto a parte de movimento (Fase 3.4) — contraste e
  legibilidade continuam obrigatórios mesmo assim.
