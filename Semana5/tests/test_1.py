from Semana5.ejercicio1 import contar_ciclo, contar_recursivo

def test_contar_hasta_n():
    esperado = [1, 2, 3, 4, 5]
    assert contar_ciclo(5) == esperado, (
        "La solución con ciclo no genera correctamente la lista de números."
    )
    assert contar_recursivo(5) == esperado, (
        "La solución recursiva no genera correctamente la lista. "
        "Revise el caso base y la llamada recursiva."
    )

def test_ambas_soluciones_coinciden():
    assert contar_ciclo(10) == contar_recursivo(10), (
        "La solución iterativa y la recursiva no producen el mismo resultado."
    )
