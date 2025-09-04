def mercado():
    quantidade_maçã = int(input("Digite a quantidade de maçãs compradas: "))
    quantidade_uvas = int(input("Digite a quantidade de uvas compradas: "))
    quantidade_bananas = int(input("Digite a quantidade de bananas compradas: "))
    
    preço_maçã = 1.35
    preço_uva = 2.50
    preço_banana = 1.00
    
    custo_total = (quantidade_maçã * preço_maçã) + (quantidade_uvas * preço_uva) + (quantidade_bananas * preço_banana)
    print(f"O valor total da sua compra foi de R$ {custo_total:.2f}")
    return custo_total

if __name__ == "__main__":
    mercado()
    
#Carlos Trindade
   