from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///banco.db", echo=True)


Base = declarative_base()

class Funcionario(Base):
    __tablename__ = 'funcionarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    sobrenome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)

Base.metadata.create_all(engine)

def adiciona_funcionario(nome, sobrenome, idade):
    Session = sessionmaker(bind=engine)
    session = Session()
    funcionario = Funcionario(nome=nome, sobrenome= sobrenome, idade=idade)
    session.add(funcionario)
    session.commit()
    session.close()
    
adiciona_funcionario('João', 'Zeni', 22)
adiciona_funcionario('Maria', 'Silva', 28)

def atualiza_funcionario(id, nome=None, sobrenome=None, idade=None):
    Session = sessionmaker(bind=engine)
    session = Session()
    funcionario = session.query(Funcionario).filter_by(id=id).first()
    if funcionario:
        if nome is not None:
            funcionario.nome = nome
        if sobrenome is not None:
            funcionario.sobrenome = sobrenome
        if idade is not None:
            funcionario.idade = idade
        session.commit()
        session.close()
        
def exclui_funcionario(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    funcionario = session.query(Funcionario).filter_by(id=id).first()
    if funcionario:
        session.delete(funcionario)
        session.commit()
    session.close()
