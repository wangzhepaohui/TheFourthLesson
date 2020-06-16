from flask import Flask, render_template, request,escape

from .admin import admin
from .user import user
from .root import root

from werkzeug.utils import redirect
from vsearch import search4letters

app = Flask(__name__)

#注册 ,
app.register_blueprint(root)
app.register_blueprint(admin, urlprefix = '/admin')
app.register_blueprint(user, urlprefix = '/user')

