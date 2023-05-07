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
