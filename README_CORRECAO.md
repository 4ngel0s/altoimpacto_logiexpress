# LOGIEXPRESS 1.1 — Pacote consolidado de documentação e exercícios

Este pacote corrige a integração entre `app.py` e as páginas de documentação/exercícios.

## Rotas incluídas

- `/documentacao-tecnica`
- `/documentacao-auxiliar`
- `/guia-git-integracao`
- `/kanban`
- `/desafios`
- `/instrucoes`
- `/atividades-3009` → redireciona para `/desafios`

## Menu esperado

- Dashboard
- Cadastros
- Relatórios
- Documentação
  - Documentação Técnica
  - Documentação Auxiliar
  - Guia Git e Integração
  - Kanban do Produto
- 20 Exercícios
- Instruções 29/09

## Importante

Não substitua `static/`, `instance/` ou o banco de dados do seu Codespace com este pacote.
Aplique os arquivos deste pacote sobre o projeto que já está funcionando.

Depois, teste com:

```bash
python3 -m py_compile app.py
python3 app.py
```

Antes de iniciar o Git, confirme no navegador:

1. Dashboard
2. Cadastros → Clientes
3. Documentação → Documentação Técnica
4. Documentação → Documentação Auxiliar
5. Documentação → Guia Git e Integração
6. Documentação → Kanban do Produto
7. 20 Exercícios
8. Instruções 29/09

Somente depois de tudo funcionando devemos fazer o primeiro `git status` e iniciar a configuração do Git.
