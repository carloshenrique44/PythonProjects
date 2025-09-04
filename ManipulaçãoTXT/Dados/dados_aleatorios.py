import pandas as pd
import numpy as np

dados_aba1 = {
    "ID": [1, 2, 3, 4, 5],
    "Nome": ["Ana", "Carlos", "Lucas", "Fernanda", "João"],
    "Idade": [23, 30, 22, 25, 28],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Porto Alegre"],
}

dados_aba2 = {
    "ID": [1, 2, 3, 4, 5],
    "Nome": ["Fernando", "Mariana", "Roberto", "Patrícia", "Sofia"],
    "Idade": [29, 31, 24, 27, 26],
    "Cidade": ["Salvador", "Fortaleza", "Recife", "Manaus", "Goiânia"],
}

dados_aba3 = {
    "ID": [1, 2, 3, 4, 5],
    "Nome": ["Eduardo", "Camila", "Rafael", "Juliana", "Thiago"],
    "Idade": [32, 29, 30, 28, 27],
    "Cidade": ["Brasília", "Natal", "Florianópolis", "João Pessoa", "Campo Grande"],
}

dados_aba4 = {
    "ID": [1, 2, 3, 4, 5],
    "Nome": ["Isabela", "Gustavo", "Mariana", "Leonardo", "Aline"],
    "Idade": [26, 33, 25, 31, 29],
    "Cidade": ["Vitória", "Maceió", "Teresina", "Aracaju", "Palmas"],
}

df_aba1 = pd.DataFrame(dados_aba1)
df_data2 = pd.DataFrame(dados_aba2)
df_data3 = pd.DataFrame(dados_aba3)
df_data4 = pd.DataFrame(dados_aba4)

caminho_arquivo = "Dados/dados_aleatorios.xlsx"

with pd.ExcelWriter(caminho_arquivo, engine="openpyxl") as writer:
    df_aba1.to_excel(writer, sheet_name="Aba1", index=False)
    df_data2.to_excel(writer, sheet_name="Aba2", index=False)
    df_data3.to_excel(writer, sheet_name="Aba3", index=False)
    df_data4.to_excel(writer, sheet_name="Aba4", index=False)
    
print(f"Arquivo {caminho_arquivo} criado com sucesso!")