from src import app, db
from src.models import Note
from src.controllers import *

def setup_database(app):
    """
    Ensure the database tables are created.
    """
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    """
    Starts the Flask application and creates the necessary database tables.
    """
    setup_database(app)  # Set up the database within the app context
    app.run(debug=True, host='0.0.0.0', port=5000)
