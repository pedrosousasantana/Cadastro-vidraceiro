from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(**name**)
app.secret_key = “vidracaria_secret”

vidros = []
contador_id = 1  # Controla IDs únicos mesmo após deletar

@app.route(”/”)
def index():
return render_template(“index.html”, vidros=vidros)

@app.route(”/criar”, methods=[“GET”, “POST”])
def criar_vidro():
if request.method == “POST”:
global contador_id

```
    nome = request.form.get("nome", "").strip()
    tipo = request.form.get("tipo", "").strip()
    preco_str = request.form.get("preco", "").strip()

    # Validações
    if not nome or not tipo or not preco_str:
        flash("Todos os campos são obrigatórios.", "danger")
        return render_template("form.html", acao="Cadastrar", vidro=None)

    try:
        preco = float(preco_str.replace(",", "."))
        if preco < 0:
            raise ValueError
    except ValueError:
        flash("Preço inválido. Use um número positivo.", "danger")
        return render_template("form.html", acao="Cadastrar", vidro=None)

    vidro = {
        "id": contador_id,
        "nome": nome,
        "tipo": tipo,
        "preco": preco,
    }
    vidros.append(vidro)
    contador_id += 1

    flash(f'Vidro "{nome}" cadastrado com sucesso!', "success")
    return redirect(url_for("index"))

return render_template("form.html", acao="Cadastrar", vidro=None)
```

@app.route(”/editar/<int:vidro_id>”, methods=[“GET”, “POST”])
def atualizar_vidro(vidro_id):
vidro = next((v for v in vidros if v[“id”] == vidro_id), None)

```
if vidro is None:
    flash("Vidro não encontrado.", "danger")
    return redirect(url_for("index"))

if request.method == "POST":
    nome = request.form.get("nome", "").strip()
    tipo = request.form.get("tipo", "").strip()
    preco_str = request.form.get("preco", "").strip()

    if not nome or not tipo or not preco_str:
        flash("Todos os campos são obrigatórios.", "danger")
        return render_template("form.html", acao="Atualizar", vidro=vidro)

    try:
        preco = float(preco_str.replace(",", "."))
        if preco < 0:
            raise ValueError
    except ValueError:
        flash("Preço inválido. Use um número positivo.", "danger")
        return render_template("form.html", acao="Atualizar", vidro=vidro)

    vidro["nome"] = nome
    vidro["tipo"] = tipo
    vidro["preco"] = preco

    flash(f'Vidro "{nome}" atualizado com sucesso!', "success")
    return redirect(url_for("index"))

return render_template("form.html", acao="Atualizar", vidro=vidro)
```

@app.route(”/deletar/<int:vidro_id>”, methods=[“POST”])
def deletar_vidro(vidro_id):
global vidros
vidro = next((v for v in vidros if v[“id”] == vidro_id), None)

```
if vidro is None:
    flash("Vidro não encontrado.", "danger")
else:
    vidros = [v for v in vidros if v["id"] != vidro_id]
    flash(f'Vidro "{vidro["nome"]}" removido com sucesso!', "success")

return redirect(url_for("index"))
```

if **name** == “**main**”:
app.run(debug=True)