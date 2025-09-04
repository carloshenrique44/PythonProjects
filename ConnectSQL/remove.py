import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

id = (1, 2)
cursor.execute (
    """
    DELETE from funcionarios
    WHERE ID in (?, ?)
    """,
    id
)

conexao.commit()

print("Dados removidos com sucesso da tabela 'funcionarios'!")