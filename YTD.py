from tkinter import *
from pytube import YouTube

root = Tk()
root.title('YouTube Downloader')
root.geometry('250x100')
root.columnconfigure(0, weight=1)
Label(root, text='YouTube Video Downloader', font='arial 15 bold').pack(side=TOP, pady=10)
root.resizable(True, True)
link = StringVar()
Label(root, text='Paste Link Here:', font='arial 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)


def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)


Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2, command=downloader).place(x=180, y=150)
root.mainloop()
