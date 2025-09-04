import sqlite3

conexao = sqlite3.connect('banco.db')

cursor = conexao.cursor()

cursor.execute(
    """
    CREATE TABLE funcionarios (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        sobrenome TEXT NOT NULL,
        idade INTEGER NOT NULL
    );
    """
)

conexao.close()
print("Tabela 'funcionarios' criada com sucesso!")