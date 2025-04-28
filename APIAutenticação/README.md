API com Autenticação JWT usando Flask

Este é um projeto de estudo onde desenvolvi uma API com autenticação baseada em JWT (JSON Web Token) usando Flask, SQLAlchemy e Flask-JWT-Extended

Esse foi meu primeiro projeto usando JWT com Flask!  
Aqui eu aprendi como proteger rotas, gerar tokens e armazenar usuários com SQLAlchemy!

📦 Tecnologias utilizadas:

- Python 3
- Flask
- Flask-JWT-Extended
- Flask-SQLAlchemy
- SQLite (como banco de dados)

🔐 Como funciona a autenticação??

Login (POST /login)
Envie um JSON com username e password

Se as credenciais estiverem corretas, você recebe um access_token

Acesso Protegido (GET /protegido)
Requer o token de acesso no header

🧠 Extras
O banco de dados SQLite (usuarios.db) é criado automaticamente na primeira execução

A verificação de usuário ainda é feita manualmente com um dicionário Python (users), mas já temos a estrutura com SQLAlchemy pronta para evoluir
