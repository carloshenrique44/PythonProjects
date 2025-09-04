texto = """O desenvolvimento de SoftWare Seguro é essencial para proteger Aplicações contra ameaças Virtuais, garantindo a Integridade e a Confidencialidade dos Dados. Técnicas como encriptação e Gerenciamento de Sessão são fundamentais para evitar VULNERABILIDADES exploráveis por atacantes.
Além disso, a Implementação de boas Práticas de Codificação reduz o risco de Exploits, tornando os Sistemas mais RESILIENTES. Frameworks modernos oferecem Ferramentas para fortalecer a Autenticação e o Controle de Acesso, prevenindo Ataques como SQL Injection e Cross-Site Scripting (XSS)."""

def corrigir_texto(texto: str) -> str:
    texto_corrigido = texto.replace("SoftWare", "Software") \
                           .replace("RESILIENTES", "resilientes") \
                           .replace("VULNERABILIDADES", "vulnerabilidades")
    return texto_corrigido

if __name__ == "__main__":
    novo_texto = corrigir_texto(texto)
    print(novo_texto)
