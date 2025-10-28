import os
from tkinter import *
root=Tk()
root.title('kivioja  python developer bootcamp 135: sales.csv randomizer')
root.iconbitmap(default='berserker.ico')
root.geometry("800x400")

menu=Menu(root)
root.config(menu=menu)


backup_file_path = "/backup/sales_backup_2025-10-28.csv"

def k135():
       os.startfile("135.py")

def k135text():
       os.startfile("135.txt")

def k135csv():
       os.startfile("135.csv")
       

def k135log():
       os.startfile("135.log")


def k135backup():
       

       # Check if the file exists
       if os.path.exists(backup_file_path):
              try:
                     os.startfile(backup_file_path)
              except Exception as e:
                     print(f"Error opening file: {e}")
       else:
              print("Backup file does not exist.")
 

def hoppa():
    pass

aaa=Menu(menu)
bbb=Menu(menu)
ccc=Menu(menu)

menu.add_cascade(label="part 1",menu=aaa)
aaa.add_command(label="randomizer",command=k135)

menu.add_cascade(label="description",menu=bbb)
bbb.add_command(label="description",command=k135text)

menu.add_cascade(label="relevant files",menu=ccc)
ccc.add_command(label="original csv",command=k135csv)
ccc.add_command(label="log file",command=k135log)
ccc.add_command(label="shuffled csv",command=k135backup)




root.mainloop()