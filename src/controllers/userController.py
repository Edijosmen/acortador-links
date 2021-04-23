from flask import render_template, request, redirect, url_for, jsonify, flash, session
from src import app
from src.models.user import UsuarioModel
import random ,string
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib

@app.before_request
def before_request():
    if 'username' not in session and request.endpoint in ['comment']:
        return redirect(url_for("login"))
    

@app.route('/usuarios', methods=['GET'])
def usuarios():

    usuarioModel = UsuarioModel()
    usuarios = usuarioModel.listarUser()
    #return jsonify({"usuarios":usuarios})
    return render_template('crearUser.html')

@app.route("/usuario/create", methods =['POST','GET'])
def createUser():
    if request.method == 'POST':
        usuarioModel = UsuarioModel()
        usuario = request.form['usuario']
        correo = request.form['email']
        contrasena = request.form['password']
        encriptar = generate_password_hash(contrasena)
        #encriptar = hashlib.md5(contrasena.encode())
        #claveEncritada = encriptar.hexdigest()
        usuarioModel.crearUser(usuario,correo,encriptar) 
        return redirect(url_for("enlaces"))
    else:
        return render_template('crearUser.html')

@app.route("/update/<id>",methods=["PUT"])
def apdate(id):
    usuarioModel = UsuarioModel()
    request_data = request.get_json()
    nombre = request_data['nombre']
    apellido = request_data['apellido']
    celular = request_data['celular']
    correo = request_data['correo']
    contrasena = request_data['contrasena']
    usuarioModel.update(id,nombre,apellido,celular,correo,contrasena)
    return "ok"

@app.route("/delete/<id>",methods=["DELETE"])
def deleteUser(id):
    usuarioModel = UsuarioModel()
    usuarioModel.delete(id)
    return "ok"

@app.route("/login" ,methods =['POST','GET'])
def login():
    usuarioModel = UsuarioModel()
    if request.method == "GET":
        return render_template("login.html")
    else:
        usuario = request.form['email']
        password = request.form['password']
        user = usuarioModel.validarUser(usuario)
        result = validardateuser(user,password)
        if user is not None and result==True:
            #success_message = 'Datos correctos: ¡Bienvenido!'
            #flash(success_message)
            session['username'] = usuario
            return redirect(url_for("enlaces"))
        else:
            print("incorrecto")
            return redirect(url_for("login"))
            #error_menssage = "Datos incorrectos: usuario o contraseña incorrecta"
            #flash(success_message)
        return "ok"
def validardateuser(users,password):
    for user in users:
        return check_password_hash(user[1],password)

@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for("login"))

