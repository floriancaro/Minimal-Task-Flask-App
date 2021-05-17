from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8u3rouhfkjdsfiluh'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

# We cannot import routes before creating our Flask app and the corresponding db since the routes.py script refers back to those instances

from routes import *

# the variable __name__ is automatically set to "__main__" when the .py script is run
if __name__ == '__main__':
    app.run(debug=True)
