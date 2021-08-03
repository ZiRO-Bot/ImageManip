import imagemanip
import requests

from flask import Flask, request, Response


app = Flask(__name__)


ENABLED_SYMBOLS = ("true", "t", "yes", "y", "on", "1")
DISABLED_SYMBOLS = ("false", "f", "no", "n", "off", "0")


@app.route("/")
def index():
    return "Hello World"


def manipulate(img_url: str, manip_type: str, **kwargs):
    req = requests.get(str(img_url))
    img_bytes = req.content
    return getattr(imagemanip, manip_type)(img_bytes, **kwargs)


@app.route("/invert", methods=["GET"])
def invert():
    _url = request.args.get("url")
    if _url is None:
        return "Where's the image? D:<"

    return Response(
        response=manipulate(_url, "invert"),
        headers={"Content-Type": "image/png"},
    )


@app.route("/red", methods=["GET"])
def red():
    _url = request.args.get("url")
    if _url is None:
        return "Where's the image? D:<"

    return Response(
        response=manipulate(_url, "red"),
        headers={"Content-Type": "image/png"},
    )


@app.route("/polaroid", methods=["GET"])
def polaroid():
    _url = request.args.get("url")
    fixed = request.args.get("fixed", "false")
    is_fixed = True
    if fixed.lower() in ENABLED_SYMBOLS:
        is_fixed = True
    if fixed.lower() in DISABLED_SYMBOLS:
        is_fixed = False

    if _url is None:
        return "Where's the image? D:<"

    return Response(
        response=manipulate(_url, "polaroid", fixed=is_fixed),
        headers={"Content-Type": "image/png"},
    )


@app.route("/sad", methods=["GET"])
def sad():
    _url = request.args.get("url")
    if _url is None:
        return "Where's the image? D:<"

    return Response(
        response=manipulate(_url, "polaroid"),
        headers={"Content-Type": "image/png"},
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
