# Postulación para Fintual – Software Engineer Fondos Mutuos (Con Python 3.11.10)

Este repositorio contiene la solución al ejercicio técnico solicitado por Fintual como parte del proceso de postulación al squad de Fondos Mutuos. Se desarrolla un sistema básico para gestionar un portafolio de acciones, incluyendo la capacidad de rebalancear activos según una asignación deseada.

## 🧠 Descripción del problemas

> **Construct a simple `Portfolio` class that has a collection of `Stocks`. Assume each `Stock` has a “Current Price” method that receives the last available price. Also, the `Portfolio` class has a collection of “allocated” Stocks that represents the distribution of the Stocks the Portfolio is aiming (i.e. 40% META, 60% AAPL). Provide a portfolio rebalance method to know which Stocks should be sold and which ones should be bought to have a balanced Portfolio based on the portfolio’s allocation. Add documentation/comments to understand your thinking process and solution.**

---

## 🚀 Solución

La solución consiste en dos clases principales:

### `Stock`

Representa una acción individual con su símbolo y precio actualizado. Permite actualizar su precio con el método `update_price()` y obtener el precio actual con `current_price()`.


### `Portfolio`
Encargada de:

- Agregar acciones disponibles (add_stock)
- Asignar cantidades actuales de cada acción (update_holding_quantity)
- Calcular el valor total actual del portafolio (get_total_value)
- Verificar si una acción existe en el portafolio (stock_exists)
- Validar que la asignación deseada sume 100% (check_percentage_allocation)
- Rebalancear el portafolio con base en una asignación objetivo (rebalance)

#### Método rebalance(allocation_dict)
Esta función compara la asignación actual del portafolio contra la asignación deseada y determina qué acciones comprar o vender para alcanzar ese equilibrio. El resultado es una lista de transacciones del tipo:

```
[('META', 'SELL', 1.23), ('AAPL', 'BUY', 2.34)]
```
Además, se aplican automáticamente las operaciones calculadas al portafolio.

## 📄 Estructura del proyecto
```
.
├── main.py        # Script principal que instancia y prueba la solución
├── stocks.py      # Clases Stock y Portfolio
├── README.md      # Este archivo
```

## 🧪 Ejemplo de ejecución
```
python main.py
```
Salida esperada (puede variar si cambian los precios):
```
[('AMZN', 'SELL', 2), ('META', 'SELL', 0.85), ('AAPL', 'BUY', 3.32)]
[('META', 'BUY', 1.98), ('AAPL', 'SELL', 2.82)]
```

## 🧩 Uso de LLMs
Se utilizó deepseek para:
1. Mayormente para entender la tarea, generando una definición más amplia a lo que se refería, tanto términos como descripción general ('puedes traducirme esto al español y despues explicarmelo porfavor:...' )
2. Asistencia con los nombres en inglés de funciones respecto a lo deben realizar, dandole el contexto que realizan la funciones
3. Conversación al respecto del ejercicio ya que no entendía del todo la parte del rebalanceo de acciones ("dime si estoy bien:  Para realizar el rebalanceo (rebalance), primero debo sacar el valor total actual de las acciones(total_actual), luego calcular la compra venta de las acciones en base de los porcentajes 0.4(40% META) y 0.6(60% APPL) y la sumas debe ser igual que la primera suma(total_actual)?")
4. Generar parte de la documentación
5. Generar el formato del archivo "readme.md"
---

## Por qué esta Solución
1. Clara y concisa: Implementación directa que resuelve el problema central
2. Extensible: Diseñada para fácil incorporación de nuevas funcionalidades
3. Robusta: Manejo adecuado de casos límite y errores
4. Documentada: Comentarios que explican el razonamiento detrás de cada decisión
5. Práctica: Incluye ejemplos ejecutables que demuestran el funcionamiento
