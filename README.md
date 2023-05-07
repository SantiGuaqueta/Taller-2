# Taller-2 🦖
Porque lo decepcionamos la ultima vez con el logo esta vez nos inspiramos e hicimos nosotros nuestro propio logo, fue realizado con mucho esfuerzo y trabajo duro aunque no lo parezca.

A continuacon el mejor logo que vera ( o eso esperamos ).....

[![image-2.png](https://i.postimg.cc/KYT0QBLw/image-2.png)](https://postimg.cc/Z9TP59wx)

Ahora si, que hay de nuevo prograsaurio, ya sabes que quedamos pocos de nosotros pero mientras existamos realizaremos repos a la vieja escuela prehistorica asi que empecemos.
Como todo programador prehistorico empecemos con un chiste:


[![no-se-dejaba.jpg](https://i.postimg.cc/sXw7Jgnb/no-se-dejaba.jpg)](https://postimg.cc/R6JWS4xT)


1. Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número.

##### Solucion

``` python
# 1)  Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número.

def num(a): # definimos la función 'num' con parámetro 'a'
     entero = [int(i) for i in a] # definimos entero para que tome cada digito 'i' de 'a'
     print(entero) # imprimimos los números

n = input("Ingrese un número: ") # pedimos al usuario que ingrese un número
num(n) # ejecutamos la función 'num' para el número 'n' dado

``` 

2. Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entrege los digitos tanto de la parte entera como de la decimal.

##### Solucion

``` python
# Ejercicio 2
def numero_real(n:float)->int: # Declaramos la funcion en la cual va a dar un entero
    m=int(n) # Declaramos a m como el entero de n  
    return(m) # Returnoamos m

if __name__ == "__main__":
    n=float(input("Escriba un numero real: ")) # Le pedimos n que es e numero que separaremos en parte entera y decimal
    parte_entera = numero_real(n) # Llamamos a la funcion 
    z=float(n - parte_entera) # Aqui declaramos z como un flotante porque sera la parte decimal de el numero n para esto ponemos que a n le reste la funcion anterior que retorna solo la parte entera
    print ( "La parte entera del numero ingresado es "+str(parte_entera)) # Imprimimos la parte entera
    print( " y la parte decimal es" +str(z)) # Imprimimos la parte decimal

``` 
3. Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos.

##### Solucion

``` python
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

``` 
4. Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Con cuántos valores de la serie, se tienen errores del 10%, 1%, 0.1% y 0.001%.
$$cos(x) \approx cos(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i}}{(2i)!}$$

##### Solucion

``` python
# Ejercicio 4 taller 2
import math

def aprox_cos(x, n): # Define la función
    z = 0
    for i in range(0,n): # Recorre todos los números hasta n-1 
        a = (-1) ** i # Cambia signo y eleva por los numeros del for
        b = (x ** (2 * i)) / math.factorial(2 * i ) # Calcula una aproximación de la función seno para x utilizando los primeros n términos de la serie de Maclaurin
        z += a * b # Calcula todos los datos para dar la aproximación guardada en a
    return z

if __name__ == "__main__":
    x = float(input("Ingrese el numero para calcular el Coseno = ")) # Pide al usuario el número
    n = int(input("Ingrese un número de series de MacLaurin = ")) # Pide al usuario las series
    z = aprox_cos(x, n) # Llama la función
    coseno = math.cos(x) # Resultado real
    print("Resultado Serie MacLaurin: "+str (z)) # Imprime la aproxcimación
    print("Resultado Funcion Math: "+str(coseno)) # Imprime la el valor real
    print("Diferencia = "+str(coseno - z)) # Imprimir la diferencia entre los dos valores

``` 

5. Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde la perpectiva iterativa como recursiva.

##### Solucion 5.1

``` python
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

```

##### Solucion 5.2

``` python
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

```
6. Desarrollar un programa que determine si en una lista no existen elementos repetidos.

##### Solucion

``` python
# Ejercicio 6
def lista_repetida(n):
    for x in range(0,n): 
        num=float(input("Escriba el numero: "))# Le pido un numero
        lista.append(num) # El numero que pedimos anterior se agregara a la lista 
    duplicados = [x for i, x in enumerate(lista) if i != lista.index(x)] # Usamos List comprenhension con index para saber los repetidos de la lista 
    print( "Los elementos repetidos son:"+str(duplicados)) # Imprime los duplicados que existen y si no lo hay imprime una lista vacia

if __name__ == "__main__":
    n=int(input("Cantidad de datos en la lista: ")) #Pido cantidad de numeros que va a tener la lista
    lista=[] # declaro una lista vacia que se utilizara mas adelante
    lista_repetida(n) # Llamamos a la funcion para que imprima 

```
7. Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. 
Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.
##### Solucion

``` python
# Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales.
# Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.
list1 = [] #creamos una lista vacía
list2 = ['a','e','i','o','u'] #creamos la lista de las vocales
n = (input("ingrese un elemento de texto para la lista : "))  #preguntamos al usuario que elemento desea añadir
cont = 0 #iniciamos nuestro contador en 0
while (n != 'stop'): #ejecutamos siempre que los elementos ingresados sean distintos a la palabra 'stop'
    el = list(n) #creamos la lista 'el' que nos separará las letras del elemento ingresado
    print(el) #imprimimos la lista 'el'
    len1 = len(el)-1 #creamos 'len1' para saber cuantos elementos tenemos en la lista
    i = 0 #asignamos a 'i' un valor inicial de 0
    while (i <= len1): #iniciamos un ciclo siempre que 'i' sea mejor o igual a 'len1'
        if el[i] in list2: #si el elemento 'i' de la lista 'el' está en la lista 2
            i = i + 1 #sumamos 1 a 'i'
            cont = cont + 1 #sumamos 1 al contador
        else:
            i = i + 1 #sumamos 1 a 'i'
    if cont >= 2: #si al final, el contador es mayor o igual a 2, imprimimos la cadena
        print('el elemento ',n,' tiene ',cont,' vocales o más') #imprimimos el enunciado
    else:
        print('No existe') #si el contador es menor a 2, imprime 'no existe'
    cont = cont-cont #volvemos a poner el contador en 0
    list1.append(n)  #añadimos el elemento a la lista 
    n = (input("ingrese un elemento de texto para la lista (si no deseas añadir mas, escribe 'stop'): "))  #incluimos la pregunta en el ciclo para que se repita hasta terminar el ciclo
print(list1)  #imprimimos la lista 
```

8. Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista. **Ejemplo:**
<center>
<table border="1">
<tr>
<td>
lista1: [1, 'Hola', -12.3 ,True]<br>
lista2: [11, -12.3, 'Hola', False]
</td>
</tr>
<tr>
<td>
salida: [1, True]
</td>
</tr>
</table>
</center>

##### Solucion

``` python
# Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista

list1 = [] #creamos una lista 1 vacía
n = (input("ingrese un elemento para la lista 1 : "))  #preguntamos al usuario que elemento desea añadir
while (n != 'stop'): #ejecutamos siempre que los elementos ingresados sean distintos a la palabra 'stop'
    list1.append(n)  #añadimos el elemento a la lista 1
    n = (input("ingrese un elemento para la lista 1 (si no deseas añadir mas, escribe 'stop'): "))  #incluimos la pregunta en el ciclo para que se repita hasta terminar el ciclo
print(list1)  #imprimimos la lista 1
list2 = [] #creamos una lista 2 vacía
m = (input("ingrese un elemento para la lista 2 : "))  #preguntamos al usuario que elemento desea añadir
while (m != 'stop'):  #ejecutamos siempre que los elementos ingresados sean distintos a la palabra 'stop'
    list2.append(m)  #añadimos el elemento a la lista 2
    m = (input("ingrese un elemento para la lista 2 (si no deseas añadir mas, escribe 'stop'): "))  #incluimos la pregunta en el ciclo para que se repita hasta terminar el ciclo
print(list2)  #imprimimos la lista 2

len1 = len(list1)-1 #creamos 'len1' para saber cuantos elementos tenemos en la lista
i = 0 #asignamos a 'i' un valor inicial de 0

while (i <= len1): #iniciamos un ciclo siempre que 'i' sea mejor o igual a 'len1'
    if list1[i] in list2: #si el elemento 'i' de la lista 1 está en la lista 2, no lo imprimimos
            i = i + 1 #sumamos 1 a 'i'
    else:
        print('elsiguiente elemento de la lista 1 no está en la lista 2 : ',list1[i]) #si el elemento 'i' de la lista 1 no está en la lista 2 lo imprimimos
        i = i + 1 #sumamos 1 a 'i'
```

9. Resolver el punto 7 del [taller 1](https://github.com/fegonzalez7/pdc_unal_clase8) usando operaciones con vectores.

##### Solucion

``` python
# Ejercicio 9
Lista = [] #crea una lita vacia
for i in range(5): #recorre 5 veces para generar 5 entradas para los números
    n= float(input("Ingrese el número:")) #pide al usuario los números
    Lista.append(n) #agrega los números ingresados a la lista
promedio = sum(Lista) / len(Lista) #calcula el promedio sumando los valores de la lista y dividiendo por el número de valores
numerosOrdenado = sorted(Lista) #organiza los números en orden ascendente
mediana = numerosOrdenado[len(numerosOrdenado) // 2] #saca la mediana a través de los números ordenados encontrando el de la mitad 
producto = 1 #empizala variable en 1
for n in Lista: #recorre segun lo números que existan en la lista
    producto *= n #multiplica los númerosy se guarda el resultado en la variable producto
promedioMultiplicativo = producto ** (1 / len(Lista)) #aplica la formúla de promedio multiplicativo a traves de la variable del producto
numerosAscendente = sorted(Lista) #ordena los números de forma ascendente
numerosDescendente = sorted(Lista, reverse=True) #ordena los números de forma descendente
mayor = max(Lista) #tomael mayor número de la lista
menor = min(Lista) # toma el menor número de la lista
potencia = mayor ** menor #calcula la potencia del mayor elevado al menor número
raizCubica = menor ** (1 / 3) #calcula la raiz cubica del menor número
print("Promedio:"+str( promedio))  #imprime el promedio
print("Mediana:"+str( mediana)) #imprime la mediana
print("Promedio multiplicativo:"+str( promedioMultiplicativo)) #imprime la promedio multiplicativo
print("Números ordenados de forma ascendente:"+str( numerosAscendente)) #imprime la lista en orden ascendente
print("Números ordenados de forma descendente:"+str( numerosDescendente)) #imprime la lista de orden descendente
print("Potencia del mayor número elevado al menor número:"+str( potencia)) #imprime la potencia
print("Raíz cúbica del menor número:" +str(raizCubica)) #imprime la raiz

```

10. Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.

##### Solucion

``` python
# Ejercicio 10
# Desarrollar un algoritmo que determine si una matriz es mágica.
# Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas,
# de cada una de sus columnas y de cada diagonal es igual.


list1 = [] #creamos una lista vacia
B = [] #creamos una lista vacia

for i in range(3): #limitamos las filas a 3
    for j in range(3): #limitamos las columnas a 3
        num = float(input("ingrese los valores de los elementos de su matriz: ")) #pedimos los elementos de la matriz
        list1.append(num) #añadimos los elementos a la lista 1
    B.append(list1) #añadimos los elementos a la lista B
    list1 = []
print(B) #imprimimos B

def magic(B:float):#definimos la suma rotativa
    a = B[0][0] #escribimos las posiciones de los elementos que deseamos sumar
    b = B[1][0]
    c = B[2][0]

    d = B[0][1]
    e = B[1][1]
    f = B[2][1]

    g = B[0][2]
    h = B[1][2]
    i = B[2][2]

    a1 = B[0][0] #escribimos las posiciones de los elementos que deseamos sumar
    b1 = B[0][1]
    c1 = B[0][2]

    d1 = B[1][0]
    e1 = B[1][1]
    f1 = B[1][2]

    g1 = B[2][0]
    h1 = B[2][1]
    i1 = B[2][2]
    
    a2 = B[0][0] #escribimos las posiciones de los elementos que deseamos sumar
    b2 = B[1][1]
    c2 = B[2][2]    
    
    d2 = B[0][2]
    e2 = B[1][1]
    f2 = B[2][0]

    suma1 = a + b + c#realizamos las sumas de las columnas
    suma2 = d + e + f
    suma3 = g + h + i
    suma4 = a1 + b1 + c1 #realizamos las sumas de las columnas
    suma5 = d1 + e1 + f1
    suma6 = g1 + h1 + i1
    suma7 = a2 + b2 + c2 #realizamos las sumas de las columnas
    suma8 = d2 + e2 + f2

    if suma1 == suma2 == suma3 == suma4 == suma5 == suma6 == suma7 == suma8:
        print("su matriz es magica: ")
    else:
        print("tu matriz no es magica")

magic(B)
``` 
