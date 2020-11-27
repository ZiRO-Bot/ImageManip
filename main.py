import imagemanip
import requests

from flask import Flask, request, Response
from io import BytesIO

app = Flask(__name__)

@app.route("/ping")
def pong():
  return "pong!"

@app.route('/')
def index():
    return 'Hello World'

@app.route("/invert", methods=["GET"])
def invert():
    _url = request.args.get("url")
    test = requests.get(str(_url))
    src = test.content
    img = imagemanip.invert(src)
    return Response(response=img, headers={"Content-Type": "image/png"})

@app.route("/red", methods=["GET"])
def red():
    _url = request.args.get("url")
    test = requests.get(str(_url))
    src = test.content
    img = imagemanip.red(src)
    return Response(response=img, headers={"Content-Type": "image/png"})

app.run(debug = True)