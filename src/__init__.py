from flask import Flask, render_template
import os
app = Flask(__name__, template_folder= 'views')
app.secret_key ="crack"
#importar los controllers
from src.controllers import *

def create_app():
    app.run(debug=True, port=5000)