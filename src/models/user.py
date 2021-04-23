
from src.config.db import mysql

class UsuarioModel():
    def listarUser(self):
        cursor = mysql.get_db().cursor()
        cursor.execute('select * from usuario')
        usuarios = cursor.fetchall()
        cursor.close()
        return usuarios
    def crearUser(serlf,usuario,correo,claveEncritada):
        cursor = mysql.get_db().cursor()
        cursor.execute('insert into usuario(nombre,correo,password) values(%s,%s,%s)', (usuario,correo,claveEncritada))
        mysql.get_db().commit()
        cursor.close()
    def update(self,id,nombre,apellido,celular,correo,contrasena):
        cursor = mysql.get_db().cursor()
        cursor.execute('update persona set nombre = %s, apellido = %s, celular = %s,correo = %s, contrasena = %s WHERE idpersona=%s',(nombre,apellido, celular, correo, contrasena, id))
        mysql.get_db().commit()
        cursor.close()
    def delete(self,id):
        cursor = mysql.get_db().cursor()
        cursor.execute('delete from persona where idpersona = %s', (id,))
        mysql.get_db().commit()
        cursor.close()
    def validarUser(self,usuario):
        cursor = mysql.get_db().cursor()
        cursor.execute('select correo, password from usuario where usuario.correo = %s',(usuario,))
        usuario = cursor.fetchall()
        cursor.close()
        return usuario
