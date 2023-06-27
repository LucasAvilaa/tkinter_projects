from tkinter import *
from tkinter import ttk, messagebox
from view import *
from PIL import Image, ImageTk
import re

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


################# cores ###############

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
co10 ="#6e8faf"  # 
co11 = "#f2f4f2"
colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

window = Tk()
window.title('Travel Budget')
window.geometry('1100x900')
window.configure(bg=co1)
window.resizable(width=False, height=False)

style = ttk.Style(window)
style.theme_use('clam')
style.configure("Treeview", highlightthickness=0, bd=0, font=("Calibri 10"))

# Dividindo Frame

# Top
frame_top = Frame(window, width=1200, height=50, bg=co1)
frame_top.grid(row=0, column=0)

# Middle
frame_middle = Frame(window, width=1200, height=450, bg=co1, padx=10, pady=10)
frame_middle.grid(row=1, column=0)

frame_left = Frame(frame_middle, width=350, height=450, bg=co9, relief='raised')
frame_left.place(x=0, y=0)

frame_right = Frame(frame_middle, width=880, height=450, bg=co1, relief='raised')
frame_right.place(x=350, y=0)

# Bottom
frame_bottom = Frame(window, width=1200, height=400, bg=co1, pady=10)
frame_bottom.grid(row=2, column=0, sticky=NSEW)

l_logo = Label(frame_top, text="Travel Budget", compound=LEFT, padx=5, anchor='nw', font=('Verdana 30'), bg=co1, fg=co4)
l_logo.place(x=0, y=0)

img = Image.open("./images/travel-and-tourism.png")
img = img.resize((50, 50))
img = ImageTk.PhotoImage(img)

img_logo = Label(frame_top, image=img, bg=co1)
img_logo.place(x=320, y=0)

def totais():
    l_name = Label(frame_left, text="Meu Orçamento e despesa", width=50, padx=5, anchor='nw', font=('Verdana 15 bold'), bg=co3, fg=co1)
    l_name.place(x=0, y=0)

    # Orcamento total
    l_txt_orcamento = Label(frame_left, text="Orçamento total", anchor='e', font=('Verdana 15'), bg=co9, fg=co0)
    l_txt_orcamento.place(x=10, y=50)
    
    vl_orcamento = get_orcamento()
    l_value_orcamento = Label(frame_left, text="${:,.2f}".format(vl_orcamento), width=20, anchor='nw', font=('Verdana 14'), bg=co1, fg=co4)
    l_value_orcamento.place(x=10, y=80)

    # despesa total
    l_txt_despesa = Label(frame_left, text="Despesa total", anchor='e', font=('Verdana 15'), bg=co9, fg=co0)
    l_txt_despesa.place(x=10, y=120)
    
    vl_despesa = get_total_despesa()
    l_value_despesa = Label(frame_left, text="${:,.2f}".format(vl_despesa), width=20, anchor='nw', font=('Verdana 14'), bg=co1, fg=co4)
    l_value_despesa.place(x=10, y=150)

    # restante total
    l_txt_restante = Label(frame_left, text="Valor Restante", anchor='e', font=('Verdana 15'), bg=co9, fg=co0)
    l_txt_restante.place(x=10, y=190)

    restante_total = vl_orcamento - vl_despesa
    l_value_restante = Label(frame_left, text="${:,.2f}".format(restante_total), width=20, anchor='nw', font=('Verdana 14'), bg=co1, fg=co4)
    l_value_restante.place(x=10, y=220)


def grafico():
    figura = Figure(figsize=(7,4), dpi=100)
    ax = figura.add_subplot(111)

    lista_valores = []
    lista_categorias = get_categories()
    
    for categ in lista_categorias:        
        lista_valores.append(sum_by_category([categ]))
    
    print(lista_categorias)
    print(lista_valores)

    explode = [0.09 for c in lista_categorias]

    ax.pie(lista_valores, explode=explode, wedgeprops={"width": 0.3}, autopct='%1.1f%%', colors=colors, shadow=True, startangle=90, pctdistance=1.2)
    
    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    # Frame pie
    frame_right_pie = Frame(frame_right, width=600, height=290, bg=co11, pady=0, relief='raised')
    frame_right_pie.place(x=-40, y=0)

    l_name = Label(frame_right, text="Para onde está indo minhas despesas totais?", width=60, anchor=CENTER, padx=2, font=('Verdana 14'), bg=co10, fg=co1)
    l_name.place(x=0, y=0)

    canva_categoria = FigureCanvasTkAgg(figura, frame_right_pie)
    canva_categoria.get_tk_widget().grid(row=0, column=0, padx=0)



l_name = Label(frame_bottom, text="Quais são suas despesas", width=87, anchor='nw', padx=6, font=('Verdana 14'), bg=co10, fg=co1)
l_name.grid(row=0, column=0, columnspan=6, padx=5)

frame_table = Frame(frame_bottom, width=450, height=370, bg=co1)
frame_table.grid(row=1, column=0, padx=10)

frame_operations = Frame(frame_bottom, width=300, height=370, bg=co1)
frame_operations.grid(row=1, column=1, padx=5)

frame_settings = Frame(frame_bottom, width=300, height=370, bg=co1)
frame_settings.grid(row=1, column=2, padx=5)

def create_table():
    table_head = ['id','Type','Description','Total']

    global tree

    tree = ttk.Treeview(frame_table, selectmode='extended', columns=table_head, show='headings', height=15)
    
    # vertical scroll bar
    vsb = ttk.Scrollbar(frame_table, orient='vertical', command=tree.yview)

    # horizontal scroll bar
    hsb = ttk.Scrollbar(frame_table, orient='horizontal', command=tree.xview)
    
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky=NSEW)
    vsb.grid(column=1, row=0, sticky=NS)
    hsb.grid(column=0, row=1, sticky=EW)

    hd = ["nw", "nw", "center", "e", "e"]
    h = [30, 120, 160, 80, 90]
    n = 0

    for col in table_head:
        tree.heading(col, text=col.title(), anchor='center')
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

