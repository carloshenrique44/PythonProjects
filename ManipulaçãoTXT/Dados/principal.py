from agenda import add_contact, view_contacts, delete_contact

def main():
    while True:
        print("\nAgenda de Contatos:")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Remover Contatos")
        print("4. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")
            
if __name__ == "__main__":
    main()