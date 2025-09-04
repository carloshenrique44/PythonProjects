import pandas as pd

tb_clientes = pd.read_excel("Dados/dados_aleatorios.xlsx", sheet_name="Aba1")
print(tb_clientes)

tb_clientes = pd.read_excel("Dados/dados_aleatorios.xlsx", index_col=0)
print(tb_clientes)

tb_clientes = pd.read_excel("Dados/dados_aleatorios.xlsx", usecols=[0,1])
print(tb_clientes)

tb_clientes_aba1 = pd.read_excel("Dados/dados_aleatorios.xlsx", sheet_name="Aba1")
tb_clientes_aba2 = pd.read_excel("Dados/dados_aleatorios.xlsx", sheet_name="Aba2")

with pd.ExcelWriter("Dados/novos_clientes.xlsx", engine="openpyxl") as nova_planilha:
    tb_clientes_aba1.to_excel(nova_planilha, sheet_name="Clientes_Aba1", index=False)
    tb_clientes_aba2.to_excel(nova_planilha, sheet_name="Clientes_Aba2", index=False)
    