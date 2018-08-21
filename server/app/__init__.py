from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .api import api

app = Flask(__name__, static_folder='./dist/static', template_folder='./dist')
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(api, url_prefix="/api/v1")

from app import routes, models
