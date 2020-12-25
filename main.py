from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askdirectory
from PIL import Image
from PIL import ImageTk
import os
import pygame





## creating gui
root = Tk()
var = StringVar()
root.title("Persona_player")


songtitle = Label(root, font="Helvetica 12 bold", textvariable=var)
songtitle.pack()

frame1 = Frame(root)
frame1.pack()
## for selecting the music directory path
file_directory = askdirectory()
os.chdir(file_directory)
songlist = os.listdir()
scroll = Scrollbar(frame1, orient=VERTICAL)
playlist = Listbox(frame1, yscrollcommand=scroll.set, height=6,selectmode=SINGLE,font ="Cambria 14 bold")
scroll.config (command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(fill=BOTH)
for item in songlist:
    pos=0
    playlist.insert(pos, item)
    pos = pos + 1
frame2 = Frame(root)
frame2.pack()
##integrating buttons

##initialize py game modules
pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playlist.get(ACTIVE))
    var.set(playlist.get(ACTIVE))
    pygame.mixer.music.play()

def Exit():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()

my_pic1 = Image.open("icons8-circled-play-48.png")
resize1 = my_pic1.resize((40,40),Image.ANTIALIAS)
new_pic1 = ImageTk.PhotoImage(resize1)
my_pic2 = Image.open("icons8-stop-48.png")
resize2 = my_pic2.resize((40,40),Image.ANTIALIAS)
new_pic2 = ImageTk.PhotoImage(resize2)
my_pic3 = Image.open("icons8-pause-button-48.png")
resize3 = my_pic3.resize((40,40),Image.ANTIALIAS)
new_pic3 = ImageTk.PhotoImage(resize3)
my_pic4 = Image.open("icons8-resume-button-48.png")
resize4 = my_pic4.resize((40,40),Image.ANTIALIAS)
new_pic4 = ImageTk.PhotoImage(resize4)
button1 = Button(frame2,command=play,image=new_pic1)
button2 = Button(frame2,command=Exit,image=new_pic2)
button3 = Button(frame2,command=pause,image=new_pic3)
button4 = Button(frame2,command=resume,image=new_pic4)
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)

root.mainloop()





