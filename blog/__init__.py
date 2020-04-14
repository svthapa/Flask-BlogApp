from flask import Flask
from .blog import mysql
from .blog import upload_folder

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'secretkey435273'
    app.config['DEBUG'] = True
    app.config['IMAGE_UPLOADS'] = upload_folder
    app.config['MYSQL_DATABASE_HOST'] = 'us-cdbr-iron-east-01.cleardb.net'
    app.config['MYSQL_DATABASE_USER'] = 'b6be13d48336cb'
    app.config['MYSQL_DATABASE_PASSWORD'] = '21c36705'
    app.config['MYSQL_DATABASE_DB'] = 'heroku_442bfb3107ad0c4'
    app.config['MYSQL_DATABASE_CURSOR'] ='DictCursor'
    mysql.init_app(app)

    from .blog import bp
    app.register_blueprint(bp)

    return app
