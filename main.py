from flask import Flask, redirect, url_for, render_template, request, jsonify
import downloader
from downloader import *
import json


app = Flask(__name__, template_folder='website/templates',
            static_folder='website/static')

app.jinja_env.autoescape = True

@app.route("/")
def home():
    return render_template('index.html')


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
def search():
    if request.method == "POST":
        video = YouTube(request.form["url"])
        title = video.title
        url = request.form["url"]
        thumbnail = video.thumbnail_url
        return render_template("downloader.html", url=url, title=title, thumbnail=thumbnail)
    else:
        return render_template("downloader.html")

@app.route('/get_title', methods=['POST'])
def get_title_and_thumbnail():
    if request.method == "POST":
        video = YouTube(request.form["url"])
        title = video.title
        thumbnail = video.thumbnail_url
        return jsonify({'title': title, 'thumbnail': thumbnail})




if __name__ == "__main__":
    app.run(debug=True)
