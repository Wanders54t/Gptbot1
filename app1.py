from flask import Flask

import os

app = Flask(__name__)

@app.route("/")

def hello():

    return "Hello, world!"

app.run(port=int(os.environ.get("PORT", 5000)))
