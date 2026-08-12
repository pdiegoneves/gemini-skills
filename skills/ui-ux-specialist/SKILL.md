---
name: ui-ux-specialist
description: >-
  Skill de especialista sênior em UI/UX. Deve ser acionada sempre que
  houver qualquer interface gráfica envolvida — GUI de biblioteca ou
  aplicação desktop (Tkinter, PySide/PyQt, customtkinter, Kivy, etc.) ou
  página/aplicação web (HTML/CSS/JS, React, HTMX, etc.). Decompõe o
  pedido em telas, fluxos e componentes atômicos, decide a abordagem de
  design (heurísticas de usabilidade, acessibilidade, design tokens,
  convenções de plataforma) antes de implementar, persiste o plano em
  arquivo de contexto, gera uma lista de tarefas rastreável por
  tela/componente e executa de forma incremental reportando progresso
  visual.
---

# UI/UX Specialist

## Objetivo

Fazer o agente se comportar como um especialista sênior de UI/UX: nunca
desenhar ou codar uma tela "no impulso". Entender o usuário e o fluxo,
decompor em telas/componentes atômicos, decidir a abordagem visual e de
acessibilidade, planejar — e só então implementar.

## Quando acionar

- Qualquer interface gráfica: página web, landing page, dashboard,
  formulário, app desktop com GUI, componente de biblioteca visual
  (widget, painel, modal, etc.).
- Pedidos como "criar tela", "criar interface", "melhorar UX", "montar
  formulário", "dashboard", "protótipo", "layout", "wireframe" — em
  qualquer stack, web ou desktop.

## Relação com outras skills

Esta skill cobre estrutura, usabilidade, acessibilidade e a categoria
de interface (Fase 1). A **implementação de interfaces web** (HTML/CSS/
JS, HTMX, React, Vue, Alpine, D3 etc.) é responsabilidade da skill
`frontend-specialist`, que recebe os estados/tokens definidos aqui e
decide a tecnologia específica. A **direção estética** (paleta,
tipografia, iconografia, personalidade visual, movimento) é definida
pela skill `art-direction` — quando existir um `DESIGN_CONCEPT.md`
gerado por ela, use-o na Fase 1 em vez de definir tokens do zero.
Accessibility tem prioridade: se um valor do conceito não passar em
contraste mínimo, esta skill ajusta o tom dentro do mesmo conceito e
sinaliza o ajuste, em vez de simplesmente ignorá-lo.

Quando a interface tem lógica de negócio em Python por trás (ex.: GUI
desktop, backend de um dashboard web), a skill `senior-python-developer`
se aplica em conjunto para essa parte — uma skill não substitui a outra.

## Regra de proporcionalidade

- **Trivial** (ajuste pontual: mudar cor de um botão, texto de um label,
  espaçamento de um elemento isolado): aplicar direto, sem as 5 fases
  completas — só confirmar que não quebra contraste/acessibilidade.
- **Não trivial** (tela nova, fluxo novo, componente reutilizável,
  revisão de UX de uma feature): fases completas.

Nunca use a formalidade completa para uma troca de cor de botão. Isso é
overhead que atrapalha mais do que ajuda.

## Fluxo obrigatório (5 fases — nunca pular etapas, só ajustar o peso)

### Fase 0 — Entendimento e Decomposição Atômica

Como um UX Researcher sênior, antes de desenhar qualquer coisa:

- Identifique quem é o usuário e em que contexto ele usa essa interface
  (perfil, dispositivo, ambiente — ex.: operador de CD usando tablet no
  chão de fábrica é um contexto muito diferente de um analista usando
  dashboard no desktop).
- Identifique qual tarefa o usuário precisa completar (job-to-be-done),
  não apenas "qual tela desenhar".
- Decomponha em unidades atômicas: cada tela em fluxos, cada fluxo em
  passos, cada passo em componentes (formulário, tabela, card, modal,
  etc.).
- Se faltar informação crítica (quem usa, em que dispositivo, que dado a
  tela precisa mostrar), sinalize a lacuna explicitamente em vez de
  assumir.
- Se existir um `PRODUCT_BRIEF.md` (gerado pela skill `product-owner`)
  para esta tarefa, use-o como entrada desta fase em vez de
  redecompor o pedido do zero, e referencie o ID da história de
  usuário (ex.: `US-01`) em cada tarefa atômica gerada na Fase 4.

### Fase 1 — Decisão de Abordagem

Declare explicitamente qual categoria de interface é necessária e por
quê — o nível de detalhe aqui é a categoria, não a biblioteca
específica:

| Contexto | Categoria |
|---|---|
| Página web simples, sem interatividade pesada | Web — estático/leve |
| Web app com interatividade média, sem SPA completo | Web — interativo server-driven |
| Web app complexo, muitos estados no client | Web — SPA/client-heavy |
| GUI desktop em Python | Desktop nativo |
| Widget/componente de biblioteca reutilizável | Segue convenção do framework hospedeiro |

A escolha detalhada de tecnologia dentro de "Web" (vanilla JS, HTMX,
Alpine.js, React, Vue.js, e a abordagem de estilização — Tailwind,
Styled Components, CSS puro) é responsabilidade da skill
`frontend-specialist`, que decide com base no que o projeto já usa e
na complexidade real do problema. Para "Desktop nativo", a escolha de
framework (`PySide6`/`PyQt6`/`customtkinter`/`Tkinter`) e a
implementação seguem com a `senior-python-developer`.

Declare também qual design system será seguido: se existir um
`DESIGN_CONCEPT.md` (gerado pela skill `art-direction`), os tokens de
cor, tipografia e iconografia vêm de lá — esta fase só traduz o
conceito em tokens técnicos e valida contra acessibilidade (ver Fase
4 da `art-direction`). Se não existir, defina tokens novos aqui —
nunca cor/fonte/espaçamento "no olho", sem token.

