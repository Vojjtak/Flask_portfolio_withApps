from flask import Flask, render_template, request, jsonify
from downloader import *
import smtplib
from email.message import EmailMessage
from emailing import PASSWORD, RECEIVER, SENDER
import ssl
import resizer
from bs4 import BeautifulSoup


app = Flask(__name__, template_folder='website/templates',
            static_folder='website/static')

# HOME #
@app.route("/")
def home():
    return render_template('index.html')

# ABOUT ME #
@app.route("/about_me")
def about():
    return render_template("about-me.html")

# CONTACT #
@app.route("/contact", methods=["POST", "GET"])
def contact():
    return render_template("contact.html")

@app.route("/contact_sent", methods=["POST", "GET"])
def send_email():

    if request.method == "POST":
        print(request.form)
        try:
            context = ssl.create_default_context()
            message = request.form["messageinput"]

            email_message = EmailMessage()
            email_message['Subject'] = request.form["nameinput"]
            email_message.set_content(message)

            gmail = smtplib.SMTP("smtp.gmail.com", 587)
            gmail.starttls(context=context)
            gmail.login(SENDER, PASSWORD)
            gmail.sendmail(request.form["nameinput"], RECEIVER, email_message.as_string())
            gmail.quit()

            sent = "Thank you for your message!"
            return jsonify({'sent': sent})
        except Exception as e:
            return jsonify({'error': str(e)})


# VIDEO DOWNLOADER YTB #
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

# IMAGE RESIZER #
@app.route("/imageresizer")
def img_res():
    return render_template("/apps/imageresizer.html")


@app.route("/get_img_path", methods=['POST', 'GET'])
def img_path():
    if request.method == "POST":
        image_name = resizer.choose_image()
        print(request.form.get("sliderValue"))
        return jsonify({'image_name': image_name})



# EXCEL ART #

@app.route("/excelart")
def excel_art():
    return render_template("apps/excel_art.html")


if __name__ == "__main__":
    app.run(debug=True)
