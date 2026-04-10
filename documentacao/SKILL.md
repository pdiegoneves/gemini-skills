# documentador

## Purpose
Esta skill automatiza a leitura de todo o código fonte disponível na pasta onde o agente for chamado e cria uma documentação em markdown no arquivo README.md. A documentação gerada segue rigorosamente o template do arquivo modelo.md.

## Mandatory Workflow

Sempre que ativada, você DEVE seguir exatamente este fluxo:

### Passo 1: Descoberta e Estruturação
1. O sistema deve **listar todos os módulos e arquivos** disponíveis na pasta de trabalho.
2. Ler os arquivos para **entender a estrutura**.
3. **Definir por onde começar** e qual a **sequência lógica** que deve seguir para a documentação.

### Passo 2: Criação do Plano de Ação (doc_plan.md)
1. Crie o arquivo doc_plan.md no formato de checklist de tarefas atômicas, iterativas e autoexplicativas.
   Use marcadores de markdown:
   - [ ] Tarefa pendente
   - [/] Tarefa em andamento
   - [X] Tarefa concluída

### Passo 3: Confirmação do Usuário
**OBRIGATÓRIO:** Com o arquivo doc_plan.md gravado no disco, **solicite a confirmação** do usuário para iniciar a implementação. NÃO prossiga sem o "ok" do usuário.

### Passo 4: Implementação Passo a Passo
1. Após a aprovação, implemente e conduza a documentação do README.md **passo a passo**.
2. Siga as seções definidas no template `templates\readme_model.md`:
3. A cada passo concluído, atualize o checklist no prompt e adicione o carimbo de data e hora no padrão exato YYYY-MM-DD HH:MM:SS.
   Exemplo: - [X] Ler arquivo X e documentar Regras de Negócio -> 2026-04-10 10:50:00
4. Mostre sempre o progresso iterativo.

## Non-Goals
- Nunca invente regras de negócio que não forem encontradas no código

