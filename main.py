import tkinter
import customtkinter
from pytube import YouTube


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

link = customtkinter.CTkEntry(app, width=350, height=40)
link.pack()

# run app

app.mainloop()