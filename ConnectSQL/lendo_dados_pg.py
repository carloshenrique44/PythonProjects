from conexao_post import conn

cursor_obj = conn.cursor()

cursor_obj.execute ("SELECT * FROM game" )

result = cursor_obj.fetchall()
