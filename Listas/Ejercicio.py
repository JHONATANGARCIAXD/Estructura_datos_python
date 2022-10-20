# EJERCICIOS LISTAS

# EJERCICIOS MANIPULACIÓN

# 1. Consiste en la dificion de una lista con elementos de diferentes tipos y en mostrarla en pantalla, tanto entera como por elementos accediendo a la posicion que ocupa dentro de la lista.

lista = ["python" , " Guanentá" , "2022","libro" , 3 ]
print (lista)
print(lista[0])
print(lista[2])

# 2. Consiste en el uso del operador + para realizar uniones de listas. Ademas, utilizar la funcion len() para conocer  el número de elementos que componen la lista.
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

lista1 = ["Camiseta", "Pantalón", "Zapatos"]
print(lista)
lista = lista+["Abrigo"]
print(lista)
lista = lista + ["Jersey", "Sudadera"]
print(lista)
lista = lista + ["Calcetines"] + ["Bufanda"]
print(lista)


# 4. Modicar elementos de una lista y borrar elementos de la misma.

lista = ["Camiseta", "Pantalón", "Zapatos"]
print(lista)

lista[1] = "Cazadora"
print(lista)
del lista[0]
print(lista)
