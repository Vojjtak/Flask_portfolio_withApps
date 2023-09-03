import tkinter as tk
import tkinter.filedialog
import cv2
from PIL import Image
import os
from flask import Blueprint, render_template, request, jsonify

resizer = Blueprint("resizer", __name__)

@resizer.route("/imageresizer")
def img_resizer():
    return render_template("apps/imageresizer.html")

@resizer.route("/get_img_path", methods=['POST'])
def img_path():
    if request.method == "POST":
        image_name = choose_image()
        return jsonify({'image_name': image_name})


def choose_image():
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    image_path = tk.filedialog.askopenfilename(parent=root)
    name = os.path.split(image_path)
    img = Image.open(image_path)
    img.save(f"website/static/temp/{name[1]}")
    return name[1]


def resize_image(width, height, image):
    img_to_resize = cv2.imread(image)
    resized_image = cv2.resize(img_to_resize, (width, height))
    return resized_image


def save_image(resized_image):
    type = "jpg"
    save_dir = tkinter.filedialog.asksaveasfilename(defaultextension=type)
    cv2.imwrite(save_dir, resized_image)


if __name__ == "__main__":
    choose_image()