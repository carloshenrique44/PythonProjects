import tkinter as tk
from tkinter import ttk

def escolherjogador(jogador):
    jogador = jogador.lower()
    if jogador == "m":
        resultado = "⚽ Você escolheu Messi, o melhor e maior jogador da história! 🐐"
        cor = "#3498db"  # Azul Messi
    elif jogador == "p":
        resultado = "⚠️ Opção inválida! Aqui não é obra, e nem exército! ⚠️"
        cor = "#f1c40f"  # Amarelo Pelé
    elif jogador == "c":
        resultado = "🚧 Opção inválida! Isso não é sobre cones, é futebol! 🚧"
        cor = "#2ecc71"  # Verde CR7
    else:
        resultado = "❌ Escolha entre M, P ou C, parceiro!"
        cor = "red"

    # Atualiza label resultado com cor vibrante e fonte estilosa
    label_resultado.config(text=resultado, fg=cor)

# Janela principal
janela = tk.Tk()
janela.title("⚽ Escolha o Melhor Jogador da História ⚽")
janela.geometry("800x500")
janela.configure(bg="#145214")  # Fundo verde escuro tipo gramado

# Fonte geral para botões e labels (futebol style)
fonte_titulo = ("Segoe UI Black", 24, "bold")
fonte_botoes = ("Segoe UI Semibold", 16, "bold")
fonte_resultado = ("Arial Black", 18, "bold")

# Título
label_titulo = tk.Label(janela, text="Quem é o melhor jogador da história?", 
                       font=fonte_titulo, bg="#145214", fg="#FFFFFF")  # dourado
label_titulo.pack(pady=(30, 40))

# Frame dos botões (centralizado)
frame = tk.Frame(janela, bg="#145214")
frame.pack()

# Configurar estilo ttk para botões com hover e cor custom
style = ttk.Style(janela)
style.theme_use('clam')
style.configure('Botao.TButton', font=fonte_botoes, foreground="white", background="#1a73e8", padding=12)
style.map('Botao.TButton', background=[('active', '#1769aa')])

# Botões com emojis e cores do time
botao_messi = ttk.Button(frame, text="🐐 Messi (M)", style='Botao.TButton', command=lambda: escolherjogador("m"))
botao_messi.grid(row=0, column=0, padx=20, pady=15)

botao_pele = ttk.Button(frame, text="👑 Pelé (P)", style='Botao.TButton', command=lambda: escolherjogador("p"))
botao_pele.grid(row=0, column=1, padx=20, pady=15)

botao_cr7 = ttk.Button(frame, text="🔥 Cr7 (C)", style='Botao.TButton', command=lambda: escolherjogador("c"))
botao_cr7.grid(row=0, column=2, padx=20, pady=15)

# Label resultado destacado com sombra (duplo label)
label_resultado_bg = tk.Label(janela, text="", font=fonte_resultado, bg="#145214", fg="black")
label_resultado_bg.pack(pady=(40, 10))
label_resultado = tk.Label(janela, text="", font=fonte_resultado, bg="#145214", fg="white")
label_resultado.place(x=label_resultado_bg.winfo_x()+2, y=label_resultado_bg.winfo_y()+2)

# Atualiza label resultado de forma simples (sem sombra) por enquanto pra garantir funcionamento
label_resultado.pack(pady=(40, 10))

janela.mainloop()
