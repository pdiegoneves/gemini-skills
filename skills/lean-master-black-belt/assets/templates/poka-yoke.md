# Template — Poka-Yoke (Mecanismo à Prova de Erro)

**Quando usar:** um erro humano se repete apesar de treinamento, atenção reforçada ou instrução clara. Se a contramedida proposta é "reforçar treinamento" ou "pedir mais atenção" para um erro recorrente, é sinal de que falta um Poka-Yoke — pessoas não erram por falta de vontade, erram porque o sistema permite o erro.

## Passo 1 — Classificar o tipo de defeito
- **Erro de processamento:** etapa foi pulada ou feita errado.
- **Erro de setup:** ferramenta/peça/configuração errada usada.
- **Peça/material faltando ou errado.**
- **Erro de operação/ajuste.**
- **Erro de medição.**

## Passo 2 — Escolher o nível de intervenção (do mais forte ao mais fraco)
| Nível | Descrição | Exemplo |
|---|---|---|
| 1. Prevenção física | Torna o erro **impossível** — o encaixe errado simplesmente não entra. | Conector USB-C (não tem "lado errado"); pino guia assimétrico. |
| 2. Detecção automática | Torna o erro **imediatamente detectável** pelo próprio sistema, parando o processo (Jidoka). | Sensor de peso que barra a caixa se faltar item; checklist digital que não avança sem campo obrigatório. |
| 3. Alerta sensorial | Sinaliza o erro para um humano agir rápido. | Alarme sonoro/luz — mais fraco que os dois acima, porque ainda depende de resposta humana. |

**Priorize sempre o nível mais forte que for viável** — "colocar um aviso" (nível 3) é o último recurso, não a primeira ideia.

## Passo 3 — Template de análise
| Erro observado | Frequência/impacto | Nível de Poka-Yoke proposto | Descrição do mecanismo | Custo estimado | Quem implementa |
|---|---|---|---|---|---|
| | | | | | |

## Passo 4 — Validar antes de escalar
Teste o mecanismo tentando deliberadamente cometer o erro de propósito — se ainda é possível, o Poka-Yoke não está completo.

---

**Nota para ambientes de software/serviços:** Poka-Yoke aqui vira validação de formulário que não deixa submeter campo obrigatório vazio, valores default seguros, confirmação de ação destrutiva, ou testes automatizados que travam o deploy — o princípio (impossibilitar > detectar > alertar) é o mesmo.
