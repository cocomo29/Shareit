from ast import Return
from flask import Flask

def createApp():
    app = Flask(__name__)
    
    #gota change this when deploying
    app.config['SECRET_KEY'] = "!&@#$C0C0M0^~*7WEN7YN1N3_{./"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app