from pydantic import BaseModel
from typing import Optional
from fastapi_jwt_auth import AuthJWT


# Modelo de configuração para o JWT
class Settings(BaseModel):
    authjwt_secret_key: str = '20335bc5feb438fbe189aa69a9a88f5f0af8ed74b7fff2e1230a0bd25ae38e70'
    authjwt_algorithm: str = 'HS256'  # Algoritmo para assinar o JWT
    authjwt_access_token_expires: int = 3600  # Expiração do token de acesso (em segundos)
    authjwt_refresh_token_expires: int = 86400 

    class Config:
        env_file = ".env" 

@AuthJWT.load_config
def get_config():
    return Settings()


# Modelo de dados para criar um novo usuário (sign up)
class SignUpModel(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    password: str
    is_staff: Optional[bool] = False
    is_active: Optional[bool] = True

    class Config:
        from_attributes = True
        schema_extra = {
            'example': {
                'username': 'carlos',
                'email': 'atrkaike@hotmail.com',
                'password': 'password',
                'is_staff': False,
                'is_active': True
            }
        }

class LoginModel(BaseModel):
    username: str
    password: str
    
class OrderModel(BaseModel):
    id=Optional[int]
    quantity:int
    order_status:Optional[str] = 'Pendente'
    pizza_size:Optional[str] = 'Pequena'
    user_id:Optional[int]
    
class Config:
    orm_mode = True
    schema_extra = {
        "example": {
            "quantity": 2,
            "pizza_size": "Pequena",
        }
    }
