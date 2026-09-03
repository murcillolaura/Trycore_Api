from fastapi.testclient import TestClient

from App.main import app


cliente = TestClient(app)


def test_health():
    respuesta = cliente.get("/health")

    assert respuesta.status_code == 200
    assert respuesta.json() == {"status": "ok"}


def test_transacciones():
    datos = [
        {
            "tipo": "BUY",
            "fecha": "2026-09-03",
            "producto": "TIMBER",
            "cantidad": 10,
            "valor_unitario": 50
        },
        {
            "tipo": "SELL",
            "fecha": "2026-09-03",
            "producto": "TIMBER",
            "cantidad": 3,
            "valor_unitario": 70
        }
    ]

    respuesta = cliente.post("/transacciones", json=datos)

    assert respuesta.status_code == 200

    resultado = respuesta.json()

    assert resultado["stock"]["TIMBER"] == 7
    assert resultado["valor_ventas"]["TIMBER"] == 210
    assert resultado["producto_mas_rentable"] == "TIMBER"