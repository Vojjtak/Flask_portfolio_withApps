from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = "abcdefg"

    from .views import views
    from .auth import auth
    from .contact import contact
    from .downloader import downloader
    from .excelart import excelarts

    app.register_blueprint(views, url_preflix='/')
    app.register_blueprint(auth, url_preflix='/')
    app.register_blueprint(contact, url_preflix='/')
    app.register_blueprint(downloader, url_preflix='/')
    app.register_blueprint(excelarts, url_preflix='/')

    return app

