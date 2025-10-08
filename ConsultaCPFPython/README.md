Automação de Consulta de CPF com Selenium & OpenPyXL

Um projeto prático de **automação web com Python**, desenvolvido para **ler dados de uma planilha Excel**, consultar o **status de pagamento de clientes via navegador automatizado** e registrar o resultado em uma nova planilha de fechamento.  

Este projeto foi inspirado em **tarefas reais de automação de processos financeiros**, reduzindo o trabalho manual e aumentando a eficiência no controle de clientes.

---

Visão Geral

O script realiza as seguintes etapas de forma automática:

1. Lê os dados de clientes a partir de um arquivo Excel (`dados_clientes.xlsx`), contendo:
   - Nome  
   - Valor  
   - CPF  
   - Vencimento  

2. Acessa o site de consulta [`https://consultcpf-devaprender.netlify.app/`](https://consultcpf-devaprender.netlify.app/) usando **Selenium**.  

3. Para cada cliente, insere o CPF no campo de busca e clica no botão de consulta.

4. Analisa o resultado:
   - Se o cliente estiver **“em dia”**, captura a **data** e o **método de pagamento** exibidos.
   - Caso contrário, marca o status como **“pendente”**.

5. Grava as informações coletadas em uma planilha de fechamento (`planilha fechamento.xlsx`), gerando um histórico automático.

---

## ⚙️ Tecnologias Utilizadas

| Ferramenta | Função |
|-------------|---------|
| 🐍 **Python 3** | Linguagem principal |
| 📘 **OpenPyXL** | Manipulação de planilhas Excel |
| 🌐 **Selenium WebDriver (Chrome)** | Automação do navegador |
| ⏱️ **time.sleep()** | Controle de tempo entre ações |
