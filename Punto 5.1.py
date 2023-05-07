def mcmI(n1:int, n2:int)->int: 
 nm = max(n1, n2) #escoge el número maximo entre las variables
 mcm = nm #el mnm epieza en el número maximo
 while True: #mientras sea verdadero ejecuta
    if mcm % n1 == 0 and mcm % n2 == 0: #si el cociente entre mcm y los números son 0 se rompe el ciclo
        break
    mcm += nm #se actualiza mcm
    return mcm #devuelve el mcm
if __name__ == "__main__": 
 n1 = int(input("Ingrese el primer número: ")) #pide al usuario el primer número
 n2 = int(input("Ingrese el segundo número: ")) #pide al usuario el segundo número
 mcm1 = mcmI(n1, n2) #llama la función
 print("El MCM de", n1, "y", n2, "es:", mcm1) #imprime los números y su mcm
