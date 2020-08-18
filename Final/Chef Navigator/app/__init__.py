import flask
import flask_sqlalchemy
import flask_migrate
import flask_login
import os



basedir = os.path.abspath(os.path.dirname(__file__))

app = flask.Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "app.db")


db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

login_mgr = flask_login.LoginManager(app)

app.config['SECRET_KEY'] = 'raiksdafciaewsbnrifdanjneqw'

from. import views, models