from flask import Flask, redirect, render_template, request

app = Flask(__name__)

app.secret_key = "uva"

lista_de_comentario = []

@app.route("/principal")
@app.route("/")
def pagina_principal():
    return render_template("principal.html")

@app.route("/about", methods=["GET"])
def sobre():
    return render_template("about.html")

@app.route("/senha", methods=["GET"])
def senha():
    return render_template("senha.html")

@app.route("/senha", methods=["POST"])
def senha_post():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    if usuario == "Luan Santana" and senha == "ilyluan":
        return redirect("/comentarios")
        
    else:
      return render_template("senha.html", msg_erro = "Senha incorreta")

@app.route("/comentarios")
def comentario():
    return render_template("comentarios.html", lista_de_comentario_html = lista_de_comentario)

@app.route("/adicionar_comentario", methods=["POST"])
def adicionar_comentario():
    coment = request.form.get("comentario")
    lista_de_comentario.append(coment)
    print(lista_de_comentario)
    return redirect("/comentarios")

app.run(debug=True)