# Venta de Entradas - MVP con TDD

MVP desarrollado para la Actividad 2 mediante TDD y pruebas de aceptación.

## Requisitos

- Python 3.9 o superior
- pip

## Instalacion

```
pip install pytest
```

## Ejecucion

Para ejecutar el ejemplo funcional:

```bash
python ejemplo_uso.py
```

Para ejecutar todas las pruebas:

```bash
pytest -v
```

## Estructura

```
venta_entradas/
    modelos.py         <- logica del dominio
tests/
    test_aceptacion.py <- pruebas de aceptacion, NO MODIFICAR
    test_unitarias.py  <- pruebas unitarias desarrolladas con TDD
ejemplo_uso.py         <- demostracion del MVP
```

## Como trabajar

El desarrollo siguio tres pasos:

1. Se ejecutaron las pruebas de aceptacion del proyecto base para comprobar
   que las siete fallaban por `NotImplementedError` (rojo).

```
pytest tests/test_aceptacion.py -v
```

2. Se escribieron pruebas unitarias pequenas antes de implementar cada
   comportamiento. Luego se agrego el codigo minimo necesario (verde).

3. Se refactorizo la solucion y se ejecutaron todas las pruebas:

```
pytest -v
```

El resultado final esperado es de 25 pruebas aprobadas: 18 unitarias y 7 de
aceptacion.
