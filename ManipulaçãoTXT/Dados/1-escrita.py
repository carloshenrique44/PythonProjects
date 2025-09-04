name = input("Digite o nome do aluno:\n")

# file = open("Dados/names.txt", "a")
# file.write(f"{name}\n")
# file.close()

with open("Dados/names.txt", "a", encoding="utf-8") as file:
    file.write(f"{name}\n")