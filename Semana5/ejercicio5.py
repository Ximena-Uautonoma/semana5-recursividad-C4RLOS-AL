"""
Ejercicio 5:
Calcular la potencia de una base elevada a un exponente entero positivo.
"""

def potencia_ciclo(base, exponente):
    resultado = base
    while (exponente != 1):
        resultado = resultado * base
        exponente = exponente -1
    return resultado
#print(potencia_ciclo(5,3))


def potencia_recursiva(base, exponente):
    if (exponente == 1):
        return base
    elif (exponente == 0):
        return 1
    else: 
        return base * (potencia_recursiva(base, exponente - 1)) 

#print(potencia_recursiva(5,3))