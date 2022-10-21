# EJERCICIOS TUPLAS

# EJERCICIOS MANIPULACIÓN

# 1. Consite en la definicion de una tupla y cómo acceder a sus elementos.

print("------Ejercicio 1------")
tupla = ('Casa' , '2' , 345 , 'Perro' , 99)
print("ELEMENTOS DE LA TUPLA: " , tupla)
print("ELEMENTO DE LA POSICION 0: " , tupla[0])
print("ELEMENTO DE LA POSICION 1: " , tupla[1])
print("ELEMENTO DE LA POSICION 2: " , tupla[2])
print("ELEMENTO DE LA POSICION 3: " , tupla[3])
print("ELEMENTO DE LA POSICION 4: " , tupla[4])


# 2. Extraer posiciónes de la tupla en una tupla nueva.
print("------Ejercicio 2------")
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tupla)
tupla1 = tupla[4:9]
print(tupla1)
tupla2 = tupla[:3]
print(tupla2)
tupla3 = tupla[2:]
print(tupla3)

# 3. Consiste en el uso del operador + para realizar uniones de tuplas. Ademas, utilizar la funcion len() para conocer  el número de elementos que componen la tupla.
print("------Ejercicio 3------")
tupla1 = (29 , 'Televisión', 8763)
tupla2 = (1,2,3, 'VideoJuego')
print("NÚMERO DE ELEMENTOS DE LA TUPLA1: " ,  len(tupla1))
print("TUPLA1: " , tupla1)
print("NÚMERO DE ELEMENTOS DE LA TUPLA2: " ,  len(tupla2))  
print("TUPLA2: " , tupla2)
tupla_concatenada = tupla1 + tupla2
print("NÚMERO DE ELEMENTOS DE LA TUPLA CONCATENADA: " ,  len(tupla_concatenada))
print("TUPLA CONCATENADA: " , tupla_concatenada)


# 4. Uso del operedor * que permite concatenar una tupla con ella misma un número finito de veces.
print("------Ejercicio 4------")
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
print(tupla)
tuplaresultante = tupla * 4
print(tuplaresultante)
