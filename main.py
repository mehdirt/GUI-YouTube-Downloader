import tkinter as tk
import customtkinter
from pytube import YouTube
from pytube.exceptions import RegexMatchError
from urllib.error import URLError

def start_download():
    state_label.configure(text="Donwloading...")
    try:
        # Creating YouTube object by the given link
        yt_link = link.get()
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        video = yt_object.streams.get_highest_resolution()
        # Showing the title of the video
        title.configure(text=yt_object.title, text_color='white')
        # Downloading the video
        video.download()
    except URLError:
        state_label.configure(text="Connection Error Occured!", text_color="red")
        
    except RegexMatchError:
        state_label.configure(text="YouTube link is invalid!", text_color="red")
        
    else:
        state_label.configure(text="Download Completed Successfully!", text_color="green")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_compeletion = int(bytes_downloaded / total_size * 100)
    progress_bar.configure(text=str(percentage_of_compeletion) + '%')
    progress_bar.set(percentage_of_compeletion / 100)

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

# State Label
state_label = customtkinter.CTkLabel(app, text="")
state_label.pack()

# Progress Bar
progress_bar = customtkinter.CTkProgressBar(app, progress_color='blue')
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=start_download)
download.pack(padx=10, pady=10)

#Run App
app.mainloop()