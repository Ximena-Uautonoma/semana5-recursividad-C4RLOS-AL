from Semana5.ejercicio4 import contar_pares_ciclo, contar_pares_recursivo


def test_contar_pares():
    assert contar_pares_ciclo(10) == 5, (
        "La solución con ciclo no cuenta correctamente los números pares."
    )

    assert contar_pares_recursivo(10) == 5, (
        "La solución recursiva no cuenta correctamente los números pares."
    )
