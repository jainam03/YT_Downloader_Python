from asyncio import StreamReader
import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!")
    except:
        finishLabel.configure(text="Download Error!",text_color="red")
        
def on_progress(streams, chunck, bytes_remaining):
    total_size = StreamReader.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()
    
    # update progres bar
    progressBar.set(float(percentage_of_completion) / 100)
    

# system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube downloader")

# adding UI elements
title = customtkinter.CTkLabel(app,text="Insert a YouTube link")
title.pack(padx=10,pady=10)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# finished download
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# progress percentage
pPercentage = customtkinter.CTkLabel(app,text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app,width=400)
progressBar.set(0.5)
progressBar.pack(padx=10,pady=10)

# download button
download = customtkinter.CTkButton(app,text="Download",command=startDownload)
download.pack(padx=10,pady=10)

# run app
app.mainloop()