from tkinter import *
from tkcalendar import Calendar, DateEntry
import datetime
from dateutil.relativedelta import relativedelta

cor0="#3b3b3b"
cor1 = "#3b3b3b"
cor2 = "#333333"
cor3 = "#FFFFFF"
cor4 = "#fcc058"

window = Tk()
window.title("Age Calculator")
window.geometry('310x400')
window.configure(bg=cor0)
window.resizable(width=False, height=False)

frame_top = Frame(window, width=310, height=140, padx=0, pady=0, bg=cor2)
frame_top.grid(row=0, column=0)

frame_bottom = Frame(window, width=310, height=400, padx=0, pady=0, bg=cor1)
frame_bottom.grid(row=1, column=0, sticky=NW)

l_calculator = Label(frame_top, text="CALCULATOR", width=25, height=1, padx=3, anchor="center", font=('Ivy 15 bold'), bg=cor2, fg=cor3)
l_calculator.place(x=0, y=30)

l_age = Label(frame_top, text="AGE", width=11, height=1, padx=0, anchor="center", font=('Arial 35 bold'), bg=cor2, fg=cor4)
l_age.place(x=0, y=70)

l_dt_inicial = Label(frame_bottom, text="Initial date", height=1, pady=0, padx=0, anchor="nw", font=('Ivy 11'), bg=cor1, fg=cor3)
l_dt_inicial.place(x=50, y=30)

cal_1 = DateEntry(frame_bottom, width=13, background="darkblue", foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy', year=datetime.date.today().year)
cal_1.place(x=170, y=30)

l_dt_nasc = Label(frame_bottom, text="Date of birth", height=1, pady=0, padx=0, anchor="nw", font=('Ivy 11'), bg=cor1, fg=cor3)
l_dt_nasc.place(x=50, y=80)

cal_2 = DateEntry(frame_bottom, width=13, background="darkblue", foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy', day=1, month=7, year=2000)
cal_2.place(x=170, y=80)

value_years = Label(frame_bottom, text="", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 25 bold'),bg=cor1,  fg=cor3)
value_years.place(x=60, y=135)

l_years = Label(frame_bottom, text="Years", height=1, pady=0, padx=0, anchor="nw", font=('Ivy 11'), bg=cor1, fg=cor3)
l_years.place(x=50, y=175)

value_months = Label(frame_bottom, text="", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 12 bold'),bg=cor1,  fg=cor3)
value_months.place(x=140, y=135)

l_months = Label(frame_bottom, text="Months", height=1, pady=0, padx=0, anchor="nw", font=('Ivy 11'), bg=cor1, fg=cor3)
l_months.place(x=130, y=175)

value_days = Label(frame_bottom, text="", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 12 bold'),bg=cor1,  fg=cor3)
value_days.place(x=220, y=135)

l_days = Label(frame_bottom, text="Days", height=1, pady=0, padx=0, anchor="nw", font=('Ivy 11'), bg=cor1, fg=cor3)
l_days.place(x=210, y=175)

def calculate():
    start = datetime.datetime.strptime(cal_1.get(), "%d/%m/%Y")
    final = datetime.datetime.strptime(cal_2.get(), "%d/%m/%Y")

    calc = relativedelta(start, final)

    value_years['text'] = calc.years
    value_months['text'] = calc.months
    value_days['text'] = calc.days

b_age = Button(frame_bottom, command=calculate, text="Calcular Idade", width=20, height=1, bg=cor1, fg=cor3,font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
b_age.place(x=60, y=225)



window.mainloop()