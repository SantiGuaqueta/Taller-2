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