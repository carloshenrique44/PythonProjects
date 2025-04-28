from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from APIFinancaspy.database import Base

class Transacao(Base):
    __tablename__ = "transacoes"
    
    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, index=True)
    valor = (Column(Float, nullable=False))
    tipo = Column(String, nullable=False)
    data = Column(DateTime, default=datetime.utcnow)