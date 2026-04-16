skill:
  metadata:
    name: universal-planner
    description: "Use sempre que precisar realizar qualquer tarefa relacionada a código."
    category: planning
    risk: unknown
    source: my
    date_added: "2026-04-08"

  purpose: "Forçar um protocolo de planejamento padronizado e obrigatório para TODA solicitação envolvendo modificações de código ou novas implementações. Garante integridade técnica exigindo contexto profundo e quebra estruturada de tarefas antes de qualquer modificação de arquivo."

  trigger_conditions:
    mandatory_usage: "ESTA SKILL É OBRIGATÓRIA E SEU WORKFLOW DEVE SER SEGUIDO SE A SOLICITAÇÃO ENVOLVER:"
    scenarios:
      - "Implementação de novas features (funcionalidades)."
      - "Correção de bugs ou resolução de erros."
      - "Refatoração de código existente."
      - "Modificação de arquivos de configuração."
      - "Escrita ou atualização de testes."

  constraints:
    - "NEVER_SKIP_PLANNING: A fase de planejamento não pode ser ignorada sob nenhuma hipótese."
    - "NO_MODIFICATIONS_BEFORE_STEP_4: É terminantemente proibido modificar qualquer arquivo no disco antes de chegar à fase de Execução Atômica."
    - "TASK_SIZE: As tarefas devem ser granulares o suficiente para serem concluídas em 1 a 2 turnos de interação."
    - "STATE_TRACKING_REQUIRED: O status do checklist de tarefas deve ser atualizado e impresso em TODAS as mensagens durante a fase de Execução."

  workflow:
    step_1_context:
      name: "Context Understanding (Entendimento)"
      actions:
        - "Analisar a base de código existente relacionada à solicitação."
        - "Identificar dependências, módulos afetados e possíveis efeitos colaterais."
        - "Verificar suposições lendo os arquivos relevantes ou executando comandos de descoberta."

    step_2_specification:
      name: "Specification (Especificação)"
      actions:
        - "Definir claramente O QUE será executado."
        - "Listar os resultados esperados e os requisitos técnicos."
        - "Definir os critérios exatos para considerar a implementação como 'sucesso'."

    step_3_planning:
      name: "Complete Planning (Planejamento)"
      actions:
        - "Projetar a abordagem arquitetural."
        - "Selecionar as ferramentas e bibliotecas necessárias (verificando sua disponibilidade)."
        - "Definir a estratégia de testes que será utilizada para validação."

    step_4_execution:
      name: "Atomic Task Execution (Execução Atômica)"
      actions:
        - "Quebrar o plano em tarefas pequenas, independentes e verificáveis."
        - "Utilizar estritamente os marcadores de status abaixo em cada resposta para rastrear o progresso."
      status_markers:
        pending: "- [ ] Tarefa Pendente: Ainda não iniciada."
        in_progress: "- [/] Em Andamento: Tarefa atualmente em execução. Marcar ao iniciar o turno."
        completed: "- [X] Concluída: Tarefa finalizada e verificada. Marcar imediatamente após o sucesso."
        error: "- [-] Erro/Falha: Ação obrigatória -> PARE a execução atual, inicie uma nova fase de planejamento focada exclusivamente na correção do erro e retome as tarefas originais apenas quando resolvido."

  example_usage:
    trigger_prompt: "Fix the login error"
    simulated_workflow:
      context: "Identificado que o 'AuthService' está lançando 401 devido a um cabeçalho ausente."
      spec: "Adicionar o cabeçalho 'X-API-KEY' a todas as requisições de saída em 'apps/common/services'."
      plan: "Modificar 'api_client.py', atualizar os testes unitários e rodar a suíte de integração."
      tasks:
        - "- [X] Ler 'apps/common/services/api_client.py' para identificar o ponto de injeção de headers."
        - "- [/] Atualizar o dicionário 'headers' dentro de 'ApiClient.request'."
        - "- [ ] Adicionar teste unitário em 'tests/test_api_client.py'."
        - "- [ ] Executar 'pytest tests/test_api_client.py'."