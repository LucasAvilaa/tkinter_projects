from tkinter import *

# cores ---------------------------------------
co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"   # azul / blue
co5 = "#fff873"   # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"   # vermelha / red
co8 = co4   # + verde
co10 ="#fcfbf7"
fundo = "#3b3b3b" # preta / black

janela = Tk()
janela.title("Tic Tac Toe")
janela.geometry("260x410")
janela.configure(bg=fundo)
janela.resizable(width=False, height=False)

# Dividir janela em 2 frames
frame_cima = Frame(janela, width=240, height=100, bg=co1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW, padx=10, pady=10)

# Configurando frame cima
app_x = Label(frame_cima, text="X", height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co7)
app_x.place(x=25, y=10)
app_x = Label(frame_cima, text="Jogador 1", height=1, relief='flat', anchor='center', font=('Ivy 9 bold'), bg=co1, fg=co0)
app_x.place(x=17, y=70)
app_x_pontos = Label(frame_cima, text="0", height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_x_pontos.place(x=80, y=20)

app_separador = Label(frame_cima, text=":", height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_separador.place(x=110, y=16)

app_o = Label(frame_cima, text="O", height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co4)
app_o.place(x=170, y=10)
app_o = Label(frame_cima, text="Jogador 2", height=1, relief='flat', anchor='center', font=('Ivy 9 bold'), bg=co1, fg=co0)
app_o.place(x=165, y=70)
app_o_pontos = Label(frame_cima, text="0", height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_o_pontos.place(x=130, y=20)

# Criando logica do app
jogador_1 = "X"
jogador_2 = "O"

score_1 = 0
score_2 = 0

tabela = [["1","2","3"],["4","5","6"],["7","8","9"]]

jogando = "X"
jogar = "Jogador 1"
contador = 0
contador_de_rodada = 0

def iniciar_jogo():
    app_vez = Label(frame_baixo, text=f"Vez de {jogar}", width=15, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=fundo, fg=co7)
    app_vez.place(x=28 , y=220)

    # Pra controlar o jogo
    def controlar(l, c):
        global jogando
        global contador
        global jogar

        # Linha 0
        if l == 0 and c == 0:
            btn = b_1
        
        elif l == 0 and c == 1:
            btn = b_2
        
        elif l == 0 and c == 2:
            btn = b_3
        
        # Linha 1
        elif l == 1 and c == 0:
            btn = b_4
        
        elif l == 1 and c == 1:
            btn = b_5
        
        elif l == 1 and c == 2:
            btn = b_6
        
        # Linha 2
        elif l == 2 and c == 0:
            btn = b_7
        
        elif l == 2 and c == 1:
            btn = b_8
        
        elif l == 2 and c == 2:
            btn = b_9
        
        # Logica
        if btn['text'] == '':
            if jogando == 'X':
                cor = co7
            else:
                cor = co8

            btn['fg'] = cor
            btn['text'] = jogando
            tabela[l][c] = jogando

            contador += 1

            if contador >= 5:
                # Linhas
                if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                    vencedor(jogando)
                elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                    vencedor(jogando)
                elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                    vencedor(jogando)

                # Colunas
                elif tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                    vencedor(jogando)
                elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                    vencedor(jogando)
                elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                    vencedor(jogando)
                
                # Diagonal
                elif tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                    vencedor(jogando)
                elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                    vencedor(jogando)

                # Empate
                elif contador == 9:
                    vencedor("Empate")

            if jogando == 'X':
                jogando = 'O'
                jogar = 'Jogador 2'
                cor_b = co4
            else:
                jogando = 'X'
                jogar = 'Jogador 1'
                cor_b = co7
            
            app_vez['text'] = f'Vez de {jogar}'
            app_vez['fg'] = cor_b

    # pra definir o vencedor
    def vencedor(jogando):
        global score_1
        global score_2
        global contador
        global contador_de_rodada
        global tabela
        
        change_att_btn('state', 'disable')
        
        app_vez.place(x=500, y=500)

        app_vencedor = Label(frame_baixo, text="", width=15, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)
        app_vencedor.place(x=28 , y=200)
        
        if jogando == 'X':
            contador_de_rodada += 1
            score_1 += 1
            app_vencedor['text'] = "Jogador 1 venceu!"
            app_x_pontos['text'] = score_1
        
        elif jogando == 'O':
            contador_de_rodada += 1
            score_2 += 1
            app_vencedor['text'] = "Jogador 2 venceu!"
            app_o_pontos['text'] = score_2
        
        elif jogando == 'Empate':
            app_vencedor['text'] = "Empate!"

        def start():                   
            change_att_btn('text', '')
            change_att_btn('state', 'normal')
            change_att_btn('state', 'normal')
            app_vencedor.destroy()
            b_jogar.destroy()

            app_vez.place(x=28 , y=220)

        # Botao jogar
        b_jogar = Button(frame_baixo, command=start, text="Próxima rodada", width=13, height=1, overrelief=RIDGE, font=('Ivy 10 bold'), bg=fundo, fg=co0)
        b_jogar.place(x=50, y=240)

        def jogo_acabou():
            app_vencedor.destroy()
            b_jogar.destroy()
            terminar()

        if contador_de_rodada >= 5:
            jogo_acabou()
        else:
            contador = 0
            tabela = [["1","2","3"],["4","5","6"],["7","8","9"]]
    
    # Pra terminar o jogo atual
    def terminar():
        global score_1
        global score_2
        global tabela
        global contador
        global contador_de_rodada

        score_1 = 0
        score_2 = 0
        contador = 0
        contador_de_rodada = 0
        tabela = [["1","2","3"],["4","5","6"],["7","8","9"]]

        change_att_btn('state', 'disable')

        app_fim = Label(frame_baixo, text="Jogo Acabou!", width=13, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)
        app_fim.place(x=40, y=200)

        def jogar_de_novo():
            app_x_pontos['text'] = "0"
            app_o_pontos['text'] = "0"
            app_fim.destroy()
            b_jogar.destroy()

            iniciar_jogo()

        # Botao jogar
        b_jogar = Button(frame_baixo, command=jogar_de_novo, text="Jogar de novo", width=10, height=1, overrelief=RIDGE, font=('Ivy 10 bold'), bg=fundo, fg=co0)
        b_jogar.place(x=65, y=240)

    # Configurando frame baixo
    def change_att_btn(att, value):
        b_1[att] = value
        b_2[att] = value
        b_3[att] = value
        b_4[att] = value
        b_5[att] = value
        b_6[att] = value
        b_7[att] = value
        b_8[att] = value
        b_9[att] = value

    # Linhas verticais
    app_ = Label(frame_baixo, text="", height=19, relief='flat', anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)
    app_.place(x=92 , y=15)
    app_ = Label(frame_baixo, text="", height=19, relief='flat', anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)
    app_.place(x=147, y=15)

    # Linhas Horizontais
    app_ = Label(frame_baixo, text="", width=160, relief='flat', anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co7)
    app_.place(x=40, y=70)
    app_ = Label(frame_baixo, text="", width=160, relief='flat', anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co7)
    app_.place(x=40, y=130)

    # Linha 0
    b_1 = Button(frame_baixo, command=lambda:controlar(0, 0) , text="", width=1, font=('Ivy 25 bold'), bg=fundo, borderwidth=0)
    b_1.place(x=43, y=18)
    b_2 = Button(frame_baixo, command=lambda:controlar(0, 1) , text="", width=1, font=('Ivy 25 bold'), bg=fundo, borderwidth=0)
    b_2.place(x=97, y=18)
    b_3 = Button(frame_baixo, command=lambda:controlar(0, 2) , text="", width=1, font=('Ivy 25 bold'), bg=fundo, borderwidth=0)
    b_3.place(x=150, y=18)

    # Linha 1
    b_4 = Button(frame_baixo, command=lambda:controlar(1, 0) , text="", width=1, font=('Ivy 25 bold'), bg=fundo, borderwidth=0)
    b_4.place(x=43, y=78)
    b_5 = Button(frame_baixo, command=lambda:controlar(1, 1) , text="", width=1, font=('Ivy 25 bold'), bg=fundo, borderwidth=0)
    b_5.place(x=97, y=78)
    b_6 = Button(frame_baixo, command=lambda:controlar(1, 2) , text="", width=1, font=('Ivy 25 bold'), bg=fundo, borderwidth=0)
    b_6.place(x=150, y=78)

    # Linha 2
    b_7 = Button(frame_baixo, command=lambda:controlar(2, 0) , text="", width=1, font=('Ivy 25 bold'), bg=fundo, borderwidth=0)
    b_7.place(x=43, y=136)
    b_8 = Button(frame_baixo, command=lambda:controlar(2, 1) , text="", width=1, font=('Ivy 25 bold'), bg=fundo, borderwidth=0)
    b_8.place(x=97, y=136)
    b_9 = Button(frame_baixo, command=lambda:controlar(2, 2) , text="", width=1, font=('Ivy 25 bold'), bg=fundo, borderwidth=0)
    b_9.place(x=150, y=136)

iniciar_jogo()

janela.mainloop()