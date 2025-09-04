from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings
from fastapi import Depends, HTTPException, status
from app.models.user_model import User
from jose import jwt
from app.schemas.auth_schema import TokenPayLoad
from datetime import datetime
from pydantic import ValidationError
from app.services.user_service import UserService
from fastapi import APIRouter
from app.schemas.user_schema import UserDetail

auth_router = APIRouter()

oauth_reusavel = OAuth2PasswordBearer(
    tokenUrl = f"{settings.API_V1_STR}/auth/login",
    scheme_name="JWT"
)

async def get_current_user(token: str = Depends(oauth_reusavel)) -> User:
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            settings.ALGORITHM
        )
        token_data = TokenPayLoad(**payload)
        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                details="Token expirado",
                headers={"WWW-Authenticate": "Bearer"}
            )
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            details="Erro na validação do token",
            headers={"WWW-Authenticate": "Bearer"}
        )
    user = await UserService.get_user_by_id(token_data.sub)
    if not User:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            details = "Não foi possível encontrar o usuário",
            headers = {"WWW-Authenticate": "Bearer"}
        )
    return user

@auth_router.post("/teste-token", summary="Teste de autenticação", response_model=UserDetail)
async def teste_token(user: User = Depends(get_current_user)):
    return user

