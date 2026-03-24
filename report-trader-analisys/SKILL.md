---
name: report-trader-analisys
description: Essa skils devera ser utilizada para avaliar os relatórios financeiros do sistema de trader
---

# Análise de relatórios
Abaixo segue a estrutura de alguns relatórios que você pode encontrar


## Tipos de relatórios
### ReportHistory
Geralmente será um arquivo xlsx
Ao recber esse arquivo você deve chamar o script `python-quantum-developer\scripts\ler-xlsx.py` passando o caminho do arquivo xlsx. Isso irá gerer 4 arquivos distintos. 'posicoes. 'ordens.csv', 'transacoes.csv' e 'resultados.csv'. Esses arquivos que você deve analisar




### Sumário executivo
Pode ser um arquivo de texto ou colado diretamente no prompt
Contem diversas estatística do robo para lhe ajudar a avaliar as estratégias

### quantum_forensic_report
Um arquivo de texto que contém o resultado do último backtest e mostra o resultado esperado de cada estratégia.


## Diretrizes Analíticas Obrigatórias:

1. Foco na Gestão de Risco: Analise imediatamente o Maximum Drawdown (MDD), o Risco de Ruína, o tamanho da posição (position sizing) e a assimetria de Risco/Retorno.
2. Viés de Curva (Overfitting): Se a estratégia parecer perfeita no passado, questione a robustez no futuro. Questione se há excesso de otimização de parâmetros.
3. Custos Ocultos: Considere sempre o impacto de slippage, taxas de corretagem, impostos e funding rates que o trader possa ter ignorado.
4. Métricas Técnicas: Use ativamente conceitos como Índice Sharpe, Índice Sortino, Expectância Matemática, Fator de Lucro (Profit Factor) e Win Rate em relação ao Payoff.
5. Comportamento e Viéses: Identifique sinais de "preço médio para trás" (martingale), aversão à perda, overtrading ou alavancagem suicida disfarçada de convicção.


## Fluxo de trabalho
1. Avalie os arquivos disponíveis
2. Entenda o que está acontecendo com o sistema
3. Compare os resultados reais com o do bakctest e valide se estão condizentes

## Formato da Resposta Esperada:

1. Diganóstico geral:
1.1. Diagnóstico Rápido: Um parágrafo resumindo a realidade da sistema como um todo.
1.2. Falhas Críticas Encontradas: Pontos em bullet points apontando exatamente onde o robo  sangra dinheiro ou onde está o risco de quebra.
1.3. Análise das Métricas: Crítica direta aos números apresentados.
1.4. Veredito/Correção Necessária: O que precisa ser ajustado matematicamente para robo ter expectativa positiva real a longo prazo.

2. Diagnóstico por estratégia:
2.1. Diagnóstico Rápido de cada estratégia: Um parágrafo resumindo a realidade da estratégia (ex: "Estratégia com risco de cauda alto e alavancagem excessiva").
2.2. Falhas Críticas Encontradas: Pontos em bullet points apontando exatamente onde o robo estratégia sangra dinheiro ou onde está o risco de quebra.
2.3. Análise das Métricas: Crítica direta aos números apresentados.
2.4. Veredito/Correção Necessária: O que precisa ser ajustado matematicamente para a estratégia ter expectativa positiva real a longo prazo.

os resultados devem ser salvos em um arquivo txt na rais do projeto como "expert-analisys.txt"