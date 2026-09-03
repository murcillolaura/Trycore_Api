# API REST de Transacciones

API REST desarrollada en Python con FastAPI para procesar transacciones de compra y venta de productos.

## Funcionalidades

La API permite:

- Recibir transacciones de tipo `BUY` y `SELL`.
- Calcular el stock final de cada producto.
- Calcular el valor total vendido por producto.
- Identificar el producto más rentable según el valor de las ventas.
- Validar los datos recibidos.
- Permitir stock negativo.
- Procesar conjuntos de transacciones vacíos.

## Productos permitidos

- TIMBER
- GOLD
- COAL
- ALUMINIUM
- IRON

## Tecnologías utilizadas

- Python
- FastAPI
- Uvicorn
- Pydantic
- Pytest
- Pytest-cov
- HTTPX

## Instalación

Crear un entorno virtual:

```bash
python -m venv venv
```

Activar el entorno virtual en Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
pip install fastapi uvicorn pytest pytest-cov httpx
```

## Ejecutar la API

Desde la raíz del proyecto:

```bash
uvicorn App.main:app --reload
```

La API estará disponible en:

```text
http://127.0.0.1:8000
```

## Documentación Swagger

Con la API ejecutándose, abrir:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

### GET /health

Permite comprobar que la API está funcionando.

### POST /transacciones

Recibe una lista de transacciones y devuelve:

- Stock final por producto.
- Valor total vendido por producto.
- Producto más rentable.

Ejemplo de entrada:

```json
[
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
```

## Reglas de negocio

El stock se calcula sumando las cantidades de las transacciones `BUY` y restando las cantidades de las transacciones `SELL`.

El valor vendido se calcula únicamente sobre transacciones `SELL`:

```text
cantidad × valor_unitario
```

El producto más rentable es el producto con mayor valor total vendido.

## Validaciones

La API valida:

- Tipo de transacción: solamente `BUY` o `SELL`.
- Productos reconocidos.
- Cantidad mayor que cero.
- Valor unitario mayor que cero.
- Formato válido de fecha.

Los datos inválidos generan una respuesta HTTP `422`.

## Pruebas

Ejecutar todos los tests:

```bash
python -m pytest
```

Ejecutar tests y medir cobertura:

```bash
python -m pytest --cov=App --cov-report=term-missing
```

La cobertura obtenida durante el desarrollo fue del 98%.

## Persistencia

La solución no utiliza base de datos porque las transacciones se procesan en la misma petición y no se requiere persistencia para realizar los cálculos solicitados.