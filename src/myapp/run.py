"""Main file to run flask application."""

from src.myapp.presentation.flask_app.app import create_app

if __name__ == "__main__":
    app = create_app()
