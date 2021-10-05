from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog

#----VIEW----
#   Window root
root=TK()
root.title('DataFlair Python MP3 Music player App')

#   Initialize mixer
mixer.init()

#   List box that contains songs
songs_list=Listbox(root,
                   selectmode=SINGLE,
                   bg="black",
                   fg="white",
                   font=('arial',15),
                   height=12,
                   width=47,
                   selectbackground="grey",
                   selectforeground="black")
songs_list.grid(columnspan=9)

#   Button font
defined_font = font.Font(family='Helvetica')

#   Play Button
play_button=Button(root, text="Play", width=7, command=Play)