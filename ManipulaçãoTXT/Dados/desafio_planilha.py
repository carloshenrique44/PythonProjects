import pandas as pd
import os
from pathlib import Path

tb_clientes_dict = pd.read_excel("Dados/novos_clientes.xlsx", sheet_name=None)
print(tb_clientes_dict)

pasta_saida = "Dados/planilhas_separadas"
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)
    
for nome_aba, tabela in tb_clientes_dict.items():
    caminho_arquivo = os.path.join(pasta_saida, f"{nome_aba}.xlsx")
    tabela.to_excel(caminho_arquivo, index=False)
    
pasta_consolidada = "Dados/planilhas_consolidadas"
if not os.path.exists(pasta_consolidada):
    os.makedirs(pasta_consolidada)
    
caminho_arquivo_consolidado = os.path.join(pasta_consolidada, "clientes.xlsx")
with pd.ExcelWriter(caminho_arquivo_consolidado) as consolidada:
    for arquivo in Path(pasta_saida).glob("*.xlsx"):
        tabela = pd.read_excel(arquivo)
        tabela.to_excel(consolidada, sheet_name=arquivo.stem, index=False)