from flask import Flask, redirect, url_for, render_template, request

import downloader
from downloader import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about_me")
def aboutme():
    return render_template("about-me.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/downloader", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        downloader.DownloadVideo().download(request.form["url"])
        return render_template("/apps/downloader.html")
    else:
        return render_template("/apps/downloader.html")


def download(video):
    dwnld = downloader.DownloadVideo.download(video)
    return dwnld


if __name__ == "__main__":
    app.run(debug=True)
