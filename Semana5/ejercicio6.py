"""
Ejercicio 6:
Una tienda registra sus ventas diarias en una lista de números. Cada número representa el monto de ventas de un día.
Se solicita calcular el total de ventas acumuladas.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""
ventas = [40, 50 , 60]
def total_ventas_ciclo(ventas):
 largo = len(ventas)
 suma = 0
 while (largo > 0):
   suma = suma + ventas[largo-1]
   largo = largo -1
 return suma



def total_ventas_recursivo(ventas):
  largo = len(ventas)
  if (largo == 0):
     return 0
  else: return (ventas[-1]+ total_ventas_recursivo(ventas[:-1])) 


#print(total_ventas_recursivo(ventas))
#print(total_ventas_ciclo(ventas))

