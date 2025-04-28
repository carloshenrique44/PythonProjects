Automação de Consulta de CPF com Selenium e Excel

Projeto criado com base no vídeo do canal [Dev Aprender | Jhonatan de Souza](https://www.youtube.com/@DevAprender), com algumas adaptações pessoais

Este script automatiza a consulta de CPF em um site e registra os dados em uma planilha de fechamento com base na situação do cliente

🚀 Tecnologias utilizadas

- [Python](https://www.python.org/)
- [Selenium](https://pypi.org/project/selenium/)
- [openpyxl](https://pypi.org/project/openpyxl/)
- [Google Chrome](https://www.google.com/chrome/)

📂 Estrutura

- `dados_clientes.xlsx` → Planilha com os dados de entrada dos clientes (nome, valor, CPF, vencimento).
- `planilha fechamento.xlsx` → Planilha onde os resultados da consulta são armazenados.

O que o script faz?

1. Abre o navegador automaticamente
2. Lê os dados dos clientes de uma planilha Excel
3. Para cada CPF:
   - Pesquisa no site: [`https://consultcpf-devaprender.netlify.app/`](https://consultcpf-devaprender.netlify.app/)
   - Verifica se o cliente está "em dia" ou "pendente"
   - Salva os resultados em outra planilha (`planilha fechamento.xlsx`), incluindo data e método de pagamento (quando disponível)
  
Possibilidades futuras
Adicionar logs para auditoria

Validar campos da planilha antes da consulta

Criar uma interface gráfica simples (GUI)

