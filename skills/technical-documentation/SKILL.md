---
name: technical-documentation
description: >-
  Gera ou atualiza a documentação técnica completa do projeto atual (README.md na raiz),
  cobrindo visão geral, arquitetura (com diagrama Mermaid), módulos com descrição a nível
  de função, instalação, execução, troubleshooting e histórico de alterações. Use esta
  skill sempre que o usuário pedir para gerar ou atualizar "documentação técnica", "tdoc",
  "tecdoc", "documentação do projeto" ou algo equivalente — mesmo abreviado, como "roda o
  tdoc", "gera a tecdoc desse projeto" ou "atualiza a tdoc". Trata geração e atualização
  como fluxos diferentes; geração escreve o documento do zero, atualização faz diff contra
  a versão existente e ajusta só o que mudou. Não confundir com pedidos de documentação de
  uma função/módulo isolado ou de comentários de código (docstrings) — esta skill é
  especificamente para o documento técnico completo do sistema salvo em README.md.
---

# tdoc — Gerador de Documentação Técnica

Esta skill gera ou atualiza o documento técnico oficial de um projeto, salvo como `README.md` na raiz do repositório, seguindo sempre a mesma estrutura fixa. O objetivo é que qualquer pessoa — dev novo no time ou stakeholder não-técnico — consiga entender o sistema lendo um único arquivo.

## Passo 1 — Determinar o modo: geração ou atualização

Antes de qualquer coisa, decida em qual dos dois fluxos você está. Isso muda o resto do processo, então não pule esta decisão:

- **Geração (do zero)**: o usuário pede para "gerar", "criar" a documentação, ou não existe `README.md` técnico ainda no projeto.
- **Atualização**: o usuário pede para "atualizar", "revisar" ou "sincronizar" a documentação, ou já existe um `README.md` no formato desta skill (reconhecível pelo cabeçalho `# Documentação Técnica - ...` e pelas seções fixas do template).

Se o pedido for ambíguo (ex.: só "roda o tdoc" e já existe um README no formato da skill), assuma **atualização** — reescrever do zero um documento que já existe e pode ter conteúdo escrito manualmente (troubleshooting reportado por humanos, trade-offs documentados em decisões passadas) descartaria informação que o código sozinho não recupera.

## Passo 2A — Fluxo de geração (do zero)

1. Se já existir um `README.md` na raiz (fora do formato desta skill, ex. um README genérico do projeto), renomeie para `readmeold.md` (`mv README.md readmeold.md`) antes de escrever o novo. Se `readmeold.md` já existir também, pergunte ao usuário se pode sobrescrever — não descarte histórico silenciosamente.
2. Prossiga para o Passo 3 (Investigar o projeto) e depois para o Passo 4, preenchendo **todas** as seções do template.

## Passo 2B — Fluxo de atualização

Atualizar não é regenerar. O objetivo é: manter o que ainda é verdade, corrigir o que mudou, e deixar rastro do que foi alterado.

1. Leia o `README.md` atual por completo antes de tocar em qualquer coisa.
2. Faça o levantamento do projeto (Passo 3) normalmente, e compare o que encontrou com o que está documentado:
   - **Stack**: dependências novas, removidas ou com versão relevante alterada.
   - **Arquitetura / Mermaid**: componentes, camadas ou integrações que apareceram, sumiram ou mudaram de relação desde a última versão do diagrama.
   - **Módulos e funções**: módulos novos, módulos removidos, funções/classes públicas que mudaram de assinatura ou responsabilidade.
   - **Instalação / Execução**: passos que já não funcionam mais (ex.: variável de ambiente renomeada, novo serviço no `docker-compose.yml`).
3. Aplique ajustes **apenas nas seções afetadas**. Não reescreva seções que continuam corretas — em especial, não descarte entradas de **Troubleshooting** que ainda são válidas, mesmo que não sejam coisas que o código revela sozinho (muitas vêm de incidentes reais reportados por humanos).
4. Adicione uma ou mais linhas novas na tabela **Alterações**, com a data de hoje, o(s) módulo(s) afetado(s) e um resumo do que mudou na documentação e por quê (ex.: "novo endpoint de sincronização adicionado ao módulo X").
5. Não renomeie nada para `readmeold.md` neste fluxo — a atualização edita o `README.md` existente diretamente.

## Passo 3 — Investigar o projeto

Não invente conteúdo genérico — cada seção deve refletir o projeto real. Isso vale tanto para geração quanto para atualização.

1. **Verifique se as skills `init` e `code-review` estão disponíveis** no ambiente atual. Se estiverem, use-as para mapear a estrutura do projeto e entender a qualidade/arquitetura do código antes de documentar. Se não estiverem disponíveis, siga com investigação manual normalmente (não bloqueie a geração/atualização por causa disso).
2. Leia arquivos de configuração e manifestos (`package.json`, `pyproject.toml`, `requirements.txt`, `docker-compose.yml`, `Dockerfile`, `.env.example`, `Cargo.toml`, `go.mod`, etc.) para identificar a stack real.
3. Explore a árvore de diretórios para identificar os módulos/domínios principais (ex.: pastas por feature, camadas DDD, apps Django, submódulos git) e como eles se conectam entre si (chamadas diretas, filas, API REST, eventos) — essa relação é o que vira o diagrama Mermaid no Passo 4.
4. Para cada módulo identificado, leia os arquivos de código e liste as funções, métodos de classe, endpoints ou comandos **públicos** (a interface que outros módulos ou usuários realmente usam) — não é necessário documentar toda função privada/auxiliar interna.
5. Se houver `CLAUDE.md`, arquivos em `.specify/`, ADRs, RFCs ou specs no repositório, leia-os — costumam conter decisões de arquitetura, trade-offs e justificativas que evitam retrabalho de investigação.
6. Confira o histórico do git (`git log --oneline -20`) para ter uma ideia de mudanças recentes relevantes para a seção "Alterações".

