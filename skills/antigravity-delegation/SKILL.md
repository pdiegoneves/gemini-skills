---
name: antigravity-delegation
description: >-
  Autoriza e instrui o agente a delegar tarefas de implementação
  pontuais e bem definidas ao Antigravity CLI (`agy`), em modo
  headless, quando isso acelera o trabalho sem sacrificar qualidade.
  Deve ser consultada sempre que já existir uma unidade de trabalho
  atômica, com escopo de arquivos e critério de aceite claros (ex.:
  gerada pelas skills `senior-python-developer`, `frontend-specialist`
  ou `web-security-django`), antes de decidir se a implementação será
  feita diretamente ou delegada. Cobre quando delegar, como escrever o
  prompt de delegação, qual modelo/esforço escolher por tipo de
  tarefa, quando paralelizar com múltiplos subagentes headless, e como
  julgar e validar o resultado antes de aceitar — assumindo a tarefa
  diretamente se a saída não atender ao padrão de qualidade.
---

# Antigravity Delegation

## Onde esta skill mora

Ao contrário das skills `senior-python-developer`, `ui-ux-specialist`,
`art-direction`, `product-owner` e `web-security-django` — que ensinam
o **Antigravity CLI** a se comportar e vivem em `.agents/skills/` —
esta skill ensina **o agente orquestrador** (ex.: Claude Code) a usar
o Antigravity CLI como ferramenta externa. Ela deve ficar onde o
agente orquestrador descobre as próprias skills, não em
`.agents/skills/` do projeto.

## Objetivo

Autorizar o agente a invocar `agy` (Antigravity CLI) via terminal para
tarefas pontuais de implementação já bem definidas, mantendo
responsabilidade total pela qualidade do resultado — o agente julga,
corrige ou refaz se necessário, exatamente como faria se tivesse
implementado sozinho. Delegar não é terceirizar a responsabilidade,
é terceirizar a digitação.

## Quando acionar / quando NÃO acionar

**Pré-requisitos para delegar (todos precisam valer):**
- A tarefa já foi decomposta em unidade atômica, com escopo de
  arquivos definido (ex.: por `senior-python-developer` ou
  `frontend-specialist`).
- Existe critério de aceite objetivo e verificável (teste, lint,
  build, ou comportamento observável).
- Existe mecanismo de verificação local (comando de teste/lint/build)
  que pode ser executado após a delegação — sem isso, não há como
  julgar o resultado, só confiar cegamente.

**NÃO delega:**
- Decisões de arquitetura, escopo de produto, identidade visual ou
  segurança crítica — isso é papel das skills de planejamento
  (`product-owner`, `art-direction`, `ui-ux-specialist`,
  `web-security-django`), não de implementação.
- Tarefa sem critério de aceite objetivo — delegar "sem saber o que é
  sucesso" é abrir mão de julgamento, não acelerar trabalho.
- Tarefa trivial onde orquestrar a delegação (escrever prompt, disparar,
  aguardar, validar) leva mais tempo do que implementar direto.

## Relação com outras skills

Esta skill não decide **o quê** implementar — isso já vem pronto das
skills de planejamento e implementação. Ela decide **quem digita**: o
próprio agente ou um subagente do Antigravity CLI. As tarefas
rastreáveis geradas por `senior-python-developer`, `frontend-specialist`
e `web-security-django` são a unidade natural de delegação — uma
tarefa da lista, um `agy -p`.

## Fluxo obrigatório (7 fases)

### Fase 0 — Verificar pré-requisitos de delegação

Confirme os três pré-requisitos acima. Se algum faltar, não delegue —
ou implemente diretamente, ou volte para a skill de planejamento
correspondente para fechar a lacuna primeiro.

### Fase 1 — Preparar o prompt de delegação

Um prompt de delegação bem-feito é a principal prática oficial
("Explore, plan, then execute" e "Enrich your prompting context" —
docs do Antigravity CLI). Inclua sempre:

- **Escopo exato de arquivos** — caminhos explícitos, não "o projeto
  todo". Em uso interativo isso é feito com `@arquivo`; em headless,
  cite o caminho completo diretamente no texto do prompt.
- **Contexto mínimo necessário** — trecho relevante da especificação
  (ex.: a história de usuário/critério de aceite gerado pelo
  `product-owner`), não o brief inteiro.
