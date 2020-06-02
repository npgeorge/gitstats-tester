import os
from dotenv import load_dotenv
from flask import Flask, Blueprint, jsonify, request, render_template, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# import database models.py to link class tables
#from git_app.models import db, migrate, User, Repos
# import my_routes from routes.py
#from git_app.routes import my_routes

#rearranging for heroku
from routes import my_routes
from models import db, migrate, User, Repos

load_dotenv()

# database url as an environment variable
DATABASE_URL = os.getenv("DATABASE_URL", default="OOPS")

#tried this for heroku deploy, didn't work
#app = Flask(__name__)

def create_app():

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # importing models.py database class tables
    # links to __init__file which calls on create app to run
    db.init_app(app)
    migrate.init_app(app, db)
    
    # linking to routes.py page via my_routes variable
    app.register_blueprint(my_routes)

    return app

app = create_app()

if __name__ =="__main__":
    app.run_server(debug=True)