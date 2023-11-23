from pytube import YouTube
from pytube.exceptions import RegexMatchError
from urllib.error import URLError
import customtkinter

def start_download() -> None:
    """Start downloading YouTube video by given link"""
    state_label.configure(text="Donwloading...", text_color='white')
    try:
        # Creating YouTube object by the given link
        yt_link = link.get()
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        video = yt_object.streams.get_by_resolution(option_menu.get())
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

def on_progress(stream, chunk, bytes_remaining) -> None:
    """Calculates the progress and sets the progress bar"""
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
app.geometry("800x600")
app.title("YouTube Downloader")

# Adding UI Elements
# Title
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=20, pady=20)

# Link input 
url = customtkinter.StringVar()
link = customtkinter.CTkEntry(app, width=450, height=40, textvariable=url)
link.pack()

# State Label
state_label = customtkinter.CTkLabel(app, text="")
state_label.pack(pady=5)

# Progress Bar
progress_bar = customtkinter.CTkProgressBar(app, progress_color='blue', width=500, height=15)
progress_bar.set(0)
progress_bar.pack(padx=15, pady=15)

# Option Menu
option = customtkinter.StringVar(value="480p")
option_menu = customtkinter.CTkOptionMenu(app,values=['144p', '240p', '360p','480', '720p'], variable=option)
option_menu.pack(pady=5)

# Download Button
download_btn = customtkinter.CTkButton(app, text="Download", width=150, height=35, command=start_download)
download_btn.pack(padx=20, pady=20)

#Run App
app.mainloop()