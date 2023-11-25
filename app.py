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

def browse_directory():
    download_path = customtkinter.filedialog.askdirectory()
    entry_path.delete(0, customtkinter.END)  # Clear previous entry
    entry_path.insert(0, download_path)

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

# Input wrapper:
input_wrapper = customtkinter.CTkFrame(app, width=450, height=450, fg_color="transparent")
input_wrapper.pack()

# URL_wrapper
URL_wrapper = customtkinter.CTkFrame(input_wrapper, fg_color="transparent")
URL_wrapper.pack()

# YouTube Link input 
link_label = customtkinter.CTkLabel(URL_wrapper, text="YouTube URL:")
link_label.pack(padx=15, side=customtkinter.LEFT)

url = customtkinter.StringVar()
link = customtkinter.CTkEntry(URL_wrapper, width=250, height=20, textvariable=url)
link.pack(side=customtkinter.RIGHT)

# Donwload path wrapper
download_path_wrapper = customtkinter.CTkFrame(input_wrapper, fg_color="transparent")
download_path_wrapper.pack()

# Download Path input
path_label = customtkinter.CTkLabel(download_path_wrapper, text="Download Path:")
path_label.pack(padx=15, side=customtkinter.LEFT)

entry_path = customtkinter.CTkEntry(download_path_wrapper, width=195, height=20)
entry_path.pack(pady=10, side=customtkinter.LEFT)

button_browse = customtkinter.CTkButton(download_path_wrapper, width=15, text="Browse", command=browse_directory)
button_browse.pack(padx=10, side=customtkinter.RIGHT)

# State Label
state_label = customtkinter.CTkLabel(app, text="")
state_label.pack(pady=5)

# Download Button
download_btn = customtkinter.CTkButton(app, text="Download", width=150, height=35, command=start_download)
download_btn.pack(padx=20, pady=20)

# Progress Bar
progress_bar = customtkinter.CTkProgressBar(app, progress_color='blue', width=500, height=15)
progress_bar.set(0)
progress_bar.pack(padx=15, pady=15)

# Option Menu
option = customtkinter.StringVar(value="480p")
option_menu = customtkinter.CTkOptionMenu(app,values=['144p', '240p', '360p','480p', '720p'], variable=option)
option_menu.pack(pady=5)

#Run App
app.mainloop()