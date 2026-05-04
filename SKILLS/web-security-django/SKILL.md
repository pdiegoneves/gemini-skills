---
name: web-security-django
description: "Especialista em auditoria de segurança e performance para Django. Detecta arquitetura e aplica ruff."
category: security
risk: low
source: my
date_added: "2026-05-04"
---
skill:
  metadata:
    name: web-security-django
    alias: django-sec
    description: "Skill especializada em diagnosticar, formatar e proteger aplicações Django (Fullstack, API, Ninja, DRF, HTMX)."
    category: security
    risk: low
    source: pdseven
    date_added: "2026-05-04"

  purpose: "Automatizar a análise de segurança e performance em ecossistemas Django, identificando automaticamente se o projeto é Backend-only ou Fullstack e aplicando correções via Ruff e recomendações arquiteturais."

  trigger_conditions:
    mandatory_usage: "Esta skill deve ser ativada sempre que o usuário solicitar 'verificação de segurança', 'auditoria' ou 'melhoria de performance' em projetos que contenham arquivos Django."

  resources:
    inputs:
      - "pyproject.toml ou requirements.txt"
      - "settings.py"
      - "urls.py"
      - "models.py"
    tools:
      - "uv tool run ruff format"
      - "uv tool run ruff check --fix"
    outputs:
      - "security_report.md"
      - "performance_report.md"

  constraints:
    - "DJANGO_CORE: Foco total em padrões Django. Não sugira soluções genéricas de Flask/FastAPI a menos que solicitado."
    - "RUFF_INTELLIGENCE: Ao formatar, preserve imports manuais em __init__.py ou locais onde o Django faz carregamento dinâmico (ex: apps.py, signals.py)."
    - "SECURITY_FIRST: Priorize correções de vulnerabilidades (OWASP Top 10) sobre micro-otimizações de performance."

  workflow:
    step_1_discovery:
      name: "Descoberta de Arquitetura"
      actions:
        - "Ler 'settings.py' e 'pyproject.toml' para identificar dependências (rest_framework, ninja, htmx, crispy_forms)."
        - "Analisar 'urls.py' para determinar se há rotas de templates ou apenas endpoints JSON."
        - "Classificar o projeto: [Django Fullstack | Django API (DRF/Ninja) | Hybrid HTMX]."

    step_2_security_analysis:
      name: "Auditoria de Segurança"
      actions:
        - "Verificar configurações de produção: SECRET_KEY, DEBUG, ALLOWED_HOSTS, SECURE_SSL_REDIRECT."
        - "Validar proteção CSRF em formulários e requisições AJAX/HTMX."
        - "Inspecionar permissões em Views e Serializers (evitar AllowAny por padrão)."
        - "Sugerir 'django-axes' ou 'django-ratelimit' para proteção contra força bruta."

    step_3_performance_analysis:
      name: "Auditoria de Performance"
      actions:
        - "Buscar por 'Queries N+1' em loops de templates ou serializers."
        - "Recomendar 'select_related' para ForeignKey/OneToOne e 'prefetch_related' para ManyToMany."
        - "Verificar o uso de caching (Redis/Memcached) para dados pouco frequentes."
        - "Sugerir 'django-debug-toolbar' para análise em tempo real."

    step_4_code_standardization:
      name: "Padronização com Ruff"
      actions:
        - "Executar 'uv tool run ruff format' para garantir conformidade com PEP 8."
        - "Executar 'uv tool run ruff check --fix' para remover código morto e aplicar linting de segurança."
        - "Revisar mudanças nos imports para garantir que não quebram o 'registry' do Django."

  best_practices_catalog:
    python_community:
      - "Siga o 'The Zen of Python' (import this)."
      - "Use Type Hints (typing) para clareza e ferramentas de análise estática."
      - "Prefira composição sobre herança múltipla complexa."
    django_fullstack:
      - "Sempre use {% csrf_token %} em formulários POST."
      - "Use 'django-crispy-forms' para formulários seguros e bem formatados."
      - "Mantenha lógica de negócio em Services ou Managers, não em Views."
    django_drf:
      - "Use Serializers para validação rigorosa de input."
      - "Implemente Throttling para prevenir abusos na API."
      - "Use 'GenericAPIView' ou 'ViewSets' para manter o código DRY."
    django_ninja:
      - "Aproveite a performance do Pydantic para parse de JSON."
      - "Use execução assíncrona (async def) para I/O-bound tasks."
      - "Organize versões de API usando sub-routers."
    htmx_security:
      - "Configure o header 'X-CSRFToken' em todas as requisições não-GET via HTMX."
      - "Use 'hx-ext=\"debug\"' apenas em desenvolvimento."
      - "Restrinja o escopo de 'hx-target' para evitar ataques de 'DOM injection'."

  recommended_plugins:
    - "django-extensions (Graph models, shell_plus)"
    - "django-debug-toolbar (Profile queries)"
    - "django-allauth (Social auth & security)"
    - "django-cors-headers (CORS safety)"
    - "django-environ (Twelve-Factor App config)"
    - "bandit (Security linter for Python)"
    - "safety (Check dependencies for CVEs)"
