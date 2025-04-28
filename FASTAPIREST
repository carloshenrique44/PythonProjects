from fastapi import FastAPI

app =  FastAPI()

Produtos = [
    {
        "id": 1,
        "nome": "Carro",
        "descricao": "Carro esportivo",
        "preco": 100000.00,
        "disponivel": True,
    },
    {
        "id": 2,
        "nome": "Moto",
        "descricao": "Moto esportiva",
        "preco": 50000.00,
        "disponivel": True,
    },
    {
        "id": 3,
        "nome": "Bicicleta",
        "descricao": "Bicicleta esportiva",
        "preco": 2000.00,
        "disponivel": True,
    }
]

@app.get("/produtos")
def listar_produtos():
    return Produtos

@app.get("/produtos/{produto_id}", tags=["Produtos"])
def obter_produto(produto_id: int):
    for produto in Produtos:
        if produto["id"] == produto_id:
            return produto
    return {"erro": "Produto não encontrado"}

@app.post("*produtos", tags=["Produtos"])
def criar_produto(produto: dict):
    novo_id = len(Produtos) + 1
    produto["id"] = novo_id
    Produtos.append(produto)
    return produto

@app.put("/produtos/{produto_id}", tags=["Produtos"])
def  atualizar_produto(produto_id: int, produto_atualizado: dict):
    for produto in Produtos:
        if produto["id"] == produto_id:
            produto.update(produto_atualizado)
            return produto
    return {"erro": "Produto não encontrado"}

@app.delete("/produtos/{produto_id}", tags=["Produtos"])
def deletar_produto(produto_id: int):
    for produto in Produtos:
        if produto["id"] == produto_id:
            Produtos.remove(produto)
            return {"mensagem": "Produto deletado com sucesso"}
    return {"erro": "Produto não encontrado"}

