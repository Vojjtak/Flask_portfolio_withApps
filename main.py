from flask import Flask, render_template, request, jsonify
from downloader import *
import smtplib
from emailing import ssl, PASSWORD
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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


@app.route("/contact_sent", methods=["POST", "GET"])
def send_email():
    if request.method == "POST":
        context = ssl.create_default_context()
        SENDER = "einexwow@gmail.com"
        RECEIVER = "vodos@seznam.cz"

        email_message = MIMEMultipart()
        email_message['From'] = SENDER
        email_message['To'] = RECEIVER
        email_message['Subject'] = "ahoj"

        email_message.attach(MIMEText("ahoj", 'plain'))

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls(context=context)
            smtp.login(SENDER, PASSWORD)
            smtp.sendmail(SENDER, "vodos@seznam.cz", email_message.as_string())
            sent = "Thank you for your message!"
            return jsonify({'sent': sent})


if __name__ == '__main__':
    app.run()


@app.route("/downloader", methods=["POST", "GET"])
def search():
    title_display = data_title()
    url_display = data_url()
    date_display = data_date()
    return render_template("apps/downloader.html",
                           title_display=title_display,
                           url_display=url_display,
                           date_display=date_display)


# title, thumbnail
@app.route('/get_title', methods=['POST'])
def get_title_and_thumbnail():
    if request.method == "POST":
        video = YouTube(request.form["url"])
        title = video.title
        thumbnail = video.thumbnail_url
        return jsonify({'title': title, 'thumbnail': thumbnail})


# download
@app.route('/download', methods=['POST'])
def download():
    if request.method == "POST":
        url = YouTube(request.form["url"])
        video = DownloadVideo().download(url)
        # save to downloads database
        data_save(request.form["url"])
        return jsonify({'video': video})


if __name__ == "__main__":
    app.run(debug=True)
    send_email()
