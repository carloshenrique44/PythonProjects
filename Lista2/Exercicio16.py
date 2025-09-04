
def moldura():
    palavra = input("Digite uma palavra: ")
    tamanho = len(palavra)
    borda = "*" * (tamanho + 4)
    print(borda)
    print(f"* {palavra} *")
    print(borda)
    
if __name__ == "__main__":
    moldura()