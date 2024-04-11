from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""
Initializes the Flask application and configures it to use SQLAlchemy with an SQLite database.
- `SQLALCHEMY_DATABASE_URI` specifies the path to the SQLite database file.
- `SQLALCHEMY_TRACK_MODIFICATIONS` is set to False to disable Flask-SQLAlchemy event system.
"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'
db = SQLAlchemy(app)
