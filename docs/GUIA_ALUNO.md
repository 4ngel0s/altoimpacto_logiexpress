# Guia do aluno — LOGIEXPRESS 1.0

## 1. O que estamos construindo?

A LOGIEXPRESS é uma aplicação web de apoio à operação logística. Ela possui cadastros, operações e relatórios.

## 2. O que observar no código?

- `app.py`: configuração Flask, modelos, rotas, regras e inicialização.
- `templates/`: páginas HTML renderizadas pelo Flask.
- `static/`: arquivos visuais.
- `requirements.txt`: bibliotecas necessárias.
- `render.yaml`: referência de publicação no Render.

## 3. Conceito essencial

Uma requisição do navegador chega a uma **rota Flask**. A rota consulta ou altera os **modelos SQLAlchemy**, que representam tabelas do banco. Depois o Flask devolve um **template HTML**.

Fluxo simplificado:

`Navegador → Flask → SQLAlchemy → Banco → Flask → HTML`

## 4. Como trabalhar no dia 30/09

1. Criar uma branch para o grupo.
2. Ler o requisito recebido.
3. Localizar as partes do sistema que precisam ser alteradas.
4. Implementar.
5. Testar.
6. Fazer commit.
7. Abrir Pull Request.
8. Demonstrar a funcionalidade.

## 5. Regra da prática

Não apagar funcionalidades existentes. A nova demanda deve ser incorporada ao sistema atual.
