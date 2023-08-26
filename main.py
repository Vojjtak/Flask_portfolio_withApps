from flask import Flask, redirect, url_for, render_template, request, jsonify

from downloader import *

app = Flask(__name__, template_folder='website/templates',
            static_folder='website/static')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about_me")
def about():
    return render_template("about-me.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/downloader", methods=["POST", "GET"])
def search():
    return render_template("downloader.html")


@app.route('/get_title', methods=['POST'])
def get_title_and_thumbnail():
    if request.method == "POST":
        video = YouTube(request.form["url"])
        title = video.title
        thumbnail = video.thumbnail_url
        return jsonify({'title': title, 'thumbnail': thumbnail})


@app.route('/download', methods=['POST'])
def download():
    if request.method == "POST":
        url = YouTube(request.form["url"])
        video = DownloadVideo().download(url)
        return jsonify({'video': video})


if __name__ == "__main__":
    app.run(debug=True)

