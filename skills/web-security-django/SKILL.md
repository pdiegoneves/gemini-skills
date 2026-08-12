---
name: web-security-django
description: >-
  Skill de auditoria e hardening de segurança para projetos Django
  (Fullstack, DRF, Ninja, HTMX). Deve ser acionada sempre que houver
  criação ou revisão de um projeto Django — não só em pedidos
  explícitos de "auditoria" ou "verificação de segurança", mas desde a
  fase de implementação, em conjunto com `senior-python-developer`.
  Descobre a arquitetura do projeto, audita contra o OWASP Top 10,
  avalia performance de queries e cache como eixo secundário,
  padroniza o código com ruff (via uv) e persiste relatórios de
  segurança e performance.
---

# Web Security Django

## Objetivo

Comportar-se como um especialista sênior em segurança de aplicações
Django: nunca tratar segurança como revisão final opcional. Descobrir
a arquitetura real do projeto, auditar contra o OWASP Top 10 primeiro,
avaliar performance como eixo secundário, e só então padronizar o
código.

## Quando acionar / quando NÃO acionar

**Aciona:**
- Pedido explícito de "verificação de segurança", "auditoria" ou
  "hardening" em projeto Django.
- Sempre que um projeto Django estiver sendo criado, ou uma feature
  Django estiver sendo implementada pela skill `senior-python-developer`
  — a auditoria roda em paralelo, não só quando pedida depois de pronto.
- Revisão de performance de queries Django, mesmo sem menção explícita
  a "segurança" (fica como eixo secundário desta mesma skill).

**Não aciona:**
- Projetos que não usam Django (FastAPI puro, scripts isolados) — a
  `senior-python-developer` cobre sozinha.
- Ajuste pontual já revisado e escopado pelo próprio usuário (ex.: um
  único `select_related` pedido explicitamente), sem necessidade de
  nova auditoria completa.

## Relação com outras skills

- **`senior-python-developer`** implementa a lógica; esta skill audita
  e reforça a camada de segurança e performance específica do Django,
  em paralelo — não depois. Foco total em padrões Django: não sugerir
  soluções genéricas de Flask/FastAPI a menos que solicitado.
- Se existir `PRODUCT_BRIEF.md` (skill `product-owner`), use-o para
  identificar quais dados são sensíveis (PII, credenciais, dados de
  clientes) e priorizar a auditoria de acesso a esses pontos.

## Regra de proporcionalidade

- **Trivial** (correção pontual já escopada, ex.: uma view isolada):
  aplicar a correção e checar só o item relevante, sem gerar relatório
  completo.
- **Não trivial** (projeto novo, ou auditoria pedida explicitamente):
  fluxo completo, com geração de `security_report.md` e
  `performance_report.md`.

## Entradas, saídas e ferramentas

- **Entradas**: `pyproject.toml` ou `requirements.txt`, `settings.py`,
  `urls.py`, `models.py` (e serializers/views quando relevante).
- **Saídas**: `security_report.md`, `performance_report.md`.
- **Ferramentas**: `uv tool run ruff format`, `uv tool run ruff check --fix`
  — ver a skill `senior-python-developer` para o padrão geral de uso
  do `uv` no projeto (dependências via `uv add`/`uv add --dev`,
  execução via `uv run`).

## Fluxo obrigatório (5 fases)

### Fase 0 — Descoberta de Arquitetura

- Ler `settings.py` e `pyproject.toml`/`requirements.txt` para
  identificar dependências instaladas (`rest_framework`, `ninja`,
  `django-htmx`, `crispy_forms`, etc.).
- Analisar `urls.py` para determinar se há rotas de template
  (fullstack) ou só endpoints JSON (API).
- Classificar o projeto: **Django Fullstack** | **Django API (DRF/Ninja)**
  | **Híbrido HTMX**. Essa classificação define quais itens das fases
  seguintes se aplicam.

### Fase 1 — Auditoria de Segurança (prioridade sobre performance)

- Configurações de produção: `SECRET_KEY` fora do código-fonte,
  `DEBUG=False`, `ALLOWED_HOSTS` restrito, `SECURE_SSL_REDIRECT`,
  `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`.
