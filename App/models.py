from datetime import date
from typing import Literal

from pydantic import BaseModel, Field


class Transaccion(BaseModel):
    tipo: Literal["BUY", "SELL"]
    fecha: date
    producto: Literal["TIMBER", "GOLD", "COAL", "ALUMINIUM", "IRON"]
    cantidad: int = Field(gt=0)
    valor_unitario: float = Field(gt=0)