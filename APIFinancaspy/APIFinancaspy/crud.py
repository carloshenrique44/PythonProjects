from sqlalchemy.orm import Session

from . import models
from . import schemas

def get_transacoes(db: Session):
    return db.query(models.Transacao).all()

def get_transacao(db: Session, transacao_id: int):
    return db.query(models.Transacao).filter(models.Transacao.id == transacao_id == transacao_id).first()

def create_transacao(db: Session, transacao: schemas.TransacaoCreate):
    db_transacao = models.Transacao(**transacao.dict())
    db.add(db_transacao)
    db.commit()
    db.refresh(db_transacao)
    return db_transacao

def delete_transacao(db: Session, transacao_id: int):
    transacao = db.query(models.Transacao).filter(models.Transacao.id == transacao_id).first()
    if transacao:
        db.delete(transacao)
        db .commit()
        
    return transacao

def update_transacao(db: Session, transacao_id: int, transacao_update: schemas.TransacaoUpdate):
    transacao = db.query(models.Transacao).filter(models.Transacao.id == transacao_id).first()
    if transacao:
        for key, value in transacao_update.dict().items():
            setattr(transacao, key, value)
            db.commit()
            db.refresh(transacao)
    return transacao