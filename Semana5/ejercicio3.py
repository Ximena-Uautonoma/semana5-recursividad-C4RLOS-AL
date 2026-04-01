"""
Ejercicio 3:
Dado un número entero positivo N, calcular su factorial.

Debe implementar una versión iterativa y una recursiva.
"""

def factorial_ciclo(n):
    facto = n
    while(n > 1):
        facto = (facto * (n-1))
        n = n -1
    return facto

#print(factorial_ciclo(10))


def factorial_recursivo(n):
    if (n == 1):
        return 1
    else: return (n *factorial_recursivo(n-1)) 

#print(factorial_recursivo(10))