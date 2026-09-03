from App.models import Transaccion


PRODUCTOS = ["TIMBER", "GOLD", "COAL", "ALUMINIUM", "IRON"]


def calcular_stock(transacciones: list[Transaccion]):
    stock = {
        "TIMBER": 0,
        "GOLD": 0,
        "COAL": 0,
        "ALUMINIUM": 0,
        "IRON": 0
    }

    for transaccion in transacciones:
        if transaccion.tipo == "BUY":
            stock[transaccion.producto] += transaccion.cantidad
        else:
            stock[transaccion.producto] -= transaccion.cantidad

    return stock

def calcular_valor_ventas(transacciones: list[Transaccion]):
    ventas = {
        "TIMBER": 0,
        "GOLD": 0,
        "COAL": 0,
        "ALUMINIUM": 0,
        "IRON": 0
    }

    for transaccion in transacciones:
        if transaccion.tipo == "SELL":
            ventas[transaccion.producto] += (transaccion.cantidad * transaccion.valor_unitario)

    return ventas

def obtener_producto_mas_rentable(ventas: dict):
    if all(valor == 0 for valor in ventas.values()):
        return None

    return max(ventas, key=ventas.get)

def analizar_transacciones(transacciones: list[Transaccion]):
    stock = calcular_stock(transacciones)
    ventas = calcular_valor_ventas(transacciones)
    producto_mas_rentable = obtener_producto_mas_rentable(ventas)

    return {
        "stock": stock,
        "valor_ventas": ventas,
        "producto_mas_rentable": producto_mas_rentable
    }