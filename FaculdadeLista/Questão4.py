def media():
    media1 = int(input("Digite a primeira média: "))
    media2 = int(input("Digite a segunda média: "))
    media3 = int(input("Digite a terceira média: "))
    media4 = int(input("Digite a quarta média: "))
    media_final = (media1 + media2 + media3 + media4)/4
    print(f"A média final é: {media_final}")
    return media_final

if __name__ == "__main__":
    media()
    
#Carlos Trindade