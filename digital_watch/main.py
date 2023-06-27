from tkinter import *
from datetime import datetime
from pyglet import font
import os

font.add_directory(f"{os.getcwd()}/digital_watch/digital-7")


# Colors ---------------------------------------
fundo = "#3d3d3d"  # Black
cor = "#fafcff"  # White

janela = Tk()
janela.title("Digital watch")
janela.geometry("440x180")
janela.configure(bg=fundo)
janela.resizable(width=False, height=False)


def get_time_now():
    time = datetime.now()
    hour = time.strftime("%H:%M:%S")
    day_week = time.strftime("%A")

    l1["text"] = hour
    l2["text"] = f"{day_week} {str(time.day)}/{str(time.month)}/{str(time.year)}"
    
    l1.after(1000, get_time_now)

l1 = Label(janela, text="", anchor='center', font=('Arial 80'), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela, text="", font=('digital-7 17'), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)

get_time_now()

janela.mainloop()

