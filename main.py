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

my_pic4 = Image.open("res/G8Sm.gif")
resize4 = my_pic4.resize((100,100),Image.ANTIALIAS)
new_pic4 = ImageTk.PhotoImage(my_pic4)
my_label = Label(root, image=new_pic4)
my_label.place(x=0, y=0, relwidth=1, relheight=1)


songtitle = Label(root, font="Helvetica 12 bold", textvariable=var)
songtitle.pack()

frame1 = Frame(root)
frame1.pack()
## for selecting the music directory path
file_directory = askdirectory()
os.chdir(file_directory)
os.getcwd()
songlist = os.listdir()


scroll = Scrollbar(frame1, orient=VERTICAL)
playlist = Listbox(frame1, yscrollcommand=scroll.set,selectmode=SINGLE,font ="Cambria 14 bold",width=50,height=6)
scroll.config (command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(fill=BOTH,expand=TRUE)
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


'''
my_pic1 = Image.open("res/icons8-circled-play-48.png")
resize1 = my_pic1.resize((40,40),Image.ANTIALIAS)
new_pic1 = ImageTk.PhotoImage(resize1)
my_pic2 = Image.open("res/icons8-stop-48.png")
resize2 = my_pic2.resize((40,40),Image.ANTIALIAS)
new_pic2 = ImageTk.PhotoImage(resize2)
my_pic3 = Image.open("res/icons8-pause-button-48.png")
resize3 = my_pic3.resize((40,40),Image.ANTIALIAS)
new_pic3 = ImageTk.PhotoImage(resize3)
my_pic4 = Image.open("res/icons8-resume-button-48.png")
resize4 = my_pic4.resize((40,40),Image.ANTIALIAS)
new_pic4 = ImageTk.PhotoImage(resize4)
'''
style = Style()
style.configure('C.TButton', background='dodger blue',font='algerian 10 bold')
style.configure('C1.TButton',background= 'red',font='algerian 10 bold')
style.configure('C2.TButton', background= 'yellow',font='algerian 10 bold')
style.configure('C3.TButton', background = 'green',font='algerian 10 bold')
button1 = Button(frame2,command=play,text="PLAY",style = 'C.TButton')
button2 = Button(frame2,command=Exit,text="STOP",style = 'C1.TButton')
button3 = Button(frame2,command=pause,text='PAUSE',style = 'C2.TButton')
button4 = Button(frame2,command=resume,text='RESUME',style = 'C3.TButton')
button1.pack(side=LEFT,padx=5,pady=5)
button2.pack(side=LEFT,padx=5,pady=5)
button3.pack(side=LEFT,padx=5,pady=5)
button4.pack(side=LEFT,padx=5,pady=5)

root.mainloop()





