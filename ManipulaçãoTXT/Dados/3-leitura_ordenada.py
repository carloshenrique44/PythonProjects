names = []

with open("Dados/names.txt", "r", encoding="utf-8") as file:
    for line in file:
        names.append(line.rstrip())
        
for name in sorted (names, reverse=True):
    print(f"Olá, {name}")