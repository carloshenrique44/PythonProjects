def substituir_caractere():
    s = input("Digite uma string: ")
    ch1 = input("Digite o caractere que deseja substituir: ")
    ch2 = input("Digite o caractere pelo qual deseja substituir: ")
    resultado = s.replace(ch1, ch2)
    print("String resultante:", resultado)


if __name__ == "__main__":
    substituir_caractere()
