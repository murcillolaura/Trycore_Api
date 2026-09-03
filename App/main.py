from fastapi import FastAPI

from App.models import Transaccion
from App.services import analizar_transacciones

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/transacciones")
def recibir_transacciones(transacciones: list[Transaccion]):
    return analizar_transacciones(transacciones)