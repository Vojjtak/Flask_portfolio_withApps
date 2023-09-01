from website import create_app
from flask import Flask, render_template, request, jsonify
from downloader import *
import smtplib
from email.message import EmailMessage
from emailing import PASSWORD, RECEIVER, SENDER
import ssl
import resizer
from bs4 import BeautifulSoup


app = create_app()



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
