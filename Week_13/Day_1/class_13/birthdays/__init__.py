import flask
import flask_sqlalchemy
import flask_migrate
import os

# Create a variable called basedir, that contain the path to the ROOT folder
basedir = os.path.abspath( # Gives you the absolute path
                                # Gives you the name of the directory that contains
     os.path.dirname(__file__)  # the current file (which is not __init__.py but
                                # birthdays)
)

app = flask.Flask(__name__)

# First -
# Provide a path (a URL) for the database file --
# the convention wants you to add sqlite:/// at the beginning of the path
# Use os.path.join to create the full path
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "app.db")

# Second -
# Create the db and migrate objects
db      = flask_sqlalchemy.SQLAlchemy(app) # Virtual object that represents the database
migrate = flask_migrate.Migrate(app, db)   # Create migrations --> Modifications on the database structure


app.config['SECRET_KEY'] = "arandomsecretkey"

database_fn = "users.json"

from . import views, models