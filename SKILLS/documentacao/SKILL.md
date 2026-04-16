---
name: documentacao
description: "Use sempre que o for documentar um software."
category: documentations
risk: unknown
source: my
date_added: "2026-04-10"
---
skill:
  metadata:
    name: documentacao
    alias: documentador
    description: "Use sempre que for documentar um software."
    category: documentations
    risk: unknown
    source: my
    date_added: "2026-04-10"

  purpose: "Automatizar a leitura de todo o código-fonte na pasta de trabalho para gerar uma documentação em markdown no 'README.md', baseando-se estritamente em um template."

  resources:
    inputs:
      - "Código-fonte no diretório de trabalho local."
    templates:
      - "templates/readme_model.md"
    outputs:
      - "doc_plan.md"
      - "README.md"

  constraints:
    - "NON_GOAL_INVENTION: Nunca invente regras de negócio ou funcionalidades que não foram explicitamente encontradas no código-fonte lido."
    - "TEMPLATE_STRICTNESS: O README gerado deve refletir exatamente as seções contidas em 'templates/readme_model.md'."

  workflow:
    step_1_discovery:
      name: "Descoberta e Estruturação"
      actions:
        - "Listar todos os módulos e arquivos disponíveis na pasta atual."
        - "Ler o conteúdo dos arquivos para mapear a estrutura do projeto."
        - "Definir um ponto de partida lógico e a sequência de documentação."
    
    step_2_planning:
      name: "Criação do Plano de Ação"
      actions:
        - "Gerar o arquivo 'doc_plan.md' físico no disco."
        - "Estruturar o plano como um checklist de tarefas atômicas e iterativas."
      syntax_rules:
        pending: "- [ ] Tarefa pendente"
        in_progress: "- [/] Tarefa em andamento"
        completed: "- [X] Tarefa concluída"

    step_3_approval:
      name: "Confirmação do Usuário (OBRIGATÓRIO)"
      actions:
        - "Após salvar 'doc_plan.md', PAUSE a execução."
        - "Apresente o plano e solicite a confirmação do usuário."
        - "BLOCKER: Não inicie a escrita do README.md sem receber o 'ok' do usuário."

    step_4_implementation:
      name: "Implementação Passo a Passo"
      actions:
        - "Ao receber aprovação, escreva o 'README.md' iterativamente, seção por seção do template."
        - "Após finalizar cada etapa, atualize o 'doc_plan.md' e o prompt com a tarefa concluída."
      timestamp_requirement:
        format: "YYYY-MM-DD HH:MM:SS"
        example: "- [X] Ler arquivo X e documentar Regras de Negócio -> 2026-04-10 10:50:00"
      output_behavior: "Mostre o progresso ao usuário a cada iteração, mantendo transparência do processo."