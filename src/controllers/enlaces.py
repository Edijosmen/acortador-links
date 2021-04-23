from flask import render_template, request, redirect, url_for, jsonify, session
from src import app
from src.models.enlaces import EnlaceModel
import random ,string
import pyshorteners
import webbrowser

enlaceModel = EnlaceModel()

@app.route('/enlaces', methods=['GET'])
def enlaces():
    if 'username' not in session:
        return redirect(url_for('login'))
    else:
        usuario = session['username']
        print(usuario)
        return render_template('enlace.html', sesion=session)


@app.route("/enlaces/create", methods =['GET', 'POST'])
def enlaceCrear():
    cadena = ""
    enlaceModel = EnlaceModel()
    for i in range(4):
        cadena += random.choice(string.ascii_letters)
        print("letraaa",cadena)
    if request.method == 'GET':
        if 'username' not in session:
            return redirect(url_for('login'))
        else:
            return render_template('enlace.html', sesion=session)
    else:
        usuario = session['username']
        enlacecorto="127.0.0.1:5000/"+ cadena
        url = request.form.get('url')
        iduser = enlaceModel.find_iduser(usuario)
        for id in iduser:
            isidUser = id
        print("valor",isidUser)
        print("valor",type(isidUser))
        enlaceModel.crearUrl(url,enlacecorto,isidUser)
        return render_template('enlace.html',url=enlacecorto ,sesion=session)



@app.route("/my/enlaces", methods =['POST','GET'])
def listarEnlaces():
    enlaceModel = EnlaceModel()
    user = session['username']
    if request.method =="GET":
        if 'username' not in session:
            return redirect(url_for("login"))
        else:
            links = enlaceModel.listarEnlace(user)
            print(links)
            return render_template("listar.html",links = links, sesion=session)

@app.route("/<link>" , methods =['GET'])
def abrirenlaces(link):
    enlacecorto ="127.0.0.1:5000/"+ link
    enlaceModel = EnlaceModel()
    encontrado = enlaceModel.find_link(enlacecorto)
    print("ecn",encontrado)
    if encontrado == "None":
        return redirect(url_for(enlace))
    else:
        for islink in encontrado:
            print("enlace",type(islink))
        return redirect(islink)

@app.route("/eliminar/<int:id>")
def eliminar(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    else:
        enlaceModel.eliminarEnlace(id)
        return redirect(url_for('listarEnlaces'))

@app.route("/update/<int:id>",methods =['POST','GET'])
def editarEnlace(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    else:
        dateLink = enlaceModel.verEnlaceuser(id)
        if request.method =="GET":
            return render_template("editarEnlace.html", date=dateLink)
        elif request.method == "POST":
            linkoriginal = request.form.get("Link")
            linkAcortado = request.form.get("Acortado")
            enlaceModel.actualizarEnlace(linkoriginal,linkAcortado,id)
            return redirect(url_for("listarEnlaces"))

