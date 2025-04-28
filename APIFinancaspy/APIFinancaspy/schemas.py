from pydantic import BaseModel
from datetime import datetime

class TransacaoBase(BaseModel):
    descricao: str
    valor: float
    tipo: str
    
class TransacaoCreate(TransacaoBase):
    pass

class Transacao(TransacaoBase):
    id: int
    data: datetime
    
class TransacaoUpdate(TransacaoBase):
    pass


    class Config:
        orm_mode = True
