"""
Ejercicio 7:
Una persona registra cuánto dinero ahorra cada mes en una lista.
Cada valor representa el ahorro mensual.

Se requiere calcular el ahorro total acumulado.

Debe implementar:
1. Una solución con iteración
2. Una solución con recursividad
"""
#ahorros = [100000, 200000, 37000, 30000]

def ahorro_total_ciclo(ahorros):
 largo = len(ahorros)
 suma = 0
 while (largo > 0):
   suma = suma + ahorros[largo-1]
   largo = largo -1
 return suma

#print(ahorro_total_ciclo(ahorros))  
   




def ahorro_total_recursivo(ahorros):
  largo = len(ahorros)
  if (largo == 0):
     return 0
  else: return (ahorros[-1]+ ahorro_total_recursivo(ahorros[:-1])) 

#print(ahorro_total_recursivo(ahorros))