from conexao_post import conn

cursor_obj = conn.cursor()

games = [
    ('Star Wars Survivor', 'Aventura', 2023, 'PS5'),
    ('Midnight Club', 'Corrida', 2023, 'PS5'),
]

for game in games:
    cursor_obj.execute (
        """
        INSERT INTO game (name, genre, year, platform)
        VALUES (%s, %s, %s, %s)
        """,
    )
    
conn.commit()
print("Dados inseridos com sucesso!")
conn.close()