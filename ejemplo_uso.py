"""Demostracion ejecutable del MVP de venta de entradas."""

from venta_entradas.modelos import Evento, SistemaVentas, VentaError


if __name__ == "__main__":
    sistema = SistemaVentas()
    concierto = Evento("Concierto Rock", aforo_maximo=100, precio_entrada=50.0)
    sistema.registrar_evento(concierto)

    print("SISTEMA DE VENTA DE ENTRADAS")
    print(f"Evento: {concierto.nombre}")
    print(f"Aforo disponible: {concierto.entradas_disponibles}")

    total_estimado = sistema.calcular_total_con_descuento(
        "Concierto Rock", cantidad=3, porcentaje_descuento=10
    )
    print(f"Cotizacion: 3 entradas con 10% de descuento = Q{total_estimado:.2f}")

    try:
        total_pagado = sistema.vender_entradas("Concierto Rock", 3)
        print(f"Venta realizada: Q{total_pagado:.2f}")
        print(f"Entradas vendidas: {concierto.entradas_vendidas}")
        print(f"Entradas disponibles: {concierto.entradas_disponibles}")
    except VentaError as error:
        print(f"No se pudo completar la venta: {error}")
