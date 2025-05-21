from flask import Flask, jsonify, request

app = Flask (__name__)

@app.route('/home', methods = ['GET'])
def home():
    return jsonify({"message": "Bem vindo a pagina inicial"})

