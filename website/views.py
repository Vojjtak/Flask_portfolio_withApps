from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/about_me")
def about_me():
    return render_template("about-me.html")

@views.route("/contact")
def contact():
    return render_template("contact.html")