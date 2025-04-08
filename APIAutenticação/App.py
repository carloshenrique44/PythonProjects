from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'minha_chave_secreta'

db = SQLAlchemy(app)
jwt = JWTManager(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
    @app.before_first_request
    def criar_banco():
        db.create_all()

app.config["JWT_SECRET_KEY"] = "sua_chave_secreta"
jwt = JWTManager(app)  

users = {"admin": "1234"}

@app.route("/login", methods=["POST"])
def login():

    dados = request.json
    username = dados.get("username")
    password = dados.get("password")

    if users.get(username) == password:

        token = create_access_token(identity=username)
        return jsonify({"access_token": token})

    return jsonify({"erro": "Credenciais inválidas"}), 401

@app.route("/protegido", methods=["GET"])
@jwt_required()
def protegido():
    return jsonify({"mensagem": "Acesso permitido!"})

if __name__ == "__main__":
    app.run(debug=True)
