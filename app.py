

from flask import Flask, render_template, request

app = Flask(__name__)  # ✅ ESSA LINHA É OBRIGATÓRIA

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/salvar", methods=["POST"])
def salvar():
    form = request.form

    pontos = 0

    # Área
    if form.get("area") == "1000-5000":
        pontos += 10
    elif form.get("area") == "+5000":
        pontos += 20

    # Perguntas
    if form.get("cliente_final") == "Sim":
        pontos += 1

    if form.get("orgao_publico") == "Não":
        pontos += 1

    if form.get("retrofit") == "Sim":
        pontos += 20

    if form.get("sistema_antigo") == "Sim":
        pontos += 20

    if form.get("hvac_critico") == "Sim":
        pontos += 20

    if form.get("projeto_executivo") == "Sim":
        pontos += 20

    if form.get("eficiencia") == "Sim":
        pontos += 10

    if form.get("decisores") == "Sim":
        pontos += 20

    if form.get("engenharia") == "Sim":
        pontos += 20

    if form.get("instaladores") == "Não":
        pontos += 30

    # Classificação
    if pontos >= 120:
        status = "✅ QUALIFICADO"
    elif pontos >= 70:
        status = "⚠️ MÉDIO POTENCIAL"
    else:
        status = "❌ DECLINADO"

    return f"<h2>{status}</h2><p>{pontos} pontos</p><a href='/'>Voltar</a>"

if __name__ == "__main__":
    app.run()



