import tkinter as tk
import tkinter.filedialog
import cv2


def resize_image(width, heigth):
    image = tkinter.filedialog.askopenfilename()
    img_to_resize = cv2.imread(image)
    resized_image = cv2.resize(img_to_resize, (width, heigth))
    type = "jpg"
    save_dir = tkinter.filedialog.asksaveasfilename(defaultextension=type)
    cv2.imwrite(save_dir, resized_image)



if __name__ == "__main__":
    resize_image()