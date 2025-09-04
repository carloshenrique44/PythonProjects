import tkinter as tk
import orm
from tkinter import messagebox

def adiciona_funcionario():
    nome = entry_nome.get()
    sobrenome = entry_sobrenome.get()
    idade = entry_idade.get()
    orm.adiciona_funcionario(nome, sobrenome, idade)
    messagebox.showinfo("Sucesso", "Funcionário adicionado com sucesso!")
    
def atualiza_funcionario():
    id = entry_id.get()
    nome = entry_nome.get()
    sobrenome = entry_sobrenome.get()
    idade = entry_idade.get()
    orm.atualiza_funcionario(id, nome, sobrenome, idade)
    messagebox.showinfo("Sucesso", "Funcionário atualizado com sucesso!")
    
def exclui_funcionario():
    id = entry_id.get()
    orm.exclui_funcionario(id)
    messagebox.showinfo("Sucesso", "Funcionário excluído com sucesso!")
    
root = tk.Tk()
root.title("Gerenciamento de Funcionários")
label_id = tk.Label(root, text="ID:")
label_id.grid(row=0, column=0)
entry_id = tk.Entry(root, width=50)
entry_id.grid(row=0, column=1, padx=10, pady=5)

label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=1, column=0)
entry_nome = tk.Entry(root, width=50)
entry_nome.grid(row=1, column=1, padx=10, pady=5)

label_sobrenome = tk.Label(root, text="Sobrenome:")
label_sobrenome.grid(row=2, column=0)
entry_sobrenome = tk.Entry(root, width=50)
entry_sobrenome.grid(row=2, column=1, padx=10, pady=5)

label_idade = tk.Label(root, text="Idade:")
label_idade.grid(row=3, column=0)
entry_idade = tk.Entry(root, width=50)
entry_idade.grid(row=3, column=1, padx=10, pady=5)

button_adicionar = tk.Button(root, text="Adicionar Funcionario", command=adiciona_funcionario)
button_adicionar.grid(row=4, column=0, columnspan=2, pady=5)

button_atualizar = tk.Button(root, text="Atualizar Funcionario", command=atualiza_funcionario)
button_atualizar.grid(row=5, column=0, columnspan=2, pady=5)

button_excluir = tk.Button(root, text="Excluir Funcionario", command=exclui_funcionario)
button_excluir.grid(row=6, column=0, columnspan=2, pady=5)
root.mainloop()