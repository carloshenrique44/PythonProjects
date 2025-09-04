def firstandlast():
    nome = input("Digite seu nome completo: ")
    partes = nome.split()
    print("Primeiro nome:", partes[0])
    print("Ultimo sobrenome:", partes[-1])
    
if __name__ == "__main__":
    firstandlast()
    