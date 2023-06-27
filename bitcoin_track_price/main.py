from tkinter import *
import requests

from PIL import Image, ImageTk

#Colors
co1 = "white"
co2 = "#333333"
co3 = "#000000"

window = Tk()
window.title('Bitcoin Price')
window.geometry('390x300')
window.configure(bg=co1)
window.resizable(width=False, height=False)

def get_prices():
    res = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,AOA,BRL")
    dados = res.json()
    
    # -- USD
    usd = float(dados["USD"])
    formatted_usd = "${:,.3f}".format(usd)
    usd["text"] = formatted_usd

    # -- Kwanza
    aoa = float(dados["AOA"])
    formatted_aoa = "{:,.3f}".format(aoa)
    aoa["text"] = "Em Kwanzas é : AOA " + formatted_aoa

    # -- Euro
    euro = float(dados["EUR"])
    formatted_euro = "{:,.3f}".format(euro)
    euros["text"] = "Em euros é : € " + formatted_euro

    # -- Reais
    reais = float(dados["BRL"])
    formatted_reais = "{:,.3f}".format(reais)
    brl["text"] = "Em reais é : R$ " + formatted_reais

    frame_body.after(200, get_prices)

frame_head = Frame(window, width=390, height=50, bg=co1)
frame_head.grid(row=1, column=0)

frame_body = Frame(window, width=390, height=300, bg=co2)
frame_body.grid(row=2, column=0)

image_1 = Image.open('images/bitcoin.png')
image_1 = image_1.resize((30, 30))
image_1 = ImageTk.PhotoImage(image_1)

icon_1 = Label(frame_head, image=image_1, bg=co1)
icon_1.place(x=50, y=10)

name = Label(frame_head, padx = 0, text = "Bitcoin Price Tracker", bg=co1, fg=co3, width=17, height=1, anchor="center", font=('Poppins 18'))
name.place(x = 80, y=11)

usd = Label(frame_body, text = "$ ", width=14, height=1, font=('Arial 30 bold'), bg=co2, fg=co1, anchor="center")
usd.place(x=40, y=28)

euros = Label(frame_body, text = "Em euros é : € ", height=1, font=('Arial 15 bold'), bg=co2, fg=co1, anchor="center")
euros.place(x=10, y=130)

aoa = Label(frame_body, text = "Em Kwanzas é : AOA ", height=1, font=('Arial 15 bold'), bg=co2, fg=co1, anchor="center")
aoa.place(x=10, y=170)

brl = Label(frame_body, text = "Em reais é : R$ ", height=1, font=('Arial 15 bold'), bg=co2, fg=co1, anchor="center")
brl.place(x=10, y=210)

get_prices()

window.mainloop()