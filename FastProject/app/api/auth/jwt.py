from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from app.services.user_service import UserService
from app.core.security import create_access_token, create_refresh_token
from app.schemas.auth_schema import TokenSchema
from app.schemas.user_schema import UserDetail
from app.models.user_model import User
from app.api.dependencies.user_deps import get_current_user
from pydantic import ValidationError
from app.core.config import settings
from app.schemas.auth_schema import TokenPayLoad
from jose import jwt

auth_router = APIRouter()

@auth_router.post('/login', summary='Cria Access Token e Refresh Token', response_model=TokenSchema)
async def login(data: OAuth2PasswordRequestForm = Depends()) -> Any:
    usuario = await UserService.authenticate(
        email=data.username,
        password=data.password
    )
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='E-mail ou Senha estão incorretos'
        )
    
    return {
        "access_token" : create_access_token(usuario.user_id),
        "refresh_token": create_refresh_token(usuario.user_id)
    }

@auth_router.post('/test-token', summary='Testando o Token', response_model=UserDetail)
async def test_token(user: User = Depends(get_current_user)):
    return user

@auth_router.post('/refresh', summary='Refresh Token', response_model=TokenSchema)
async def refresh_token(refresh_token: str = Body(...)):
    try:
        payload = jwt.decode(
            refresh_token,
            settings.JWT_REFRESH_SECRET_KEY,
            settings.ALGORITHM
        )
        token_data = TokenPayload(**payload)
    except:
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            details='Token inválido',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    user = await UserService.get_user_by_id(token_data.sub)

    if not User:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            details = 'Não foi possível encontrar o usuário',
            headers = {'WWW-Authenticate': 'Bearer'}
        )
    
    return {
        "access_token": create_access_token(user.user_id),
        "refresh_token": create_refresh_token(user.user_id)
    }