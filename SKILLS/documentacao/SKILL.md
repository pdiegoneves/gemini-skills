---
name: documentacao
description: "Use sempre que for criar o README.md de um software, baseando-se no design técnico (TDDOC)."
category: documentations
risk: unknown
source: pdseven
date_added: "2026-04-10"
---
skill:
  metadata:
    name: documentacao
    alias: documentador
    description: "Use sempre que for criar o README.md de um software, baseando-se no design técnico (TDDOC)."
    category: documentations
    risk: unknown
    source: my
    date_added: "2026-04-10"

  purpose: "Automatizar a geração de documentação em markdown no 'README.md', utilizando o Documento de Design Técnico (TDDOC) como base de conhecimento estruturada, seguindo estritamente um template predefinido."

  resources:
    inputs:
      - "Documento de Design Técnico (TDDOC) no diretório local."
    templates:
      - "templates/readme_model.md"
    outputs:
      - "doc_plan.md"
      - "README.md"

  constraints:
    - "NON_GOAL_INVENTION: Nunca invente regras de negócio ou funcionalidades que não foram explicitamente encontradas no TDDOC."
    - "TEMPLATE_STRICTNESS: O README gerado deve refletir exatamente as seções contidas em 'templates/readme_model.md'."
    - "DEPENDENCY_FIRST: O README.md só pode ser gerado a partir de um TDDOC válido."

  workflow:
    step_1_discovery_and_dependency:
      name: "Verificação de Dependência e Descoberta"
      actions:
        - "Verificar na pasta atual se existe um Documento de Design Técnico (TDDOC)."
        - "Se o TDDOC NÃO existir, suspenda o processo de README e invoque a skill 'technical-design-doc-creator' para criar a documentação técnica completa primeiro."
        - "Após garantir a existência do TDDOC, ler o seu conteúdo para extrair o contexto, arquitetura, decisões técnicas e plano de implementação."
        - "Definir a correspondência entre as informações do TDDOC e as seções exigidas pelo template de README."
    
    step_2_planning:
      name: "Criação do Plano de Ação"
      actions:
        - "Gerar o arquivo 'doc_plan.md' físico no disco."
        - "Estruturar o plano como um checklist de tarefas atômicas e iterativas para a transposição de dados do TDDOC para o README.md."
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
        - "Ao receber aprovação, escreva o 'README.md' iterativamente, preenchendo as seções do template exclusivamente com as informações obtidas no TDDOC."
        - "Após finalizar cada etapa, atualize o 'doc_plan.md' e o prompt com a tarefa concluída."
      timestamp_requirement:
        format: "YYYY-MM-DD HH:MM:SS"
        example: "- [X] Ler TDDOC e documentar Arquitetura no README -> 2026-04-10 10:50:00"
      output_behavior: "Mostre o progresso ao usuário a cada iteração, mantendo transparência do processo."