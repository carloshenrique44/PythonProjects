import os

def add_contact():
    name = input("Informe o nome:\n")
    address = input("Informe o endereço:\n")
    phone = input("Informe o telefone:\n")
    
    contact = f"Nome: {name}\nEndereço: {address}\nTelefone: {phone}\nTelefone: {phone}\n"
    
    with open("Dados/contatos.txt", "a", encoding="utf-8") as file:
        file.write(contact)
        
def view_contacts():
    if not os.path.exists("Dados/contatos.txt"):
        print("Nenhum contato encontrado.")
        return
    
    with open("Dados/contatos.txt", "r", encoding="utf-8") as file:
        contacts = file.read()
        print("Contatos:\n")
        print(contacts)
        
def delete_contact():
    if not os.path.exists("Dados/contatos.txt"):
        print("Nenhum contato encontrado.")
        return