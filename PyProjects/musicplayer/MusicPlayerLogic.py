from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog

from MusicPlayerView import songs_list 

"""         
------------NOTES------------

Maby a global parameter
would help out

-----------------------------
"""

#   Add many songs to the playlist of python mp3 player
def addsongs():
    #   Open file
    temp_song=filedialog.askopenfilenames(initialdir="Music/", 
                                          title="Chose a song", 
                                          filetypes=(("mp3 Files", "*.mp3"),))
    #   Loop trough every item in the list then insert into into a listbox
    for s in temp_song:
        s=s.replace("C:/Users/DataFlair/python-mp3-music-player/","")
    songs_list.insert(END, s)

#   Delets song
def deletesong():
    curr_song=songs_list.curselection()
    songs_list.delete(curr_song[0])

#   Plays song
def Play():
    song=songs_list.get(ACTIVE)
    song=f'C:/Users/lenovo/Desktop/DataFlair/Notepad/Music/{song}'
    mixer.music.load(song)
    mixer.music.play()

#   Pause song
def Pause():
    mixer.music.pause()

#   Stops song
def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

#   Resumes song
def Resume():
    mixer.music.unpause()

#   Function to navigate from current song
def Previous():
    #   Selected song index
    previous_one=songs_list.curselecton()
    #   Previous song index
    previous_one=previous_one[0]-1
    #   Gets the previous song
    temp2=songs_list.get(previous_one)
    temp2=f'C:/Users/DataFlair/python-mp3-music-player/{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    #   Active new song
    songs_list.activate(previous_one)
    #   Next song set
    songs_list.selection_set(previous_one)

#   Next song in list
def Next():
    #   Get selected song index
    next_one=songs_list.curselection()
    #   Get the next song index
    next_one=next_one[0]+1
    #   Gets the next song
    temp2=songs_list.get(next_one)
    temp2=f'C:/Users/DataFlair/python-mp3-music-player/{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    #   Activate new song
    songs_list.activate(next_one)
    #   Set the next song
    songs_list.selection_get(next_one)

