
def buscar_palavra(texto: str, palavra: str) -> int:
    texto = """O desenvolvimento de SoftWare Seguro é essencial para proteger Aplicações contra ameaças Virtuais, garantindo a Integridade e a Confidencialidade dos Dados. Técnicas como encriptação e Gerenciamento de Sessão são fundamentais para evitar VULNERABILIDADES exploráveis por atacantes.
    Além disso, a Implementação de boas Práticas de Codificação reduz o risco de Exploits, tornando os Sistemas mais RESILIENTES. Frameworks modernos oferecem Ferramentas para fortalecer a Autenticação e o Controle de Acesso, prevenindo Ataques como SQL Injection e Cross-Site Scripting (XSS)."""
    texto_lower = texto.lower()
    palavra_lower = palavra.lower()
    return texto_lower.find(palavra_lower)

if __name__ == "__main__":
    texto = """O desenvolvimento de SoftWare Seguro é essencial para proteger Aplicações contra ameaças Virtuais, garantindo a Integridade e a Confidencialidade dos Dados. Técnicas como encriptação e Gerenciamento de Sessão são fundamentais para evitar VULNERABILIDADES exploráveis por atacantes.
    Além disso, a Implementação de boas Práticas de Codificação reduz o risco de Exploits, tornando os Sistemas mais RESILIENTES. Frameworks modernos oferecem Ferramentas para fortalecer a Autenticação e o Controle de Acesso, prevenindo Ataques como SQL Injection e Cross-Site Scripting (XSS)."""
    palavra = input("Digite a palavra que deseja buscar: ")
    indice = buscar_palavra(texto, palavra)

    if indice != -1:
        print(f"A palavra '{palavra}' aparece pela primeira vez no índice {indice}.")
    else:
        print(f"A palavra '{palavra}' não foi encontrada no texto.")
