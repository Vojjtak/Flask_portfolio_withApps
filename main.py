from flask import Flask, render_template, request, jsonify


from downloader import *
from downloader import data_save, data

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
    return render_template("apps/downloader.html")

#title, thumbnail
@app.route('/get_title', methods=['POST'])
def get_title_and_thumbnail():
    if request.method == "POST":
        video = YouTube(request.form["url"])
        title = video.title
        thumbnail = video.thumbnail_url
        data_txt = data()
        print(data_txt)
        return jsonify({'title': title, 'thumbnail': thumbnail, 'data': data_txt})

#stáhnout
@app.route('/download', methods=['POST'])
def download():
    if request.method == "POST":
        url = YouTube(request.form["url"])
        video = DownloadVideo().download(url)
#uložit do databáze stáhnutých
        data_save(request.form["url"])
        data_txt = data()
        return jsonify({'video': video, 'data': data_txt})

@app.route('/data', methods=['GET'])
def video_data():
    if request.method == "GET":
        data_of_video = data()
        return jsonify({'data_of_video': data_of_video})

if __name__ == "__main__":
    app.run(debug=True)
