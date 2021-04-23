from flaskext.mysql import MySQL
from src import app
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'flask-db' 
app.config['MYSQL_DATABASE_USER'] = 'root' 
app.config['MYSQL_DATABASE_PASSWORD'] = 'ediJM26' 
app.config['MYSQL_DATABASE_DB'] = 'urls' 
mysql.init_app(app)
