from Semana5.ejercicio3 import factorial_ciclo, factorial_recursivo
def test_factorial():
    assert factorial_ciclo(5) == 120, (
        "El factorial usando ciclo no es correcto."
    )

    assert factorial_recursivo(5) == 120, (
        "El factorial recursivo es incorrecto. "
        "Revise la multiplicación y el caso base."
    )
