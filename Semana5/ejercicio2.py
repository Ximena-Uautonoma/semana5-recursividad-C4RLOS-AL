"""
Ejercicio 2:
Dado un número entero positivo N, retornar la suma de los primeros N números.

Debe implementar:
- suma_ciclo(n)
- suma_recursiva(n)
"""

#    Retorna la suma de los primeros n números usando un ciclo.
def suma_ciclo(n):
    numero = 0
    while (n > 0):
        numero = numero + n
        n = n-1
    return numero

#print(suma_ciclo(2))








 # Retorna la suma de los primeros n números usando recursividad.

def suma_recursiva(n):
    if (n == 1 or n == 0):
        return n
    else:
        return (n + suma_recursiva(n-1))


#print(suma_recursiva(2))