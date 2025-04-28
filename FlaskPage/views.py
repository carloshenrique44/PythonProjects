
from app import app
from flask import render_template, redirect, url_for

@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/redirecionar", methods=["POST"])
def redirecionar():
    return redirect(url_for("outra_pagina")) 


@app.route("/outra_pagina") 
def outra_pagina():
    return render_template("outra_pagina.html")
