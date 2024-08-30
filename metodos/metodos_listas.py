lista = list([316, 34, 8.4])

#cantidad de elementos de la lista
cantidad = len(lista)

#agregar un elemento a la lista
lista.append(76)

#agregar un elemento a la lista en un limite especifico
lista.insert(2, 74)

#agregar varios elementos a la lista
lista.extend([23, False, True, False,2, 2024])

#eliminar un elemento de la lista por su indice
lista.pop(3)
#lista.pop(-1), el ultimo, es decir contando de atras para adelante

#remover un elemento de la lista por su valor
lista.remove(2)

#eliminar todos los elementos de la lista
#lista.clear()

#ordena los elementos de forma ascendente.  funciona solo sin cadenas de texto
lista.sort()
#lista.sort(reverse=True) invierte los elementos

#invierte los elementos
lista.reverse()

#busca elementos
elemento_encontrado = lista.index(76)

print(lista)