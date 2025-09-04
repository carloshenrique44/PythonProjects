import sqlite3 

def conecta_bd():
    conexao = sqlite3.connect('banco.db')
    return conexao

def insere_dados(nome, sobrenome, idade):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute(
        """
        INSERT INTO funcionarios (nome, sobrenome, idade)
        VALUES (?, ?, ?)
        """, (nome, sobrenome, idade)
    )
    conexao.commit()
    conexao.close()

def obter_dados():
    conexao = conecta_bd()
    cursor = conexao.cursor()
    dados = cursor.execute("SELECT * FROM funcionarios")
    dados = dados.fetchall()
    conexao.close()
    return dados
