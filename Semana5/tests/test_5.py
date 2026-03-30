from Semana5.ejercicio5 import potencia_ciclo, potencia_recursiva


def test_potencia():
    assert potencia_ciclo(2, 4) == 16, (
        "La potencia calculada con ciclo es incorrecta."
    )

    assert potencia_recursiva(2, 4) == 16, (
        "La potencia recursiva no reduce correctamente el exponente."
    )
