
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/salvar", methods=["POST"])
def salvar():
    nome = request.form["nome"]
    obra = request.form["obra"]

    return f"✅ Dados recebidos de {nome} - {obra}"

if __name__ == "__main__":
    app.run()
``
