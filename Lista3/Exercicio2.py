def comparartamanho():
    palavra1 = input("Digite uma palavra: ")
    palavra2 = input("Digite outra palavra: ")
    
    if len(palavra1) > len(palavra2):
        print(f"A palavra '{palavra1}' é maior que a palavra '{palavra2}'.")
    elif len(palavra1) < len(palavra2):
        print(f"A palavra '{palavra2}' é maior que a palavra '{palavra1}'.")
    else:
        print("As duas palavras têm o mesmo tamanho.")
        
if __name__ == "__main__":
    comparartamanho()