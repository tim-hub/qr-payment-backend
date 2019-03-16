import os
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = FlaskAPI(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

from api import *


if __name__ == '__main__':
    app.run()
