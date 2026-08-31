# Template — 5 Porquês + Diagrama de Ishikawa (Espinha de Peixe)

**Quando usar:** encontrar a causa raiz de um problema recorrente. 5 Porquês é rápido e individual/pequena equipe; Ishikawa é melhor quando há múltiplas categorias de causa possíveis e uma equipe maior precisa convergir.

## 5 Porquês

**Problema:** [descreva o efeito observável, com dado — "atraso de 3 dias na entrega do pedido X", não "processo ruim"]

1. Por quê? → _______
2. Por quê (a resposta 1 acontece)? → _______
3. Por quê? → _______
4. Por quê? → _______
5. Por quê? → _______ ← geralmente aqui aparece causa sistêmica

**Regra crítica:** siga o **processo**, não a **pessoa**. Se a 1ª resposta é "porque esqueci", a 2ª NÃO é "porque sou esquecido" — é "porque não há lembrete visual no momento certo". Se qualquer "porquê" aterrissar em característica pessoal, volte um nível e pergunte "o que no sistema tornou esse erro possível/provável?"

**Critério de causa raiz válida:** revela algo sistêmico (processo, falta de padronização, incentivo mal desenhado) — não uma culpa individual.

---

## Diagrama de Ishikawa (6M)

Categorias-padrão para gerar hipóteses de causa (adapte conforme o setor — em serviços/software, substitua "Máquina" e "Material" por "Sistema/Ferramenta" e "Dados/Input"):

```
                    Método          Máquina/Sistema
                       \                /
                        \              /
    Mão de obra ————————— [PROBLEMA] ————————— Medição
                        /              \
                       /                \
                  Material/Input      Meio Ambiente
```

Para cada categoria (M), faça brainstorming de causas possíveis com a equipe antes de convergir. Depois, aplique 5 Porquês nas 2–3 causas mais prováveis de cada categoria para chegar à raiz.

**Priorização:** se houver dado suficiente, valide as causas hipotéticas com Pareto (quais causas respondem por 80% da ocorrência) antes de agir — não implemente contramedida para a causa "mais óbvia" sem checar se ela é, de fato, a mais frequente/impactante.
