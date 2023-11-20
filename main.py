import tkinter as tk
import customtkinter
from pytube import YouTube

def start_download():
    print("Donwloading...")
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link)
        video = yt_object.streams.get_highest_resolution()
        video.download()
    except Exception as err:
        print("YouTube link is invalid!")
        print(err)
    else:
        print("Download Completed Successfully!")

# System Setting
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Adding UI Elements
# Title
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

# Link input 
url = tk.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url)
link.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=start_download)
download.pack(padx=10, pady=10)

#Run App
app.mainloop()