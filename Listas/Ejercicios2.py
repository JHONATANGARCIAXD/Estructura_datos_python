# EJERCICIOS LISTAS

# METODOS PROPIOS

lista = [45, 32, 3, 78]
print("LISTA ORIGINAL: " , lista)

# Función Append: Añade un elemento a la lista. 
lista.append(995)
lista.append(7)
print("LISTA CON APPEND: " , lista)

# Función Sort: Ordena los elementos de la lista.
lista.sort()
print("LISTA ORDENADA: " , lista)

# Función Reverse: Invierte el orden de los elementos de la lista.
lista.reverse()
print("LISTA INVERTIDA: " , lista)

# Función Extend: Añade una lista a otra lista.
lista_extend=[1, 5, 87, 45]
lista.extend(lista_extend)
print("LISTA DESPUES DE EXTEND: " , lista)

# Función Count: Cuenta el número de veces que aparece el elemento indicado como parámetro dentro de la lista.
print("NÚMERO DE ELEMENTOS 45: " , lista.count(45))

# Función Insert: Añade el elemento pasado como parámetro a la lista en la posicion indicada tambien por parámetro.
lista.insert(4,111)
print("LISTA DESPUES DE INSERT: " , lista)

# Finción Remove: Elimina la primera ocurrencia empezando por la izquierda de la lista del elemento pasado como parámetro.
lista.remove(45)
print("LISTA DESPUES DE REMOVE: " , lista)

# Función Index: Devuelve la posicion de la primera ocurrencia de izquierda a derecha en la lista, del elemento pasado como parámetro.
print("POSICIÓN DEL ELEMENTO 111: " , lista.index(111))

# Función Pop: Elimina el elemento de la lista y lo devuelve como resultado de la operación. 
lista.pop()
print("LISTA DESPUES DE POP: " , lista)

# Función Clear: Elimina todos los elementos de la lista.
lista.clear()
print("LISTA DESPUES DE CLEAR: " , lista)