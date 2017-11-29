# app/__init__.py
# coding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#third-party imports
from flask import abort, Flask, render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

#local imports
from config import app_config
import os

#db variable initialization chushihua shuju bianliang
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    if os.getenv('FLASK_CONFIG') == "production":
        app = Flask(__name__)
        app.config.update(
            SECRET_KEY=os.getenv('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
        )
    else:
        app = Flask(__name__, instance_relative_config=True)#为app.config.from_pyfile()查看在instance文件夹的特殊文件
        app.config.from_object(app_config[config_name])#加载内建or自己的配置变量，使用app.config.from_object(),现通过app.config["VAR_NAME"]，我们可以访问到对应的变量
        app.config.from_pyfile('config.py', silent=True)#使用app.config.from_pyfile()可以加载定义在instance文件夹中的配置变量

    Bootstrap(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    migrate = Migrate(app, db)

    from app import models

    #temporary route
    #@app.route('/')
    #def elsa():
    #    return 'Hello, Elsa!'

    from .admin import admin as admin_blueprint#app.register_blueprint means注册蓝图到应用
    app.register_blueprint(admin_blueprint, url_prefix='/admin')#蓝图可以在不同的位置挂载

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)#它们的前缀是蓝图的名称，并且用一个点(.)来分割。

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    #@app.route('/500')   TEST
    #def error():
    #    abort(500)

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html', title='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html', title='Page Not Found'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html', title='Server Error'), 500

    return app
#*****app.config.from_pyfile must have "silent=True", or report error of no file.
