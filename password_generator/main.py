from tkinter import *
from tkinter import ttk, messagebox

from PIL import Image, ImageTk

import string
import random

# cores
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor4 = "#eb463b"  # red / vermelha

window = Tk()
window.title('Password Generator')
window.geometry('320x360')
window.configure(bg=cor2)
window.resizable(width=False, height=False)

estilo = ttk.Style(window)
estilo.theme_use('clam')

# Dividindo em Frames
frame_cima = Frame(width=320, height=60, bg=cor2, padx=0, pady=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(width=320, height=300, bg=cor2, padx=0, pady=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# Frame Cima
img = Image.open('./password_generator/images/pass_1.png')
img = img.resize((50, 50))
img = ImageTk.PhotoImage(img)

app_logo = Label(frame_cima, height=50, image=img, compound=LEFT, padx=10, relief='flat', anchor='nw', bg=cor2)
app_logo.place(x=5, y=2)

app_name = Label(frame_cima, text='Password Generator', width=20, height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 16 bold') , bg=cor2, fg=cor1)
app_name.place(x=60, y=15)

app_linha = Label(frame_cima, text='', width=320, height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 1 bold') , bg=cor4, fg=cor1)
app_linha.place(x=0, y=55)

# Frame baixo

app_senha = Label(frame_baixo, text='- - - -', width=26, height=2, padx=0, relief='solid', anchor='center', font=('Ivy 10 bold') , bg=cor2, fg=cor1)
app_senha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx=3, pady=10)

app_info = Label(frame_baixo, text='Número total de caracteres na senha', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold') , bg=cor2, fg=cor1)
app_info.grid(row=1, column=0, columnspan=3, sticky=NSEW, padx=5, pady=1)

tamanho = IntVar()
tamanho.set(8)
spin = Spinbox(frame_baixo, from_=0, to=20, width=5, textvariable=tamanho)
spin.grid(row=2, column=0, columnspan=2, sticky=NW, padx=100, pady=8)

app_caracteres = Label(frame_baixo, width=310, height=210, padx=0, relief='flat', bg=cor2)
app_caracteres.grid(row=3, column=0, sticky=NSEW, columnspan=3)


# --------------- Letras Maiuscula ---------------
c_maiuscula = BooleanVar()
c_maiuscula.set(True)
check_1 = Checkbutton(app_caracteres, text='Letras Maiuscula', var=c_maiuscula, onvalue=True, offrelief='groove', font=('Ivy 10 bold'),relief='flat', bg=cor2)
check_1.grid(row=0, column=0, sticky=NW, padx=2, pady=5)

# --------------- Letras Minuscula ---------------
c_minuscula = BooleanVar()
c_minuscula.set(False)
check_2 = Checkbutton(app_caracteres, text='Letras Minuscula', var=c_minuscula, onvalue=True, offrelief='groove', relief='flat', font=('Ivy 10 bold'), bg=cor2)
check_2.grid(row=1, column=0, sticky=NW, padx=2, pady=5)


# --------------- Números ---------------
c_numeros = BooleanVar()
c_numeros.set(False)
check_3 = Checkbutton(app_caracteres, text='Números', var=c_numeros, onvalue=True, offrelief='groove', relief='flat', font=('Ivy 10 bold'), bg=cor2)
check_3.grid(row=2, column=0, sticky=NW, padx=2, pady=5)


# --------------- Simbolos ---------------
c_simbolos = BooleanVar()
c_simbolos.set(False)
check_4 = Checkbutton(app_caracteres, text='Simbolos', var=c_simbolos, onvalue=True, offrelief='groove', relief='flat', font=('Ivy 10 bold'), bg=cor2)
check_4.grid(row=3, column=0, sticky=NW, padx=2, pady=5)

# Função gerar senha

def generate_password():
    alfabeto_maior = string.ascii_uppercase
    alfabeto_menor = string.ascii_lowercase
    numeros = "0123456789"
    simbolos = "{}[](),.;/:+§!@#$%*"

    caracteres = ''
    if c_maiuscula.get():
        caracteres += alfabeto_maior
    
    if c_maiuscula.get():
        caracteres += alfabeto_menor
    
    if c_numeros.get():
        caracteres += numeros
    
    if c_simbolos.get():
        caracteres += simbolos

    password = "".join(random.sample(caracteres, int(spin.get())))
    app_senha['text'] = password

    def copy_password():
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(password)

        messagebox.showinfo("Success", "Senha copiada com sucesso")

    app_copiar = Button(frame_baixo, command=copy_password, text='Copiar', width=7, height=1, padx=0, relief='raised', anchor='center', font=('Ivy 10 bold') , bg=cor2, fg=cor1)
    app_copiar.grid(row=0, column=1, columnspan=1, sticky=NSEW, padx=5, pady=7)

# --------------- Botao gerar senha ---------------
btn_generate = Button(app_caracteres, command=generate_password, text='Gerar Senha', width=34, height=1, overrelief='solid', padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=cor4, fg=cor2)
btn_generate.grid(row=5, column=0, sticky=NSEW, padx=3, pady=11)


window.mainloop()