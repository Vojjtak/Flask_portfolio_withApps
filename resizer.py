import tkinter as tk
import tkinter.filedialog
import cv2
from PIL import Image
import os


def choose_image():
    image_path = tk.filedialog.askopenfilename()
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