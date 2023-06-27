from tkinter import *
from tkinter import ttk
import pytz
import requests
from datetime import datetime
import pycountry_convert as pc

from PIL import Image, ImageTk
from .key import KEY_WEATHER

co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul

fundo_dia = "#6cc4cc"
fundo_noite = "#484f60"
fundo_tarde = "#bfb86d"

fundo = fundo_dia

window = Tk()
window.title("Weather")
window.geometry('380x350')
window.configure(bg=fundo)
window.resizable(width=False, height=False)

ttk.Separator(window, orient="horizontal").grid(row=0, columnspan=1, ipadx=180)

# Dividindo tela
frame_head = Frame(window, width=380, height=50, bg=fundo, padx=0, pady=0)
frame_head.grid(row=1, column=0)
frame_body = Frame(window, width=380, height=300, bg=fundo, padx=0, pady=0)
frame_body.grid(row=2, column=0, sticky=NW)

stryle = ttk.Style(window).theme_use("clam")

def get_info():
    global fundo 

    city = e_city.get()
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY_WEATHER}")


    l_cidade['text'] = ''
    l_data['text'] = ''
    l_umidade['text'] = ''
    l_pressao['text'] = ''
    l_velocidade['text'] = ''
    l_descricao['text'] = ''

    if res.status_code == 200:
        data = res.json()
        #print(data)

        city = data["name"]
        pais_codigo = data["sys"]["country"]
        pais = pytz.country_names[pais_codigo]
        
        # Horas
        zona_fuso = pytz.country_timezones[pais_codigo]
        zona = pytz.timezone(zona_fuso[0])
        zona_horas = datetime.now(zona)
        zona_hora = zona_horas.strftime("%d/%m/%Y | %H:%M:%S %p")

        def pais_para_continente(i):
            continente_codigo = pc.country_alpha2_to_continent_code(i)
            return pc.convert_continent_code_to_continent_name(continente_codigo)

        continente = pais_para_continente(pais_codigo)

        l_cidade['text'] = f"{city} - {pais} / {continente}" 
        l_u_simbolo['text'] = '%'
        l_u_nome['text'] = 'Umidade'
        l_data['text'] = zona_hora
        l_umidade['text'] = data['main']['humidity']
        l_pressao['text'] = f"Pressão: {data['main']['pressure']}"
        l_velocidade['text'] = f"Velocidade vento: {data['wind']['speed']}"
        l_descricao['text'] = data['weather'][0]['description']

        # logica p/ trocar cor de fundo
        zona_periodo = int(zona_horas.strftime("%H"))

        global imagem

        if zona_periodo >= 6 and zona_periodo < 12:
            imagem = Image.open('./images/sol.png')
            fundo = fundo_dia
        elif zona_periodo >= 12 and zona_periodo <= 18:
            imagem = Image.open('./images/sol_tarde.png')
            fundo = fundo_tarde
        else:
            imagem = Image.open('./images/moon.png')
            fundo = fundo_noite

        imagem = imagem.resize((130,130))
        imagem = ImageTk.PhotoImage(imagem)

        l_icon = Label(frame_body, image=imagem, bg=fundo)
        l_icon.place(x=220, y=90)

        window.configure(bg=fundo)
        frame_head.configure(bg=fundo)
        frame_body.configure(bg=fundo)

        l_cidade['bg'] = fundo
        l_data['bg'] = fundo
        l_umidade['bg'] = fundo
        l_pressao['bg'] = fundo
        l_velocidade['bg'] = fundo
        l_descricao['bg'] = fundo
        l_u_simbolo['bg'] = fundo
        l_u_nome['bg'] = fundo

# Frame cima
e_city = Entry(frame_head, width=20, font=('', 14))
e_city.place(x=15, y=10)

b_search = Button(frame_head, text='Search', bg=co1, fg=co2, command=get_info, font=('Ivy 9 bold'), overrelief=RIDGE)
b_search.place(x=280, y=10)

# Frame corpo
l_cidade = Label(frame_body, text="", anchor='center', bg=fundo, fg=co1, font=('Arial 16'))
l_cidade.place(x=10, y=10)

l_data = Label(frame_body, text="", anchor='center', bg=fundo, fg=co1, font=('Arial 16'))
l_data.place(x=10, y=54)

l_umidade = Label(frame_body, text="", anchor='center', bg=fundo, fg=co1, font=('Arial 48'))
l_umidade.place(x=10, y=100)

l_u_simbolo = Label(frame_body, text="", anchor='center', bg=fundo, fg=co1, font=('Arial 15 bold'))
l_u_simbolo.place(x=85, y=110)

l_u_nome = Label(frame_body, text="", anchor='center', bg=fundo, fg=co1, font=('Arial 15'))
l_u_nome.place(x=85, y=140)

l_pressao = Label(frame_body, text="", anchor='center', bg=fundo, fg=co1, font=('Arial 12'))
l_pressao.place(x=10, y=184)

l_velocidade = Label(frame_body, text="", anchor='center', bg=fundo, fg=co1, font=('Arial 12'))
l_velocidade.place(x=10, y=212)

l_descricao = Label(frame_body, text="",anchor='center', bg=fundo, fg=co1, font=('Arial 12'))
l_descricao.place(x=230, y=230)

window.mainloop()
