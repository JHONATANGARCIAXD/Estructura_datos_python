# EJERCICIOS LISTAS

# EJERCICIOS MANIPULACIÓN

# 1. Consiste en la dificion de una lista con elementos de diferentes tipos y en mostrarla en pantalla, tanto entera como por elementos accediendo a la posicion que ocupa dentro de la lista.
print("------Ejercicio 1------")
lista = ["python" , " Guanentá" , "2022","libro" , 3 ]
print (lista)
print(lista[0])
print(lista[2])

# 2. Consiste en el uso del operador + para realizar uniones de tuplas. Ademas, utilizar la funcion len() para conocer  el número de elementos que componen la lista.
print("------Ejercicio 2------")
lista1 = ["Camiseta", "Pantalón", "Zapatos"]
lista2 = ["Abrigo", "Jersey", "Sudadera", "Calcetines"]
print("Número de elementos de la lista1: " ,  len(lista1))  
print("Lista1: " , lista1)  
print("Número de elementos de la lista2: " ,  len(lista2))
print("Lista2: " , lista2)
lista_concatenada = lista1 + lista2
print("Lista concatenada: " , len(lista_concatenada))
print(lista_concatenada)

# 3. Añadir elmentos para lista de diferentes formas.
print("------Ejercicio 3------")
lista1 = ["Camiseta", "Pantalón", "Zapatos"]
print(lista)
lista = lista+["Abrigo"]
print(lista)
lista = lista + ["Jersey", "Sudadera"]
print(lista)
lista = lista + ["Calcetines"] + ["Bufanda"]
print(lista)


# 4. Modicar elementos de una lista y borrar elementos de la misma.
print("------Ejercicio 4------")
lista = ["Camiseta", "Pantalón", "Zapatos"]
print(lista)

lista[1] = "Cazadora"
print(lista)
del lista[0]
print(lista)


# 5. Uso del operador * que permite concatenar una lista con ella misma un número finito de veces.
print("------Ejercicio 5------")
lista = ["Camiseta", "Pantalón", "Zapatos"]
print(lista)
lista_resultante = lista * 3
print(lista_resultante)


# 6. Cracion de listas como elementos como elementos de listas y acceso a dichos elementos. 
print("------Ejercicio 6------")
lista1 = ["Camiseta", ['calcetines', 'Cazadora'], 'Zapatos']
print(lista1)
print(lista1[0])
print(lista1[1])
print(lista1[2])
print(lista1[1][0])
print(lista1[1][1])


# 7. Extraer una porcion de la lista en una lista nueva.   
print("------Ejercicio 7------")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)
lista1 = lista[3:7]
print(lista1)
lista2 = lista[:5]
print(lista2)
lista3 = lista[6:]
print(lista3)
