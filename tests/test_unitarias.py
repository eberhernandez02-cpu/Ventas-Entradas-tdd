"""
PRUEBAS UNITARIAS (las escribes TU, el estudiante).

Aqui debes ir agregando tus propias pruebas unitarias, siguiendo el ciclo
TDD (rojo - verde - refactor), ANTES de escribir cada pequena porcion de
codigo en venta_entradas/modelos.py.

Ejemplo de como se ve una prueba unitaria (borrala y escribe las tuyas):

def test_ejemplo_evento_guarda_su_nombre():
    from venta_entradas.modelos import Evento
    evento = Evento("Teatro", aforo_maximo=10, precio_entrada=25.0)
    assert evento.nombre == "Teatro"

Recomendacion de orden sugerido (puedes seguir otro si prefieres):
1. Pruebas de la clase Evento (constructor, entradas_disponibles, etc).
2. Pruebas de SistemaVentas.registrar_evento.
3. Pruebas de SistemaVentas.vender_entradas (casos validos e invalidos).
4. Pruebas de SistemaVentas.calcular_total_con_descuento.

Para ejecutar solo tus pruebas unitarias:
    pytest tests/test_unitarias.py -v

Para ejecutar TODO (unitarias + aceptacion):
    pytest -v
"""

import pytest

from venta_entradas.modelos import Evento, SistemaVentas, VentaError


def crear_sistema(nombre="Teatro", aforo=10, precio=25.0):
    sistema = SistemaVentas()
    evento = Evento(nombre, aforo_maximo=aforo, precio_entrada=precio)
    sistema.registrar_evento(evento)
    return sistema, evento


def test_evento_guarda_los_datos_del_constructor():
    evento = Evento("Teatro", aforo_maximo=10, precio_entrada=25.0)

    assert evento.nombre == "Teatro"
    assert evento.aforo_maximo == 10
    assert evento.precio_entrada == 25.0


def test_evento_inicia_con_cero_entradas_vendidas():
    evento = Evento("Teatro", aforo_maximo=10, precio_entrada=25.0)

    assert evento.entradas_vendidas == 0


def test_entradas_disponibles_coinciden_con_aforo_al_inicio():
    evento = Evento("Teatro", aforo_maximo=10, precio_entrada=25.0)

    assert evento.entradas_disponibles == 10


def test_hay_disponibilidad_si_la_cantidad_cabe_en_el_aforo():
    evento = Evento("Teatro", aforo_maximo=10, precio_entrada=25.0)

    assert evento.hay_disponibilidad(10) is True


def test_no_hay_disponibilidad_para_cero_entradas():
    evento = Evento("Teatro", aforo_maximo=10, precio_entrada=25.0)

    assert evento.hay_disponibilidad(0) is False


def test_no_hay_disponibilidad_si_la_cantidad_excede_el_aforo():
    evento = Evento("Teatro", aforo_maximo=10, precio_entrada=25.0)

    assert evento.hay_disponibilidad(11) is False


def test_sistema_ventas_inicia_sin_eventos():
    sistema = SistemaVentas()

    assert sistema._eventos == {}


def test_registrar_evento_lo_agrega_al_sistema():
    sistema, evento = crear_sistema()

    assert sistema._eventos["Teatro"] is evento


def test_vender_entradas_devuelve_total_y_actualiza_contadores():
    sistema, evento = crear_sistema(precio=25.0)

    total = sistema.vender_entradas("Teatro", 3)

    assert total == 75.0
    assert evento.entradas_vendidas == 3
    assert evento.entradas_disponibles == 7


def test_vender_entradas_rechaza_evento_inexistente():
    sistema = SistemaVentas()

    with pytest.raises(VentaError):
        sistema.vender_entradas("Inexistente", 1)


@pytest.mark.parametrize("cantidad", [0, -1])
def test_vender_entradas_rechaza_cantidad_invalida(cantidad):
    sistema, _ = crear_sistema()

    with pytest.raises(VentaError):
        sistema.vender_entradas("Teatro", cantidad)


def test_vender_entradas_rechaza_cantidad_mayor_a_la_disponible():
    sistema, _ = crear_sistema(aforo=2)

    with pytest.raises(VentaError):
        sistema.vender_entradas("Teatro", 3)


def test_calcular_descuento_devuelve_total_sin_registrar_venta():
    sistema, evento = crear_sistema(precio=100.0)

    total = sistema.calcular_total_con_descuento("Teatro", 2, 15)

    assert total == 170.0
    assert evento.entradas_vendidas == 0


@pytest.mark.parametrize("descuento", [-1, 101])
def test_calcular_descuento_rechaza_porcentaje_fuera_de_rango(descuento):
    sistema, _ = crear_sistema()

    with pytest.raises(VentaError):
        sistema.calcular_total_con_descuento("Teatro", 1, descuento)


def test_calcular_descuento_rechaza_evento_inexistente():
    sistema = SistemaVentas()

    with pytest.raises(VentaError):
        sistema.calcular_total_con_descuento("Inexistente", 1, 10)


def test_calcular_descuento_rechaza_cantidad_invalida():
    sistema, _ = crear_sistema()

    with pytest.raises(VentaError):
        sistema.calcular_total_con_descuento("Teatro", 0, 10)
