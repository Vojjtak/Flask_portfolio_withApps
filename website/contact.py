from flask import Blueprint, render_template, request, jsonify
import ssl
from email.message import EmailMessage
from emailing import PASSWORD, RECEIVER, SENDER
import smtplib


contact = Blueprint("contact", __name__)


@contact.route("/contact_sent", methods=["POST", "GET"])
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