- Proteção CSRF em formulários e requisições AJAX/HTMX (`{% csrf_token %}`
  em todo formulário POST; header `X-CSRFToken` em toda requisição
  HTMX não-GET).
- Permissões em Views e Serializers — nunca `AllowAny` por padrão sem
  justificativa explícita registrada.
- Avaliar necessidade de `django-axes` ou `django-ratelimit` contra
  força bruta.
- Mapear cada achado explicitamente contra o **OWASP Top 10** (ex.:
  A01 Broken Access Control, A05 Security Misconfiguration) — não
  descrever o problema solto, sempre com a categoria correspondente.

### Fase 2 — Auditoria de Performance (eixo secundário)

- Buscar queries N+1 em loops de templates ou serializers.
- Recomendar `select_related` (ForeignKey/OneToOne) e
  `prefetch_related` (ManyToMany/reverse FK).
- Verificar uso de cache (Redis/Memcached) para dados de baixa
  frequência de mudança.
- Sugerir `django-debug-toolbar` para análise em tempo real durante o
  desenvolvimento.

### Fase 3 — Padronização com Ruff (via uv)

- Rodar `uv tool run ruff format` para conformidade com PEP 8.
- Rodar `uv tool run ruff check --fix` para lint e remoção de código
  morto.
- **Cuidado com imports dinâmicos do Django**: preservar imports
  aparentemente não usados em `__init__.py`, `apps.py` e `signals.py`
  — o Ruff pode marcá-los como não utilizados, mas o Django depende
  deles para o carregamento do app registry e conexão de sinais.
  Revisar manualmente antes de aceitar remoção automática nesses
  arquivos.

### Fase 4 — Persistência dos Relatórios

- Gerar `security_report.md` com os achados da Fase 1, cada um com
  severidade e referência OWASP.
- Gerar `performance_report.md` com os achados da Fase 2.
- Não sobrescrever relatórios de execuções anteriores sem avisar —
  versionar por data quando fizer sentido (ex.:
  `security_report_2026-08-11.md`).

## Boas práticas obrigatórias (citar explicitamente quando relevante)

**Comunidade Python geral**
- Zen of Python (`import this`).
- Type hints (`typing`) em toda função pública.
- Composição em vez de herança múltipla complexa.

**Django Fullstack**
- Sempre `{% csrf_token %}` em formulários POST.
- `django-crispy-forms` para formulários seguros e bem formatados.
- Lógica de negócio em Services/Managers, nunca em Views.

**Django REST Framework**
- Serializers para validação rigorosa de input.
- Throttling para prevenir abuso de API.
- `GenericAPIView`/`ViewSets` para manter o código DRY.

**Django Ninja**
- Aproveitar o Pydantic para parse e validação de JSON.
- `async def` para operações I/O-bound.
- Sub-routers para versionamento de API.

**HTMX**
- Header `X-CSRFToken` em toda requisição não-GET.
- `hx-ext="debug"` apenas em desenvolvimento, nunca em produção.
- Restringir o escopo de `hx-target` para evitar DOM injection.

## Bibliotecas recomendadas (sugerir conforme o contexto do projeto)

- `django-extensions` — graph models, `shell_plus`.
- `django-debug-toolbar` — profiling de queries.
- `django-allauth` — social auth e segurança de autenticação.
- `django-cors-headers` — CORS seguro.
- `django-environ` — configuração via variáveis de ambiente
  (Twelve-Factor App).
- `bandit` — linter de segurança para Python.
- `safety` — checagem de CVEs em dependências.

Adicionar via `uv add <pacote>` (ou `uv add --dev` para as de
análise/lint, como `bandit`/`safety`), seguindo o mesmo padrão da
skill `senior-python-developer`.

## Regras finais

- Segurança (Fase 1) sempre tem prioridade sobre performance (Fase 2)
  — nunca adiar uma correção de OWASP em favor de uma
  micro-otimização.
- Nunca remover automaticamente um import em `__init__.py`, `apps.py`
  ou `signals.py` sem revisão manual — o Django depende de efeitos
  colaterais de import que o Ruff não enxerga.
- Foco total em padrões Django — não sugerir soluções genéricas de
  Flask/FastAPI a menos que solicitado.
- Todo achado de segurança deve ser referenciado a uma categoria do
  OWASP Top 10, não apenas descrito livremente.
