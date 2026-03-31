"""
Ejercicio 1: Dado un número entero positivo N, retornar una lista con los números desde 1 hasta N.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""
#  Retorna una lista con los números desde 1 hasta n usando iteración.
def contar_ciclo(n):
   numeros = []
   contador = 1
   while (contador <= n):
       numeros.append(contador)
       contador += 1
   print (numeros) 


# Retorna una lista con los números desde 1 hasta n usando recursividad.
def contar_recursivo(n):
   # if n <= 0:
    #  return []
    #else: return [n] + contar_recursivo(n-1)
 pass



#print(contar_recursivo(10))