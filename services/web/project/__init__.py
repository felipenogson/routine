import logging
import os
import praw
from werkzeug.utils import secure_filename
from flask import Flask, jsonify, send_from_directory, request, redirect, url_for, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_mail import Mail, Message


app = Flask(__name__)
app.config.from_object("project.config.Config")
mail = Mail(app)
db = SQLAlchemy(app)
CORS(app)
from project.blueprints.routine import routine

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email


app.register_blueprint(routine, url_prefix='/routine')


@app.route("/")
def index():
    return redirect(url_for('routine.index'))
#    """ Default route """
#    app.logger.debug('this is a DEBUG message')
#    app.logger.info('this is a INFO  message')
#    app.logger.warning('this is a WARNING message')
#    app.logger.error('this is a ERROR message')
#    app.logger.critical('this is a CRITICAL message')
#    return render_template('index.html', name="Home")


@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config['STATIC_FOLDER'], filename)


@app.route("/media/<path:filename>")
def mediafile(filename):
    return send_from_directory(app.config['MEDIA_FOLDER'], filename)


@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['MEDIA_FOLDER'], filename))
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Upload a file</title>
        </head>
        <body>
        <form action="" method=post enctype=multipart/form-data>
            <p><input type=file name=file><input type="submit" value="upload"></p>
        </form>
        </body>
        </html>
        """
