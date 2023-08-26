import tkinter as tk
import tkinter.filedialog
from pytube import YouTube
import sqlite3


def data_save(url):
    video = YouTube(url)
    title = video.title
    db = (title, url)
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("insert into downloads values (?,?)", db)
    connection.commit()
    connection.close()


def data():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    selection = cursor.execute('SELECT * FROM downloads')
    list = []
    for i in selection:
        list.append(i)
    return list


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
    data()
