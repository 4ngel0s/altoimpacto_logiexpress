# Integração das novas páginas no menu

No `templates/base.html`, dentro da navegação, adicione:

```html
<li class="nav-item">
    <a class="nav-link" href="{{ url_for('documentacao_tecnica') }}">
        Documentação Técnica
    </a>
</li>

<li class="nav-item">
    <a class="nav-link" href="{{ url_for('documentacao_auxiliar') }}">
        Documentação Auxiliar
    </a>
</li>
```

As rotas adicionadas ao `app.py` são:

```python
@app.route("/documentacao-tecnica")
def documentacao_tecnica():
    return render_template("documentacao_tecnica.html")

@app.route("/documentacao-auxiliar")
def documentacao_auxiliar():
    return render_template("documentacao_auxiliar.html")
```
