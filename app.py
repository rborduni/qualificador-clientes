
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/salvar", methods=["POST"])
def salvar():
    nome = request.form.get("nome")
    obra = request.form.get("obra")

    return f"✅ Dados recebidos: {nome} - {obra}"

if __name__ == "__main__":
    app.run()

