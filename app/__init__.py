from flask import Flask

app = Flask(__name__) 

with app.app_context():
        from . import routes #importando as rotas no contexto da aplicação