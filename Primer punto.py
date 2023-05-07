# 1)  Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número.

def num(a): # definimos la función 'num' con parámetro 'a'
     entero = [int(i) for i in a] # definimos entero para que tome cada digito 'i' de 'a'
     print(entero) # imprimimos los números

n = input("Ingrese un número: ") # pedimos al usuario que ingrese un número
num(n) # ejecutamos la función 'num' para el número 'n' dado

