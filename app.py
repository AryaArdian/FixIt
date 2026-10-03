import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from routes.main import main


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-only-change-me")
    app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # max upload 5 MB
    app.register_blueprint(main)
    return app


app = create_app()  # Vercel looks for this `app` object

if __name__ == "__main__":
    app.run(debug=True)
