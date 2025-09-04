from conexao_post import conn

cursor_obj = conn.cursor ()

cursor_obj.execute("SELECT * FROM game")

result = cursor_obj.fetchall()

for row in result:
    print(f"ID: {row[0]}, Nome: {row[1]}, Gênero: {row[2]}, Ano: {row[3]}, Plataforma: {row[4]}")
    conn.close()
    
    