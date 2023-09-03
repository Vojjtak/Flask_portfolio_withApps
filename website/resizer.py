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
def choose_image():
    if request.method == "POST":
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        image_path = tk.filedialog.askopenfilename(parent=root)
        name = os.path.split(image_path)
        img = Image.open(image_path)
        img.save(f"website/static/temp/{name[1]}")
        image_name = name[1]
        im = cv2.imread(f"website/static/temp/{name[1]}")
        width = im.shape[1]
        height = im.shape[0]
        return jsonify({'image_name': image_name, 'width': width, 'height': height})


@resizer.route("/save_image", methods=['POST'])
def resize_image():
    if request.method == 'POST':
        image = request.args.get("neco")
        print(image)
        width = request.form.get("width")
        print(width)
        height = request.form["height"]
        print(height)
        img_to_resize = cv2.imread(image)
        resized_image = cv2.resize(img_to_resize, (width, height))
        type = "jpg"
        save_dir = tkinter.filedialog.asksaveasfilename(defaultextension=type)
        cv2.imwrite(save_dir, resized_image)
        save_confirmation = "Your image was saved."
        return jsonify({'save_confirmation': save_confirmation})



if __name__ == "__main__":
    pass