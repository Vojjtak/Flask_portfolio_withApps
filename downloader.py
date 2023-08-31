import tkinter as tk
import tkinter.filedialog
from pytube import YouTube
import sqlite3
import datetime


def data_save(url):
    video = YouTube(url)
    title = video.title
    date = datetime.datetime.now()
    db = (title, url, date)
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO downloads VALUES (?,?,?)", db)
    connection.commit()
    connection.close()

def data_date():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    selection = cursor.execute('SELECT date FROM downloads ORDER BY date DESC LIMIT 10')
    selection = selection.fetchall()
    list = []
    for date in selection:
        string = ''.join(date)
        list.append(string)
    return list


def data_title():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    selection = cursor.execute('SELECT title FROM downloads ORDER BY date DESC LIMIT 10')
    selection = selection.fetchall()
    list = []
    for title in selection:
        string = ''.join(title)
        list.append(string)
    return list


def data_url():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    selection = cursor.execute('SELECT url FROM downloads ORDER BY date DESC LIMIT 10')
    selection = selection.fetchall()
    list = []
    for title in selection:
        string = ''.join(title)
        list.append(string)
    return list


class DownloadVideo:
    def __init__(self):
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        self.directory = tk.filedialog.askdirectory(parent=root)

    def download(self, video):
        my_video = video.streams.get_highest_resolution()
        my_video.download(output_path=(str(self.directory)))


if __name__ == "__main__":
    pass
