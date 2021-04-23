from src.config.db import mysql


class EnlaceModel():
    def crearUrl(self,urls,enlacecorto,usuario):
        cursor = mysql.get_db().cursor()
        cursor.execute('insert into links(name_link, linkcorto,iduser) values (%s,%s,%s)',(urls,enlacecorto,usuario))
        mysql.get_db().commit()
        cursor.close()
    def find_link(self,link):
        cursor = mysql.get_db().cursor()
        cursor.execute('USE urls')
        cursor.execute('SELECT name_link from links where links.linkcorto = %s ',(link))
        islink = cursor.fetchone()
        mysql.get_db().commit()
        cursor.close()
        print(islink,link)
        return islink
    def find_iduser(self, usuario):
        cursor = mysql.get_db().cursor()
        cursor.execute("select idusuario from usuario where correo = %s",(usuario))
        idusuario = cursor.fetchone()
        mysql.get_db().commit()
        cursor.close()
        return idusuario  
    def listarEnlace(self, usuario):
        cursor = mysql.get_db().cursor()
        cursor.execute("select * from links,usuario where links.iduser=usuario.idusuario and usuario.correo= %s",(usuario))
        listaEnlace = cursor.fetchall()
        mysql.get_db().commit()
        cursor.close()
        print(listaEnlace)
        return listaEnlace

    def eliminarEnlace(self,id):
        cursor = mysql.get_db().cursor()
        cursor.execute("delete   from links where links.idlinks=%s",(id))
        mysql.get_db().commit()
        cursor.close()
    def verEnlaceuser(self,id):
        cursor = mysql.get_db().cursor()
        cursor.execute("select  * from links where links.idlinks=%s",(id))
        link = cursor.fetchall()
        mysql.get_db().commit()
        cursor.close()
        return link

    def actualizarEnlace(self,original,corto,id):
        cursor = mysql.get_db().cursor()
        cursor.execute("update links set name_link= %s,linkcorto=%s where links.idlinks=%s",(original,corto,id,))
        link = cursor.fetchall()
        mysql.get_db().commit()
        cursor.close()