#!/usr/bin/python26
#1.py
#_REQ een .gif en een .ico en een .wav
#_REQ func.py, waarin alle os en url functies
#_REQ several modules, as pmw

import os,sys
import webbrowser
from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledText



def course():
    webbrowser.open("http://www.imdb.com/title/tt1183865/episodes?season=2")

def k135():
     os.startfile("135-sales-data-randomizer.py")
     
    


def plasboek():
    os.chdir("f:\\temp")
    os.startfile("plasmans.txt")

def shutdown():
    os.system("totalbackup.py")
    os.system("c:\\windows\\system32\\shutdown.exe -s -f -t 1")

root=Tk()

c="col's paneel"



#root.withdraw('')
#root.geometry('200x210+350+420')
root.title("python course part 1")
#root.iconbitmap(default='berserker.ico')
root.geometry('600x800+100+150')
root.wm_attributes("-topmost", 1)

canvas = Canvas(width = 500, height = 500, bg = 'white')
gif1 = PhotoImage(file = 'ramesh.gif')
canvas.create_image(0, 10, image = gif1, anchor =NW)
gazet=ScrolledText(root, height=200,width=400,wrap=WORD,autohide=False,bootstyle="danger")
#gazet.pack(pady=15)
#canvas.create_text(300,50,text=quote)
canvas.pack(expand = YES, fill = BOTH)

		


v=Label(canvas,text='boer')

v.pack(side=TOP,anchor=N)

course=Button(canvas,anchor=SW,bg='red',text="course",command=course)
course.pack(side=BOTTOM,anchor=E)


#text=Label(canvas,bg='lightblue',text=str(c))
#text.pack()




quote = """
Assignment 7: Sales Data Randomizer

"""

text=Label(canvas, text=quote)
text.pack(side=BOTTOM,anchor=S)




#

a=Button(canvas,bg="yellow",text="plasboek",command=plasboek)
a.pack(side=TOP,anchor=E)
e=Button(canvas,bg="yellow",text="exit",command=exit)
e.pack(side=TOP,anchor=E)


r=Button(canvas,text="empty the cave",command=exit)
r.pack(side=TOP,anchor=E)

s=Button(canvas,text="plasboek",command=plasboek)
s.pack(side=TOP,anchor=E)


v=Button(canvas,bg="lightblue",text="plasboek",command=plasboek)
v.pack(side=BOTTOM,anchor=E)
f=Button(canvas,bg="blue",fg="white",text="afsluiten computer") #,command=shutdown
f.pack(side=BOTTOM,anchor=W)




counter = 0

#de meeste functies staan in apart func.py bestand





# create a menu
menu = Menu(root)
root.config(menu=menu)

partone = Menu(menu)
menu.add_cascade(label="nu", menu=partone)
partone.add_command(label="exit",command=exit)# exit
partone.add_command(label="k135",command=k135 )


nirsoftmenu = Menu(menu)
menu.add_cascade(label="nirsoft", menu=nirsoftmenu) 
nirsoftmenu.add_command(label="plasboek",command=plasboek)# asterisklogger
submenu = Menu(nirsoftmenu, tearoff=0)#Mozilla Cookie View
nirsoftmenu.add_cascade(label='plasboek', menu=submenu, underline=0)
submenu.add_command(label="run", command=plasboek,underline=0)
nirsoftmenu.add_command(label="plasboek", command=plasboek)# My Uninstaller


zendersmenu = Menu(menu)# ZENDERS
menu.add_cascade(label="zenders", menu=zendersmenu) 
zendersmenu.add_command(label="dordrecht", command=plasboek)# dordrecht





root.mainloop()