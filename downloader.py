import tkinter as tk
import tkinter.filedialog
from pytube import YouTube


class DownloadVideo:
    def __init__(self):
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        self.directory = tk.filedialog.askdirectory(parent=root)

    def get_title(self, url):
        video = YouTube(url)
        title = video.title

    def download(self, video):
        my_video = video.streams.get_highest_resolution()
        my_video.download(output_path=(str(self.directory)))


if __name__ == "__main__":
    dwn = DownloadVideo()
    dwn.download()
