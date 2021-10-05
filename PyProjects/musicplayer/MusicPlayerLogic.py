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

def deletesong():
    curr_song=songs_list.curselection()
    songs_list.delete(curr_song[0])

def Play():