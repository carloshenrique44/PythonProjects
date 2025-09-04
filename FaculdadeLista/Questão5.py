def tintas():
    tamanho = input("Digite o tamanho da área em metros quadrados: ")
    tamanho = float(tamanho)
    rendimento = 3 
    litros_necessarios = tamanho / rendimento
    latas_necessarias = litros_necessarios / 18 
    preço_lata = 80.00
    custo_total = latas_necessarias * preço_lata
    print(f"Você precisará de {latas_necessarias:.2f} latas de tinta")
    print(f"O custo total será de R$ {custo_total:.2f}")
    return latas_necessarias, custo_total

if __name__ == "__main__":
    tintas()
    
#Carlos Trindade