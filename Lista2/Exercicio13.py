def embaralhar_com_indice():
    s = input("Digite uma string: ")
    indice = int(input("Digite o índice onde deseja dividir a string: "))
    primeira_parte = s[:indice]
    segunda_parte = s[indice:]
    resultado = segunda_parte + primeira_parte
    print("String embaralhada:", resultado)


if __name__ == "__main__":
    embaralhar_com_indice()
