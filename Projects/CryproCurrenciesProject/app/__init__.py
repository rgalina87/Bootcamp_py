import flask
import flask_sqlalchemy
import flask_migrate
import os
import flask_login


basedir = os.path.abspath(os.path.dirname(__file__))

app = flask.Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "app.db")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = flask_sqlalchemy.SQLAlchemy(app)

migrate = flask_migrate.Migrate(app, db)

login_mgr = flask_login.LoginManager(app)

app.config['SECRET_KEY'] = "arandomsecretkey"


from . import views, models