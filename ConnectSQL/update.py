import sqlite3

conexao = sqlite3.connect('banco.db')

cursor = conexao.cursor()

id = 1
cursor.execute(
    """
    Update funcionarios set nome = ?
    Where id = ?
    """,
    ('João Zeni', id)
)

conexao.commit()
print("Dados atualizados com sucesso na tabela 'funcionarios'!")