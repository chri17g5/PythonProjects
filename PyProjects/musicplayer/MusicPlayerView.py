from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog

#----VIEW----
#   Window root
root=Tk()
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

#   Play button
play_button=Button(root, text="Play", width=7, command=Play)
play_button['font']=defined_font
play_button.grid(row=1, column=0)

#   Pause button
pause_button=Button(root, text="Pause", width=7, command=Pause)
pause_button['font']=defined_font
pause_button.grid(row=1, column=1)

#   Stop button
stop_button=Button(root, text="Stop", width=7, command=Stop)
stop_button['font']=defined_font
stop_button.grid(row=1, column=2)

#   Resume button
resume_button=Button(root, text="Resume", width=7, command=Resume)
resume_button['font']=defined_font
resume_button.grid(row=1, column=3)

#   Previous button
previous_button=Button(root, text="Previous", width=7, command=Previous)
previous_button['font']=defined_font
previous_button.grid(row=1, column=4)

#   Next button
next_button=Button(root, text="Next", width=7, command=Next)
next_button['font']=defined_font
next_button.grid(row=1, column=5)

#   Menu
my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=add_song_menu)
add_song_menu.add_command(label="Add songs", command=addsons)
add_song_menu.add_command(label="Delete song", command=deletesong)