- **Critério de aceite explícito**, copiado literalmente da tarefa.
- **Instrução para autoverificação**: peça para o próprio `agy` rodar
  o comando de teste/lint/build ao final e reportar o resultado —
  prática documentada oficialmente como "Establish verification loops".

### Fase 2 — Selecionar modelo e esforço

Liste o que está disponível antes de fixar algo — nomes de modelo e
agentes mudam com o tempo:

```bash
agy models
agy agents
```

Heurística inicial por tipo de tarefa (ponto de partida, não regra
fixa — calibre com a experiência real, ver nota de confiabilidade no
fim do arquivo):

| Tipo de tarefa | Modelo | Effort |
|---|---|---|
| Tarefa mecânica, um arquivo, bem especificada (ex.: escrever um teste unitário simples, aplicar um rename, gerar boilerplate) | `gemini-3.6-flash-medium` | `low`/`medium` |
| Múltiplos arquivos, lógica não trivial, mas já bem escopada por uma skill de planejamento | `gemini-3.1-pro-high` ou `claude-sonnet-4-6` | `medium`/`high` |
| Refactor sensível, revisão de segurança, ou qualquer tarefa em que a qualidade do raciocínio importa mais que velocidade | `claude-opus-4-6` | `high` |
| Pesquisa/exploração de código, sumarização, sem escrita de arquivo | `gemini-3.5-flash-medium` | `medium` |

### Fase 3 — Decidir paralelização

Paraleliza quando as tarefas são **independentes** entre si (arquivos
diferentes, sem dependência de ordem). Não paraleliza quando há
dependência sequencial (tarefa B precisa do resultado de A) ou quando
as tarefas tocam o mesmo arquivo — nesse caso o risco de conflito
supera o ganho de velocidade.

Mantenha o número de subagentes concorrentes moderado (referência de
mercado: por volta de 3 a 5 simultâneos nos planos pagos — a quota é
compartilhada entre app desktop, CLI e SDK, e uma única tarefa mal
escopada pode disparar dezenas de chamadas de modelo aninhadas sem
avisar). Se disponível, cheque o consumo antes de rodadas grandes.

### Fase 4 — Disparar em modo headless

Sempre `-p`/`--print` (nunca interativo — o agente está automatizando,
não conversando) e sempre `--output-format json`, para obter um
envelope parseável (`status`, `response`, `usage`) em vez de tentar
interpretar texto livre:

```bash
agy -p "$(cat <<'EOF'
Implemente a tarefa: <ID da tarefa, ex. US-02/Tarefa-3>.
Escopo: apenas os arquivos <caminho1>, <caminho2>.
Critério de aceite:
<colar o critério de aceite literal da tarefa>
Ao terminar, rode `<comando de verificação, ex. uv run pytest caminho/test.py>`
e reporte o resultado no final da resposta.
EOF
)" \
  --model gemini-3.1-pro-high \
  --effort high \
  --output-format json \
  --print-timeout 10m \
  --dangerously-skip-permissions
```

Paralelo (tarefas independentes, mesmo lote):

```bash
for tarefa in tarefa_a tarefa_b tarefa_c; do
  agy -p "$(cat "prompts/${tarefa}.txt")" \
    --model gemini-3.6-flash-medium \
    --output-format json \
    --dangerously-skip-permissions \
    > "resultados/${tarefa}.json" &
done
wait
```

**Sobre `--dangerously-skip-permissions`**: em modo headless não há
prompt interativo, então uma ferramenta que normalmente pediria
confirmação (ex.: rodar comando de shell) é *soft-denied* por padrão —
a execução segue, mas aquele passo específico é pulado e um aviso vai
para `stderr`. Isso destrava a execução sem supervisão, mas aprova
**tudo**, incluindo escrita de arquivo e execução de comando. Use
apenas dentro de um ambiente já isolado/confiável (sandbox, branch
descartável, container). Quando possível, prefira regras granulares em
`~/.gemini/antigravity-cli/settings.json` (`permissions.allow`, ex.:
`"command(git)"`, `"write_file(src/)"`) em vez do flag geral.

### Fase 5 — Julgar o Resultado (nunca aceitar por confiança)

Nunca aceite só porque a chamada retornou. Verifique, nessa ordem:

