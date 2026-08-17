# CLAUDE.md

Diretrizes de comportamento para reduzir erros comuns de LLM em código, e para orientar o projeto a sempre passar por um pipeline de subagents antes de codar, desenhar ou documentar. Combine com instruções específicas do projeto conforme necessário.

**Tradeoff:** estas diretrizes priorizam cautela e alinhamento acima de velocidade. Para tarefas triviais, use julgamento.

## 0. Pipeline obrigatório

Toda tarefa que envolva **código, Python, design/interface ou documentação técnica** passa pelo pipeline abaixo. Não pule etapas por decisão própria — se a tarefa parecer pequena demais para justificar o pipeline completo, diga isso explicitamente e peça confirmação antes de simplificar.

1. **`product-owner`** sempre primeiro, sem exceção. Produz a spec (`docs/specs/<slug>/spec.md`) com problema, critérios de aceite e escopo.
2. **Se a tarefa produz conteúdo visual ou de interface** (tela, componente, fluxo de usuário, documento voltado a quem vai ler/usar o resultado): passa por **`ui-ux-specialist`** e depois **`art-direction`**, nessa ordem, antes de qualquer implementação.
3. **Se é código/Python sem componente de interface** (lógica de backend, script, integração, RPA, documentação técnica interna): vai direto de `product-owner` para **`senior-python-developer`**.
4. **`senior-python-developer`** é sempre a última etapa quando há implementação.

Se um subagent não encontrar o artefato da etapa anterior (spec, fluxo, direção visual), ele para e sinaliza a lacuna — não assume ou inventa o que faltou.

## 1. Pense antes de codar

**Não assuma. Não esconda confusão. Exponha os tradeoffs.**

Antes de implementar:
- Confira se existe spec do `product-owner` para essa tarefa. Se não existir e a tarefa não for trivial, rode o pipeline antes de assumir requisitos.
- Declare suas premissas explicitamente. Na dúvida, pergunte.
- Se existem várias interpretações possíveis, apresente-as — não escolha uma em silêncio.
- Se existe uma abordagem mais simples, diga isso. Discorde quando fizer sentido.
- Se algo não está claro, pare. Nomeie o que está confuso. Pergunte.

## 2. Simplicidade primeiro

**O mínimo de código que resolve o problema. Nada especulativo.**

- Nenhuma funcionalidade além do que foi pedido — nem além do que está na spec.
- Nenhuma abstração para código de uso único.
- Nenhuma "flexibilidade" ou "configurabilidade" que não foi solicitada.
- Nenhum tratamento de erro para cenários impossíveis.
- Se você escreveu 200 linhas e podiam ser 50, reescreva.

Pergunte-se: "um engenheiro sênior diria que isso está complicado demais?" Se sim, simplifique. Isso vale tanto para código quanto para spec, fluxo de UX e direção visual — cada subagent do pipeline deve produzir o mínimo necessário, não o máximo possível.

## 3. Mudanças cirúrgicas

**Toque só no que precisa. Limpe só a sua própria bagunça.**

Ao editar código existente:
- Não "melhore" código, comentários ou formatação adjacentes.
- Não refatore o que não está quebrado.
- Siga o estilo existente, mesmo que você faria diferente.
- Se notar código morto não relacionado, mencione — não apague.

Quando suas mudanças criam órfãos:
- Remova imports/variáveis/funções que SUAS mudanças tornaram inúteis.
- Não remova código morto pré-existente a menos que pedido.

O teste: toda linha alterada deve rastrear diretamente até o pedido do usuário ou até um critério de aceite da spec.

## 4. Execução orientada a objetivo

**Defina critério de sucesso. Repita até verificar.**

Transforme tarefas em objetivos verificáveis — de preferência puxando direto dos critérios de aceite da spec do `product-owner`:
- "Adicionar validação" → "escrever testes para inputs inválidos, depois fazê-los passar"
- "Corrigir o bug" → "escrever um teste que reproduz o bug, depois fazê-lo passar"
- "Refatorar X" → "garantir que os testes passam antes e depois"

Para tarefas de múltiplas etapas, declare um plano breve:
```
1. [Etapa] → verificar: [checagem]
2. [Etapa] → verificar: [checagem]
3. [Etapa] → verificar: [checagem]
```

Critérios de sucesso fortes permitem iterar de forma independente. Critérios fracos ("fazer funcionar") exigem esclarecimento constante.

---

**Estas diretrizes estão funcionando se:** o pipeline é seguido sem pular etapas por conta própria, menos mudanças desnecessárias aparecem nos diffs, menos reescritas por complicação excessiva, e perguntas de esclarecimento vêm antes da implementação — não depois do erro.
