def mcmR(n1:int, n2:int)->int:
 nm = max(n1, n2) #escoge el número mayor entre las variables
 def mcmR2(a, b, mcm): 
   if mcm % a == 0 and mcm % b == 0: #si el cociente es igual a 0 entre el mcm y los números devuelve el mcm, si no aplica la función recursiva sobre él mismo
        return mcm #devuelve el mcm
   return mcmR2(a, b, mcm + nm) #vuelve a utilizar su función sobre él mismo 
 return mcmR2(n1, n2, nm) #devuelve el mcm
if __name__ == "__main__":
 n1 = int(input("Ingrese el primer número: ")) #pide al usuario ingresar el primer número
 n2 = int(input("Ingrese el segundo número: ")) #pide al usuario ingresar el segundo número	
 mcmF = mcmR(n1, n2) #llama la función principal
 print("El MCM de"+str(n1)+ "y" +str(n2)+ "es:"+str(mcmF) ) #imprime los números y su mcm
