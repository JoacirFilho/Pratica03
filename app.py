from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template("paginas/index.html", \
        titulo_pagina="Página inicial")
    
@app.route("/cadastrar")
def sobre():
    return render_template("paginas/cadastrar.html", \
        titulo_pagina="Cadasstrar")
    
@app.route("/veterinarios")
def veterinarios():
    return render_template("paginas/veterinarios.html", \
        titulo_pagina="Veterinarios")

@app.route("/contato")
def contato():
    return render_template("paginas/contato.html", \
        titulo_pagina="Contatos")

@app.route("/medicamentos")
def medicamentos():
    return render_template("paginas/medicamentos.html", \
        titulo_pagina="Medicamentos")
    
if __name__ == "__main__":
    app.run(debug=True)