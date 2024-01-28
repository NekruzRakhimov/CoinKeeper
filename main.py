from flask import Flask
from routes import app as routes_app
from models import Base
from connection import engine

Base.metadata.create_all(bind=engine)

# Create app
app = Flask(__name__)
app.register_blueprint(routes_app)


# Run if Point of entry
if __name__ == '__main__':
    app.run(debug=True, port=7000)
