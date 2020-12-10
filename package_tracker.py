from flask import Flask
from app.config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

@app.route("/")
def root():
    return "<h1>Package Tracker</h1>"
