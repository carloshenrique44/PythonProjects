def converter_data():
    data_americana = input("Digite a data no formato MM/DD/YYYY: ")
    partes = data_americana.split("/")
    mes = partes[0]
    dia = partes[1]
    ano = partes[2]
    data_brasileira = f"{dia}/{mes}/{ano}"
    print("Data no formato brasileiro:", data_brasileira)


if __name__ == "__main__":
    converter_data()
