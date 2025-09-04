def embaralhar_metades():
    s = input("Digite uma string: ")
    meio = len(s) // 2
    primeira_metade = s[:meio]
    segunda_metade = s[meio:]
    resultado = segunda_metade + primeira_metade
    print("String embaralhada:", resultado)


if __name__ == "__main__":
    embaralhar_metades()
