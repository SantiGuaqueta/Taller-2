# Ejercicio 3
def numeroEspejo(n1:int, n2:int)->int: 
 d1 = str(n1) #se lee los número como cadena de caracteres con str
 d2 = str(n2) #se lee los número como cadena de caracteres con str
 if len(d1) != len(d2): #verifica si el número de caracteres son diferentes para parar el proceso
    return False 
 for i in range(len(d1)): #recorrepor lo números de la cadenade caracteres
    if d1[i] != d2[len(d2) - 1 - i]:#si no son iguales los caracteres al voltearse devuelve que es falso el número espejo 
     return False
 return True #si llega a este punto son números espejos
if __name__ == "__main__":
 n1 = int(input("Ingrese el primer número: ")) #pide al usuario el primer número
 n2 = int(input("Ingrese el segundo número: ")) #pide al usuario el segundo número
 if numeroEspejo(n1, n2): #llama la función y si se completa al evaluar los números imprimeque son espejos
    print("Los números son espejos")
 else: #si no lo hace imprime que no son espejos
    print("Los números no son espejos")
