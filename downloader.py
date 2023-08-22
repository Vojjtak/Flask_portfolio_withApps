import tkinter as tk
import tkinter.filedialog
from pytube import YouTube


class DownloadVideo:
    def __init__(self):
        self.directory = tk.filedialog.askdirectory()

    def get_title(self):
        video = YouTube(self.url)
        title = video.title
        print(title)

    def acces(self):
        agreement = input("Is this title of your video? ")
        return agreement

    def download(self, url):
        video = YouTube(url)
        my_video = video.streams.get_highest_resolution()
        my_video.download(output_path=(str(self.directory)))




if __name__ == "__main__":
    dwn = DownloadVideo()
    dwn.get_title()
    if dwn.acces() == "yes":
        dwn.download()
    else:
        print("zkus to znovu")
        pass