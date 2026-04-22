from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "vidracaria_secret"

vidros = []
contador_id = 1  # Controla IDs únicos mesmo após deletar


# ── Helpers ──────────────────────────────────────────────────────────────────

def _validar_form(form):
    """
    Valida os campos do formulário.
    Retorna (nome, tipo, preco) em caso de sucesso ou levanta ValueError com
    a mensagem de erro.
    """
    nome = form.get("nome", "").strip()
    tipo = form.get("tipo", "").strip()
    preco_str = form.get("preco", "").strip()

    if not nome or not tipo or not preco_str:
        raise ValueError("Todos os campos são obrigatórios.")

    try:
        preco = float(preco_str.replace(",", "."))
        if preco < 0:
            raise ValueError
    except ValueError:
        raise ValueError("Preço inválido. Use um número positivo.")

    return nome, tipo, preco


def _buscar_vidro(vidro_id):
    """Retorna o vidro com o id informado ou None."""
    return next((v for v in vidros if v["id"] == vidro_id), None)


# ── Rotas ─────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html", vidros=vidros)


@app.route("/criar", methods=["GET", "POST"])
def criar_vidro():
    global contador_id

    if request.method == "POST":
        try:
            nome, tipo, preco = _validar_form(request.form)
        except ValueError as e:
            flash(str(e), "danger")
            return render_template("form.html", acao="Cadastrar", vidro=None)

        vidros.append({"id": contador_id, "nome": nome, "tipo": tipo, "preco": preco})
        contador_id += 1

        flash(f'Vidro "{nome}" cadastrado com sucesso!', "success")
        return redirect(url_for("index"))

    return render_template("form.html", acao="Cadastrar", vidro=None)


@app.route("/editar/<int:vidro_id>", methods=["GET", "POST"])
def atualizar_vidro(vidro_id):
    vidro = _buscar_vidro(vidro_id)

    if vidro is None:
        flash("Vidro não encontrado.", "danger")
        return redirect(url_for("index"))

    if request.method == "POST":
        try:
            nome, tipo, preco = _validar_form(request.form)
        except ValueError as e:
            flash(str(e), "danger")
            return render_template("form.html", acao="Atualizar", vidro=vidro)

        vidro["nome"] = nome
        vidro["tipo"] = tipo
        vidro["preco"] = preco

        flash(f'Vidro "{nome}" atualizado com sucesso!', "success")
        return redirect(url_for("index"))

    return render_template("form.html", acao="Atualizar", vidro=vidro)


@app.route("/deletar/<int:vidro_id>", methods=["POST"])
def deletar_vidro(vidro_id):
    global vidros
    vidro = _buscar_vidro(vidro_id)

    if vidro is None:
        flash("Vidro não encontrado.", "danger")
    else:
        vidros = [v for v in vidros if v["id"] != vidro_id]
        flash(f'Vidro "{vidro["nome"]}" removido com sucesso!', "success")

    return redirect(url_for("index"))


# ── Entrypoint ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app.run(debug=True)
