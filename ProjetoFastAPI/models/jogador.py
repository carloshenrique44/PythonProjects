from pydantic import BaseModel

class Jogador(BaseModel):
    jogador_nome: str
    jogador_posicao: str
    jogador_idade: int
    jogador_nacionalidade: str
    
    