## Passo 4 — Preencher o template

Use **exatamente** esta estrutura, sem adicionar ou remover seções de nível 2/3. Se alguma informação não for descobrível, deixe a seção com uma nota objetiva (ex.: "Não identificado nos arquivos do projeto — preencher manualmente") em vez de inventar.

```markdown
# Documentação Técnica - [Nome do Projeto]

## Visão Geral

### Objetivo do sistema

### Stack

### Arquitetura do sistema

#### Diagrama

```mermaid
[diagrama aqui]
```

#### Conceitos utilizados
- Design Patterns
- Modelo de arquitetura

### Trade-offs

## Instalação do zero

## Execução atual

## Principais Módulos

### [Módulo 1]

[descrição do módulo]

#### Funções principais
- `nomeFuncao(parametros)` — o que ela faz, em uma linha.

### [Módulo 2]

[descrição do módulo]

#### Funções principais
- `nomeFuncao(parametros)` — o que ela faz, em uma linha.

## Troubleshooting
- Descrição do problema: O sintoma exato relatado e o impacto no sistema.
- Evidências e logs: Mensagens de erro, códigos de falha e horários.
- Causa raiz: O motivo real que gerou o erro.
- Solução aplicada: O passo a passo detalhado para corrigir a falha.

## Alterações

| Data | Módulo | Alteração | Motivo |
|------|--------|-----------|--------|
```

Orientações por seção:

- **Nome do Projeto**: use o nome real do repositório/projeto (nome da pasta raiz, campo `name` do manifesto, ou o nome mencionado no `CLAUDE.md`).
- **Objetivo do sistema**: 2-4 frases sobre o problema que o sistema resolve e para quem, não apenas "o que ele faz" tecnicamente.
- **Stack**: liste linguagens, frameworks, banco de dados, infra (Docker etc.) — com base no que foi de fato encontrado nos manifestos, não em suposições.
- **Arquitetura do sistema / Diagrama**: monte um diagrama Mermaid (`flowchart TD` para camadas/fluxo, ou `graph LR` para relação entre serviços/módulos, ou `sequenceDiagram` se o mais importante for um fluxo de chamadas) que represente os componentes reais e como eles se conectam — banco de dados, filas, serviços externos, frontend/backend, submódulos. Não use um diagrama genérico de "cliente → servidor → banco"; ele precisa refletir o que foi encontrado no Passo 3. Exemplo de ponto de partida:
  ```mermaid
  flowchart TD
      A[Frontend] -->|REST| B[Backend API]
      B --> C[(Banco de Dados)]
      B --> D[Serviço Externo X]
  ```
- **Conceitos utilizados**: liste os design patterns realmente identificados no código (repository, factory, CQRS, etc.), não uma lista genérica de patterns populares.
- **Trade-offs**: decisões conscientes que abriram mão de algo em troca de outra coisa (ex.: "otimizamos para leitura sacrificando latência de escrita"). Puxe isso de ADRs/specs se existirem.
- **Instalação do zero**: passo a passo reproduzível — clonar, instalar dependências, variáveis de ambiente necessárias, subir containers, rodar migrations. Deve funcionar para alguém que nunca tocou no projeto.
- **Execução atual**: como o sistema roda hoje (comandos de start, ambiente de produção/homologação, jobs agendados, portas, etc.) — diferente da instalação do zero, foca no dia a dia de quem já tem o ambiente configurado.
- **Principais Módulos**: um `###` por módulo/domínio real do sistema (renomeie `[Módulo 1]`, `[Módulo 2]` etc. para os nomes reais, adicionando quantos forem necessários), com uma descrição curta da responsabilidade de cada um.
- **Funções principais**: dentro de cada módulo, liste as funções/métodos/endpoints públicos com uma descrição de uma linha sobre o que fazem — não copie docstrings inteiras nem documente parâmetro por parâmetro; o objetivo é dar visibilidade da interface do módulo, não substituir a documentação inline do código. Se um módulo expõe muitas funções (dezenas), priorize as mais relevantes para quem for integrar com o módulo e agrupe o resto por categoria em vez de listar tudo.
- **Troubleshooting**: se o projeto tiver histórico de problemas conhecidos (issues, comentários no código, versão anterior do README), documente-os no formato de bullets pedido. Se não houver nenhum problema conhecido ainda, deixe a seção com o formato pronto e uma nota indicando que será preenchida conforme problemas forem surgindo — não invente incidentes fictícios.
- **Alterações**: preencha a tabela com o histórico real de mudanças relevantes (do git log, da versão anterior do documento, ou de specs/ADRs). Na primeira geração, inclua uma linha inicial registrando a criação do documento; nas atualizações, sempre adicione uma linha nova em vez de editar as antigas.

## Passo 5 — Salvar e confirmar

Escreva o resultado em `README.md` na raiz do projeto. Ao final, informe rapidamente ao usuário:

- **Se foi geração**: que o `README.md` anterior (se existia) foi preservado como `readmeold.md`, e quais seções ficaram com lacunas por falta de informação disponível.
- **Se foi atualização**: quais seções foram efetivamente alteradas e por quê (ligando com a linha nova adicionada em Alterações), e quais foram mantidas como estavam.
