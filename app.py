from flask import Flask, redirect, render_template, request, session

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

@app.route("/login", methods=["POST"])
def senha_post():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    if usuario == "Luan Santana" and senha == "ilyluan":
        session["usuario"] = "luan santana"
        return redirect("/comentario")
        
    else:
      return render_template("senha.html", msg_erro = "Senha incorreta")

@app.route("/comentario")
def comentario():
    if "usuario" in session:
        return render_template("comentario.html", lista_de_comentario_html = lista_de_comentario)
    else:
        return redirect("/login")
        

@app.route("/adicionar_comentario", methods=["POST"])
def adicionar_comentario():
    coment = request.form.get("comentario")
    lista_de_comentario.append(coment)
    print(lista_de_comentario)
    return redirect("/comentario")

if __name__  == "__main__":
    app.run(host="0.0.0.0", port=8080, debug= True)