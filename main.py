import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def health():
    return "ok...", 200


@app.route("/crash")
def crash():
    os._exit(1)