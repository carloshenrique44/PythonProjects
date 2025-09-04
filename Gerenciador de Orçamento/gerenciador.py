from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk


cor0 = "#2e2d2b"
cor1 = "#feffff"
cor2 = "#4fa882"
cor3 = "#0084db"
cor4 = "#403d3d"
cor5 = "#e06636"
cor6 = "#038cfc"
cor7 = "#3fbfb9"
cor8 = "#263238"
cor9 = "#e9edf5"
cor10 = "#6e8faf"
cor11 = "#f2f4f2"


janela = Tk()
janela.title("Gerenciador de Orçamento")
janela.geometry("400x490") 
janela.configure(background=cor1)
janela.resizable(width=False, height=False)


style = ttk.Style(janela)
style.theme_use("clam")


frameCima = Frame(janela, width=300, height=50, bg=cor1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=300, height=90, bg=cor1, relief="solid")
frameMeio.grid(row=1, column=0, padx=10, pady=10)

frameBaixo = Frame(janela, width=300, height=340, bg=cor1, relief="raised")  
frameBaixo.grid(row=2, column=0)


app_ = Label(frameCima, text="Budget", compound=LEFT,
             relief=FLAT, anchor=NW, font=("Verdana", 20), bg=cor1, fg=cor4)
app_.place(x=0, y=0)


try:
    app_img = Image.open("log.png")
    app_img = app_img.resize((40, 40))
    app_img = ImageTk.PhotoImage(app_img)

    app_logo = Label(frameCima, image=app_img, width=900, compound=LEFT,
                     padx=5, relief=FLAT, anchor=NW, bg=cor1, fg=cor4)
    app_logo.place(x=150, y=0)
except:
    print("Imagem 'log.png' não encontrada!")


l_linha = Label(frameCima, width=295, height=1, anchor=NW,
                font=("Verdana", 1), bg=cor3, fg=cor1)
l_linha.place(x=0, y=47)


l_valor_quantia = Label(frameMeio, text="Renda Mensal?", height=1, anchor=NW,
                        font=("Ivy", 10), bg=cor1, fg=cor4)
l_valor_quantia.place(x=7, y=15)

e_valor_quantia = Entry(frameMeio, width=10, font=("Ivy", 14),
                        justify="center", relief="solid")
e_valor_quantia.place(x=10, y=40)


def calcular():
    try:
        renda_mensal = float(e_valor_quantia.get().replace(",", "."))
    except ValueError:
        print("Insira um valor numérico válido!")
        return

    vlr_40 = (40 / 100) * renda_mensal
    vlr_30 = (30 / 100) * renda_mensal
    vlr_20 = (20 / 100) * renda_mensal
    vlr_10 = (10 / 100) * renda_mensal

    l_necessidades["text"] = f"R$ {vlr_40:,.2f}"
    l_desejos["text"] = f"R$ {vlr_30:,.2f}"
    l_poupanca["text"] = f"R$ {vlr_20:,.2f}"
    l_apostas["text"] = f"R$ {vlr_10:,.2f}"


botao_calcular = Button(frameMeio, anchor=NW, text="CALCULAR", overrelief="ridge",
                        font=("Ivy", 10, "bold"), bg=cor1, fg=cor0, command=calcular)
botao_calcular.place(x=150, y=40)


l_nome = Label(frameBaixo, text="Divisão do salário:", padx=10, width=35,
               height=1, anchor=NW, font=("Verdana", 11), bg=cor3, fg=cor1)
l_nome.place(x=0, y=0)


l_total_necessidades = Label(frameBaixo, text="Necessidades", height=1, anchor=E,
                             font=("Verdana", 10), bg=cor9, fg=cor0)
l_total_necessidades.place(x=10, y=40)

l_necessidades = Label(frameBaixo, width=22, height=1, anchor=NW,
                       font=("Verdana", 12), bg=cor1, fg=cor4)
l_necessidades.place(x=10, y=75)


l_total_desejos = Label(frameBaixo, text="Compras dia", height=1, anchor=E,
                        font=("Verdana", 10), bg=cor9, fg=cor0)
l_total_desejos.place(x=10, y=115)

l_desejos = Label(frameBaixo, width=22, height=1, anchor=NW,
                  font=("Verdana", 12), bg=cor1, fg=cor4)
l_desejos.place(x=10, y=145)


l_total_poupanca = Label(frameBaixo, text="Poupança", height=1, anchor=E,
                         font=("Verdana", 10), bg=cor9, fg=cor0)
l_total_poupanca.place(x=10, y=185)

l_poupanca = Label(frameBaixo, width=22, height=1, anchor=NW,
                   font=("Verdana", 12), bg=cor1, fg=cor4)
l_poupanca.place(x=10, y=215)


l_total_apostas = Label(frameBaixo, text="Apostas", height=1, anchor=E,
                        font=("Verdana", 10), bg=cor9, fg=cor0)
l_total_apostas.place(x=10, y=255)

l_apostas = Label(frameBaixo, width=22, height=1, anchor=NW,
                  font=("Verdana", 12), bg=cor1, fg=cor4)
l_apostas.place(x=10, y=285)


janela.mainloop()
