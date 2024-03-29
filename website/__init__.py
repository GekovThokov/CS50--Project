from flask import Flask  

def create_app():
    app = Flask(__name__)
    app.config["SECRET KEY"] = "ASDF432AJSD234NLJK45"
    
    from .views import views
    from .authentication import authentication

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(authentication, url_prefix='/')

    return app