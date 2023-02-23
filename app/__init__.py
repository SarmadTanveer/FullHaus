from flask import Flask

app = Flask(__name__)

app.config['AllowedExt'] = ['jpg','png']

from app.routes import routes