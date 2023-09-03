from flask import Blueprint, render_template

excelarts = Blueprint("excelarts", __name__)


@excelarts.route("/excelart")
def excelart():
    return render_template("apps/excel_art.html")
