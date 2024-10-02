from flask import Flask
from flask_cors import CORS
from routes import book_routes
from config import DevelopmentConfig


app = Flask(__name__)
CORS(app)

# Register the blueprints
app.register_blueprint(book_routes)

app.config.from_object(DevelopmentConfig)


if __name__ == "__main__":
    app.run()
