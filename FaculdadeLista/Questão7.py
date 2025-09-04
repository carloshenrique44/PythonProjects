def peixes():
    peso = float(input("Digite o peso do peixe em kg: "))
    excesso = max(0, peso - 50)
    multa = excesso * 4.00
    print(f"O peso do peixe é: {peso} kg")
    print(f"O excesso de peso é: {excesso} kg")
    print(f"A multa a ser paga é: R$ {multa:.2f}")
    return peso, excesso, multa

if __name__ == "__main__":
    peixes()
    
#Carlos Trindade