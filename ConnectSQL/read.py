import sqlite3

conexao = sqlite3.connect('banco.db')

cursor = conexao.cursor()

dados = cursor.execute("SELECT * from funcionarios")

print(dados.fetchall())