import flask
import flask_sqlalchemy
import flask_migrate
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = flask.Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "app.db")
db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

app.config['SECRET_KEY'] = "arandomsecretkey"


from . import views, models

#from Week_13.Day_1.W13_D1_DC.ex import views, models #(no module ex)
#from ex import views, models #(no module ex)