1. **Status do envelope** (`jq -r '.status'`): só `SUCCESS` segue
   adiante; `ERROR`/`CANCELED`/`INTERRUPTED`/`INVALID`/`WAITING` vão
   direto para a Fase 6.
2. **Verificação objetiva independente**: rode você mesmo o comando de
   teste/lint/build declarado no critério de aceite, mesmo que o `agy`
   já tenha relatado tê-lo rodado — o relato dele é evidência, não
   prova.
3. **Blast radius**: confira que só os arquivos do escopo declarado
   foram tocados (`git diff --stat` ou `git status`). Mudança fora do
   escopo é motivo de rejeição mesmo que os testes passem.
4. **Leitura do diff**: leia a mudança como leria uma PR de um colega
   — o critério de aceite passar não dispensa isso.

### Fase 6 — Agir corretivamente

- **Falha pontual clara** (erro de sintaxe, mal-entendido pequeno):
  refine o prompt (mais contexto, escopo mais explícito) e tente
  novamente — considere subir o `--effort` ou trocar de modelo.
- **Segunda falha na mesma tarefa, ou resultado fora de escopo**: pare
  de insistir em delegar. Implemente diretamente. Delegação existe
  para ganhar velocidade, não para virar um loop de tentativa e erro
  mais lento que fazer à mão.

## Boas práticas obrigatórias (documentação oficial do Antigravity CLI)

- **Loop de verificação sempre presente** — nunca delegar uma
  implementação sem um jeito objetivo de checar se ela funcionou.
- **`-p`/`--print` para toda automação** — modo interativo não se
  automatiza.
- **`--output-format json`** para parse confiável; `stream-json` só
  quando for necessário observar passos/ferramentas em tempo real.
- **Autenticação prévia**: modo headless usa credenciais em cache — é
  preciso autenticar uma vez de forma interativa antes de rodar em
  script/CI, senão a chamada falha com erro de autenticação em vez de
  travar esperando.
- **`--print-timeout` ajustado à tarefa** — o padrão é 5 minutos; tarefas
  maiores precisam de um teto maior, declarado explicitamente.
- **Nunca fixar `--model` com um nome não verificado** — headless falha
  alto (`ERROR`, exit não-zero) se o slug não existir, o que é bom
  (falha visível), mas confirme com `agy models` antes de fixar um
  pipeline.
- **Regra de arquivo de contexto do projeto**: se o projeto já tem
  (ou pode ganhar) um `GEMINI.md`/`AGENTS.md` na raiz descrevendo
  padrões, comandos de teste e convenções, o Antigravity CLI lê esse
  arquivo automaticamente — mantê-lo atualizado reduz a necessidade de
  reexplicar contexto em todo prompt de delegação.

## Regras finais

- Delegação é de **implementação**, nunca de **decisão** — arquitetura,
  escopo, segurança e identidade visual continuam sendo do agente e das
  skills de planejamento.
- Toda saída delegada passa pela Fase 5 antes de ser aceita — status
  `SUCCESS` sozinho não é critério de aceite.
- Duas falhas na mesma tarefa: pare de delegar, implemente direto.
- `--dangerously-skip-permissions` só em ambiente já confiável/isolado.
- Nunca delegar algo fora do escopo definido pelas skills de
  planejamento já existentes — a delegação executa um plano, não cria um.

## Nota de confiabilidade

A sintaxe de comandos, flags e o formato do envelope JSON acima vêm da
documentação oficial (`antigravity.google/docs/cli/*`), consultada
nesta pesquisa. A tabela de modelo/esforço por tipo de tarefa é uma
heurística inicial baseada na hierarquia de capacidade documentada
(flash = mais rápido/leve, pro/opus = mais raciocínio), **não** um
benchmark que eu rodei nas suas tarefas reais — trate como ponto de
partida e recalibre com a experiência. A recomendação de manter
paralelismo entre 3 e 5 subagentes vem de uma análise de terceiros que
afirma tê-la cruzado com a documentação oficial, não de uma página
oficial que eu tenha verificado citando esse número diretamente — se
isso for crítico para o seu uso, vale confirmar com `/usage` no
momento do uso real. O Antigravity CLI é um produto novo e iterando
rápido; comandos e nomes de modelo podem mudar — `agy models`, `agy
agents` e `agy --help` são a fonte de verdade no momento da execução,
não este arquivo.