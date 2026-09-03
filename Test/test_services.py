from App.models import Transaccion
from App.services import (
    calcular_stock,
    calcular_valor_ventas,
    obtener_producto_mas_rentable
)


def test_calcular_stock():
    transacciones = [
        Transaccion(
            tipo="BUY",
            fecha="2026-09-03",
            producto="TIMBER",
            cantidad=10,
            valor_unitario=50
        ),
        Transaccion(
            tipo="SELL",
            fecha="2026-09-03",
            producto="TIMBER",
            cantidad=3,
            valor_unitario=70
        )
    ]

    resultado = calcular_stock(transacciones)

    assert resultado["TIMBER"] == 7


def test_stock_negativo():
    transacciones = [
        Transaccion(
            tipo="SELL",
            fecha="2026-09-03",
            producto="IRON",
            cantidad=8,
            valor_unitario=20
        )
    ]

    resultado = calcular_stock(transacciones)

    assert resultado["IRON"] == -8


def test_stock_sin_transacciones():
    transacciones = []

    resultado = calcular_stock(transacciones)

    assert resultado["TIMBER"] == 0
    assert resultado["GOLD"] == 0
    assert resultado["COAL"] == 0
    assert resultado["ALUMINIUM"] == 0
    assert resultado["IRON"] == 0


def test_calcular_valor_ventas():
    transacciones = [
        Transaccion(
            tipo="SELL",
            fecha="2026-09-03",
            producto="GOLD",
            cantidad=2,
            valor_unitario=200
        ),
        Transaccion(
            tipo="SELL",
            fecha="2026-09-03",
            producto="GOLD",
            cantidad=3,
            valor_unitario=100
        )
    ]

    resultado = calcular_valor_ventas(transacciones)

    assert resultado["GOLD"] == 700


def test_producto_mas_rentable():
    ventas = {
        "TIMBER": 210,
        "GOLD": 700,
        "COAL": 120,
        "ALUMINIUM": 0,
        "IRON": 540
    }

    resultado = obtener_producto_mas_rentable(ventas)

    assert resultado == "GOLD"