def tamanhotexto():
    texto = "A segurança no desenvolvimento de software deve ser uma prioridade, e não apenas uma preocupação \"opcional\"."
    print(f"O tamanho do texto é: {len(texto)} caracteres")
    qtd_a = texto.count("a") + texto.count("A") + texto.count("ã") + texto.count("Ã")
    print(f"A letra 'a' (considerando maiúsculas, minúsculas e com acento) aparece {qtd_a} vezes no texto")
    
if __name__ == "__main__":
    tamanhotexto()