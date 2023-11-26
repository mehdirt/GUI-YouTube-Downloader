import customtkinter
from pytube import YouTube
from pytube.exceptions import RegexMatchError

from urllib.error import URLError
from PIL import Image
import os

def start_download() -> None:
    """Start downloading YouTube video by given link"""
    state_label.configure(text="Donwloading...", text_color='white')
    try:
        # Creating YouTube object by the given link
        yt_link = link.get()
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        video = yt_object.streams.get_by_resolution(option)
        # Downloading the video
        video.download(entry_path.get())
    except URLError:
        state_label.configure(text="Connection Error Occured!", text_color="red")
        
    except RegexMatchError:
        state_label.configure(text="YouTube link is invalid!", text_color="red")
    
    except Exception:
        state_label.configure(text="Some Error Occured!", text_color="red")
        
    else:
        state_label.configure(text="Download Completed Successfully!", text_color="green")

def on_progress(stream, chunk, bytes_remaining) -> None:
    """Calculates the progress and sets the progress bar"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_compeletion = int(bytes_downloaded / total_size * 100)
    # progress_bar.configure(text=str(percentage_of_compeletion) + '%') # TODO
    progress_bar.set(percentage_of_compeletion / 100)

def browse_directory() -> None:
    """Browse and select a directory"""
    download_path = customtkinter.filedialog.askdirectory()
    entry_path.delete(0, customtkinter.END)  # Clear previous entry
    entry_path.insert(0, download_path)

# System Setting
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("550x475")
app.title("YouTube Downloader")

# Set App Icon
app.iconbitmap("images/YouTube.ico")
# Adding UI Elements
# Title
title = customtkinter.CTkLabel(app, text="GUI YouTube Downloader", font=('Helvetica', 18, 'bold'))
title.pack(pady=25)

# Input wrapper:
input_wrapper = customtkinter.CTkFrame(app, width=500, height=350)
input_wrapper.pack()

    # URL_wrapper
URL_wrapper = customtkinter.CTkFrame(input_wrapper, fg_color="transparent")
URL_wrapper.pack(padx=5, pady=10)

        # YouTube Link input 
link_label = customtkinter.CTkLabel(URL_wrapper,
                                    text="YouTube URL :",
                                    font=('Helvetica', 12, 'bold'))
link_label.pack(padx=15, side=customtkinter.LEFT)

url = customtkinter.StringVar()
link = customtkinter.CTkEntry(URL_wrapper, width=257, height=20, placeholder_text="Enter YouTube URL", textvariable=url)
link.pack(side=customtkinter.RIGHT)

    # Donwload path wrapper
download_path_wrapper = customtkinter.CTkFrame(input_wrapper, fg_color="transparent")
download_path_wrapper.pack(padx=5, pady=10)

        # Download Path input
path_label = customtkinter.CTkLabel(download_path_wrapper,
                                    text="Download Path :",
                                    font=('Helvetica', 12, 'bold'))
path_label.pack(padx=15, side=customtkinter.LEFT)

entry_path = customtkinter.CTkEntry(download_path_wrapper, width=185, height=20, placeholder_text="C:/Users/mehdirt/Downloads")
entry_path.pack(pady=10, side=customtkinter.LEFT)
        # Browse Button
button_browse = customtkinter.CTkButton(download_path_wrapper,
                                        width=15,
                                        text="Browse",
                                        text_color="#252626",
                                        fg_color="#c9d4ce",
                                        hover_color="#b4bfb9",
                                        command=browse_directory)
button_browse.pack(padx=10, side=customtkinter.RIGHT)

# Button wrapper
button_wrapper = customtkinter.CTkFrame(app, width=500, height=10, fg_color="transparent")
button_wrapper.pack()

    # Download Button
download_btn = customtkinter.CTkButton(button_wrapper,
                                       text="Download",
                                       width=100,
                                       height=30,
                                       fg_color='#339e65',
                                       hover_color="#39ad6f",
                                       command=start_download)
download_btn.pack(padx=80, side=customtkinter.RIGHT)

    # Option Menu wrapper
option_menu_wrapper = customtkinter.CTkFrame(button_wrapper, fg_color="transparent")
option_menu_wrapper.pack(padx=80, side=customtkinter.LEFT)

        # Resolution Label
resolution_label = customtkinter.CTkLabel(option_menu_wrapper,
                                          text="Select Resolution:",
                                          font=("Helvetica", 12))
resolution_label.pack()
        # Option Menu
option = customtkinter.StringVar(value="480p")
option_menu = customtkinter.CTkOptionMenu(option_menu_wrapper,
                                          values=['144p', '240p', '360p','480p', '720p'],
                                          width=120,
                                          height=20,
                                          corner_radius=5,
                                          text_color="#252626",
                                          fg_color="#c9d4ce",
                                          dropdown_fg_color="#939695",
                                          dropdown_text_color="#252626",
                                          dropdown_hover_color="#6c736e",
                                          button_color="#78807b",
                                          button_hover_color="#89918c",
                                          variable=option)
option_menu.pack()

# Progress wrapper
progress_wrapper = customtkinter.CTkFrame(app, fg_color="transparent")
progress_wrapper.pack(pady=5)

    # State Label
state_label = customtkinter.CTkLabel(progress_wrapper,
                                     text="",
                                     font=('Helvetica', 14, 'bold'))
state_label.pack(pady=10)

    # Progress Bar
progress_bar = customtkinter.CTkProgressBar(progress_wrapper,
                                            progress_color='#2d8c59',
                                            width=425,
                                            height=10)
progress_bar.set(0)
progress_bar.pack(padx=5, pady=5)

# YouTube Image
image_path = os.path.join(os.path.dirname(__file__), 'images/YouTube_Logo.png')
image = customtkinter.CTkImage(light_image=Image.open(image_path), size=(400, 75))
image_label = customtkinter.CTkLabel(app, image=image, text='')
image_label.pack(pady=30)

#Run App
app.mainloop()