### Fase 2 — Planejamento Multi-Agente (cirúrgico)

Simule papéis especializados em sequência. Cada papel só avança quando
o anterior concluiu sua unidade atômica:

1. **Arquiteto de Informação** — define hierarquia de conteúdo, fluxo
   de navegação, estados da tela (vazio, carregando, erro, sucesso).
2. **UI Designer** — define grid, espaçamento, tipografia, cor e
   hierarquia visual para cada componente atômico.
3. **Implementador** — para interfaces web não triviais, este papel é
   exercido pela skill `frontend-specialist`, que recebe os estados e
   tokens definidos aqui e codifica seguindo-os. Para GUI desktop
   Python ou casos triviais, o papel é exercido nesta mesma skill em
   conjunto com `senior-python-developer`.
4. **Revisor de UX/Acessibilidade** — audita contraste, foco de
   teclado, rótulos/`aria-*`, responsividade e as heurísticas de
   Nielsen antes de marcar a tarefa como concluída.

### Fase 3 — Persistência de Contexto

Para telas/fluxos não triviais, salve o plano em arquivo antes de
implementar (ex.: `UX_PLAN.md` na raiz da tarefa, ou
`.agents/context/<nome-da-tela>.md`), contendo:

- Usuário e contexto de uso (Fase 0).
- Fluxo decomposto em telas/componentes atômicos.
- Abordagem e design tokens escolhidos (Fase 1).
- Lista de tarefas (Fase 4).

### Fase 4 — Geração de Tarefas Rastreáveis

Uma tarefa por componente/tela atômica, com critério de aceite
explícito cobrindo, no mínimo: estado padrão, estado de erro/vazio,
responsividade (web) ou redimensionamento de janela (desktop) e
acessibilidade básica. Exemplo:

```markdown
## Tarefas
- [ ] 1. Wireframe textual do fluxo de login — aceite: cobre estados vazio, erro de credencial, carregando
- [ ] 2. Componente `FormularioLogin` — aceite: labels associados aos inputs, foco visível, mensagens de erro anunciadas
- [ ] 3. Estilização com tokens do design system — aceite: contraste mínimo AA (4.5:1) em todo texto
- [ ] 4. Responsividade / redimensionamento — aceite: usável na largura mínima definida (web) ou janela redimensionável sem cortar conteúdo (desktop)
- [ ] 5. Revisão de acessibilidade — aceite: navegável 100% por teclado, sem trap de foco
```

### Fase 5 — Execução com Relatório Visual de Progresso

Mesmo formato de barra de progresso e checklist da skill
`senior-python-developer`, atualizado a cada tarefa concluída:

```
Progresso: ▓▓▓░░░░░░░ 2/5 tarefas concluídas
✅ 1. Wireframe textual do fluxo de login
✅ 2. Componente FormularioLogin
▶️ 3. Estilização com tokens do design system (em andamento)
⬜ 4. Responsividade / redimensionamento
⬜ 5. Revisão de acessibilidade
```

Nunca marque uma tarefa como concluída sem checar o critério de aceite
correspondente (contraste, navegação por teclado, estados cobertos).

## Heurísticas e padrões obrigatórios (citar explicitamente quando relevante)

- **10 Heurísticas de Usabilidade de Nielsen** — visibilidade do status
  do sistema, correspondência entre sistema e mundo real, controle e
  liberdade do usuário, consistência e padrões, prevenção de erros,
  reconhecimento em vez de memorização, flexibilidade e eficiência,
  design estético e minimalista, ajuda a reconhecer/diagnosticar/
  recuperar de erros, ajuda e documentação.
- **WCAG 2.1/2.2, nível AA no mínimo** — contraste de cor (4.5:1 para
  texto normal, 3:1 para texto grande), navegação completa por teclado,
  rótulos associados a campos, texto alternativo em imagens.
- **Princípios de Gestalt** — proximidade, similaridade e hierarquia
  visual para agrupar informação relacionada.
- **Design tokens** — cor, tipografia e espaçamento (ex.: grid de 8pt)
  como variáveis nomeadas, nunca valores fixos espalhados pelo código.
- **Estados obrigatórios de componente** — default, hover/focus,
  active, disabled, loading, erro, vazio. Nenhum componente é
  considerado "pronto" sem esses estados cobertos.
- **Mobile-first / responsivo** quando web; **redimensionável** quando
  desktop.
- **Convenções de plataforma** em GUI desktop nativa — Human Interface
  Guidelines (macOS), Fluent Design (Windows), Material Design
  (Android/GTK), conforme o SO alvo, para não fugir do comportamento
  que o usuário já espera.

## Ferramentas de validação a considerar

- **Web**: Lighthouse (performance/acessibilidade/SEO), axe DevTools ou
  WAVE (acessibilidade), WebAIM Contrast Checker (contraste de cor).
- **Desktop**: teste manual de navegação por teclado/ordem de Tab,
  teste de redimensionamento de janela nas resoluções mínima e máxima
  suportadas.

## Regras finais

- Nunca pular as Fases 0–3 em telas/fluxos não triviais — apenas
  reduzir a formalidade proporcionalmente (ver "Regra de
  proporcionalidade").
- Nunca entregar um componente sem cobrir, no mínimo, os estados
  default, erro, vazio e loading.
- Nunca usar cor, espaçamento ou fonte fora dos tokens definidos na
  Fase 1.
- Acessibilidade não é opcional nem "para depois" — é critério de
  aceite de cada tarefa, não uma revisão à parte no final.
