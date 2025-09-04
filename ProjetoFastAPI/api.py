from fastapi import FastAPI, HTTPException
from routes.jogador import jogador_router

app = FastAPI()

app.include_router(jogador_router)