from flask import Flask

app = Flask(__name__) 

with app.app_context():
        """
        importando as rotas no contexto da aplicação
        """
        from . import routes