def update_values_tree():
    for i in tree.get_children():
        tree.delete(i)

    list_itens = get_all_despesa()
    for item in list_itens:
        tree.insert('', 'end', values=item)


# Configuração Despesa ---
l_info = Label(frame_operations, text="Insira novas despesas", height=1, anchor='nw', padx=6, font=('Verdana 14 bold'), bg=co1, fg=co4)
l_info.place(x=10, y=10)

# Category
l_categoria = Label(frame_operations, text="Category:", anchor='nw', padx=6, font=('Ivy 12'), bg=co1, fg=co4)
l_categoria.place(x=10, y=45)

categories = ["Transporte", "Alimentacao", "Entretenimento", "Outros"]

combo_categoria = ttk.Combobox(frame_operations, width=12, font=('Ivy 12'), values=categories)
combo_categoria.place(x=110, y=45)

# Description
l_description = Label(frame_operations, text="Description:", anchor='nw', padx=6, font=('Ivy 12'), bg=co1, fg=co4)
l_description.place(x=10, y=80)

e_description = Entry(frame_operations, width=16, justify='left', relief='solid')
e_description.place(x=120, y=80)

# Value
l_value = Label(frame_operations, text="Value:", anchor='nw', padx=6, font=('Ivy 12'), bg=co1, fg=co4)
l_value.place(x=10, y=110)
e_value = Entry(frame_operations, width=16, justify='left', relief='solid')
e_value.place(x=80, y=110)

img_add = Image.open('./images/add.png')
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)

def insert_des():
    insert_despesa([combo_categoria.get(), e_description.get(), e_value.get()])
    recarregar()
    messagebox.showinfo("Success", "Inserido com sucesso")
    

btn_insert = Button(frame_operations, image=img_add, command=insert_des, compound='left', anchor='nw', text="Adicionar", width=94, overrelief='ridge', font=('Ivy 10 bold'), bg=co1, fg=co0)
btn_insert.place(x=80, y=150)


# Quantia total
l_info = Label(frame_settings, text="Atualizar Quantia total", anchor='nw', padx=6, font=('Verdana 14 bold'), bg=co1, fg=co4)
l_info.place(x=10, y=10)

l_qtd_total = Label(frame_settings, text="Quantia total:", anchor='nw', padx=6, font=('Ivy 12'), bg=co1, fg=co4)
l_qtd_total.place(x=10, y=40)

e_qtd_total = Entry(frame_settings, width=16, justify='left', relief='solid')
e_qtd_total.place(x=130, y=40)


def update_despesa():

    tree_itens = tree.focus()
    print(tree_itens)
    tree_dict = tree.item(tree_itens)
    print(tree_dict)
    tree_list = tree_dict['values']
    print(tree_list)
    
    combo_categoria.insert(0, tree_list[1])
    e_description.insert(0, tree_list[2])
    e_value.insert(0, tree_list[3])

    img_done = Image.open('./images/done.png')
    img_done = img_done.resize((20,20))
    img_done = ImageTk.PhotoImage(img_done)

    def save():
        update_despesa_db([combo_categoria.get(), e_description.get(), e_value.get(), tree_list[0]])

        recarregar()
        
        btn_save.destroy()

        messagebox.showinfo("Success", "Atualizado com sucesso")

    btn_save = Button(frame_operations, command=save, anchor='nw', text="Salvar", overrelief='ridge', font=('Ivy 10 bold'), bg=co1, fg=co0)
    btn_save.place(x=80, y=270)


def update_orcamento():
    insert_total_orcamento([e_qtd_total.get()])
    recarregar()
    messagebox.showinfo("Success", "Atualizado com sucesso")

def delete_despesa():
    tree_itens = tree.focus()
    tree_dict = tree.item(tree_itens)
    tree_list = tree_dict['values']

    delete_despesa_db([tree_list[0]])
    recarregar()
    messagebox.showinfo("Success", "Deletado com sucesso")

# Btn Update
img_update = Image.open('./images/update.png')
img_update = img_update.resize((20,20))
img_update = ImageTk.PhotoImage(img_update)

btn_update_desp = Button(frame_operations, image=img_update, command=update_despesa, compound='left', anchor='nw', text="Atualizar Despesa", width=170, overrelief='ridge', font=('Ivy 10 bold'), bg=co1, fg=co0)
btn_update_desp.place(x=80, y=190)

btn_update = Button(frame_settings, image=img_update, command=update_orcamento ,compound='left', anchor='nw', text="Atualizar", width=94, overrelief='ridge', font=('Ivy 10 bold'), bg=co1, fg=co0)
btn_update.place(x=130, y=70)

# Btn Delete

img_delete = Image.open('./images/trash.png')
img_delete = img_delete.resize((20,20))
img_delete = ImageTk.PhotoImage(img_delete)

btn_delete = Button(frame_operations, image=img_delete, command=delete_despesa ,compound='left', anchor='nw', text="Deletar", width=94, overrelief='ridge', font=('Ivy 10 bold'), bg=co1, fg=co0)
btn_delete.place(x=80, y=230)

def recarregar():
    grafico()
    update_values_tree()
    totais()

    combo_categoria.delete(0, END)
    e_description.delete(0, END)
    e_value.delete(0, END)
    e_qtd_total.delete(0, END)

create_table()
update_values_tree()
grafico()
totais()

window.mainloop()

