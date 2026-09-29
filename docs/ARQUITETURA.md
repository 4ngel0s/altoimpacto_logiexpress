# Arquitetura da LOGIEXPRESS 1.0

## Visão

A aplicação segue uma arquitetura web simples para facilitar a compreensão durante a prática de RAD.

```text
Usuário
  ↓
Navegador
  ↓
Flask / Gunicorn
  ↓
SQLAlchemy
  ↓
SQLite (local) ou PostgreSQL (cloud)
```

## Cloud

```text
GitHub
   ↓
GitHub Codespaces / VS Code Web
   ↓
Commit / Pull Request
   ↓
Render
   ↓
Aplicação Flask
   ↓
PostgreSQL
```

## Decisões didáticas

- SQLite local reduz barreiras para começar.
- PostgreSQL em cloud aproxima o exercício de um ambiente profissional.
- Flask deixa explícita a relação entre rota, regra, banco e template.
- Bootstrap permite concentrar o esforço dos alunos na lógica da aplicação.
- O sistema-base é completo para que a prática seja de evolução e não de configuração.
