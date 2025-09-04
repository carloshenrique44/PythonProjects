def is_positive(number):
    return number > 0

def sub(a, b):
    return a - b

def length(list):
    return len(list)

def validate_email(email):
    return '@' in email and '.' in email

def somar_lista(valores):
    """Soma os valores de uma lista"""
    if not all(isinstance(i, (int,float)) for i in valores):
        raise ValueError("Todos os elementos da lista devem ser números")
    return sum(valores)

def encontrar_valor(dicionario, chave):
    """Encontra o valor associado a uma chave em um dicionário"""
    if not isinstance(dicionario, dict):
        raise ValueError("O primeiro argumento deve ser um dicionário")
    return dicionario.get(chave, None)