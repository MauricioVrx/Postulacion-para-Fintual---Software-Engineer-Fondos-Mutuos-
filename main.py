from stocks import Stock, Portfolio

def rebalance_portfolio(portfolio, allocation):
    try:
        return portfolio.rebalance(allocation)
    except ValueError as e:
        print(f"Error: {e}")
        return None


def main():
    # Crea acciones disponibles
    meta = Stock("META", 485.75)
    aapl = Stock("AAPL", 172.35)
    amzn = Stock("AMZN", 262.35)
    msft = Stock("MSFT", 407.54)

    # Crear portafolio
    mi_portafolio = Portfolio()

    # Añadir acciones al portafolio
    mi_portafolio.add_stock(meta)
    mi_portafolio.add_stock(aapl)
    mi_portafolio.add_stock(amzn)
    mi_portafolio.add_stock(msft,2)

    # Actualizar acción al portafolio
    mi_portafolio.update_holding_quantity('META',2)

    # Establecer objetivo
    allocation_porc = {"META":0.4, "AAPL":0.6}

    # Calcular transacciones de rebalanceo
    result = rebalance_portfolio(mi_portafolio, allocation_porc)
    print(result)

    # Modificar valor de la accion de 'META'
    meta.update_price(253.15)

    # Calcular transacciones de rebalanceo con la accion con otro valor
    result = rebalance_portfolio(mi_portafolio, allocation_porc)
    print(result)


if __name__ == "__main__":
    main()