"""
Ejercicio 4:
Dado un número entero positivo N, contar cuántos números pares existen entre 1 y N.
"""

def contar_pares_ciclo(n):
    pares = 0
    while (n > 0):
        if (n%2 == 0):
            pares = pares +1
        n = n-1
    return pares

#print(contar_pares_ciclo(100))


def contar_pares_recursivo(n):
    if (n == 0):
        return 0
    if (n%2 ==0):
        return 1 + contar_pares_recursivo(n-1)
    else: return 0 + contar_pares_recursivo(n-1) 
    
print(contar_pares_recursivo(100))
    
