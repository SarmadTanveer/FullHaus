from flask import Flask

app = Flask(__name__)

app.config['AllowedExt'] = ['jpg','png']

from app.routes import routes

if __name__ == '__main__':
  app.run(port=3000)