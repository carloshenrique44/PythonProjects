from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import APIFinancaspy.models as models, APIFinancaspy.schemas as schemas, APIFinancaspy.crud as crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/transacoes/", response_model=list[schemas.Transacao])
def listar_transacoes(db: Session = Depends(get_db)):
    return crud.get_transacoes(db)

@app.get("/transacoes/{transacao_id}", response_model=schemas.Transacao)
def buscar_transacao(transacao_id: int, db: Session = Depends(get_db)):
    transacao = crud.get_transacao(db, transacao_id)
    if not transacao:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    return transacao

@app.post("/transacoes/", response_model=schemas.Transacao)
def criar_transacao(transacao: schemas.TransacaoCreate, db: Session = Depends(get_db)):
    return crud.create_transacao(db, transacao)

@app.delete("/transacoes/{transacao_id}")
def deletar_transacao(transacao_id: int, db: Session = Depends(get_db)):
    transacao = crud.delete_transacao(db, transacao_id)
    if not transacao:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    return {"ok": True}

@app.put("/transacoes/{transacao_id}", response_model=schemas.Transacao)
def atualizar_transacao(transacao_id: int, transacao: schemas.TransacaoCreate, db: Session = Depends(get_db)):
    transacao_atualizada = crud.update_transacao(db, transacao_id, transacao)
    if not transacao_atualizada:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    return transacao_atualizada

@app.get("/transacoes/total/{tipo}", response_model=schemas.TotalTransacao)
def calcular_total(tipo: str, db: Session = Depends(get_db)):
    if tipo not in ["entrada", "saida"]:
        raise HTTPException(status_code=400, detail="Tipo inválido. Use 'entrada' ou 'saida'.")
    total = crud.calcular_total(db, tipo)
    return {"total": total}
