animales = ['gato', 'perro', 'loro', 'cocodrilo']
numeros = [52, 16, 14, 72]

# Recorriendo la lista animales
for animal in animales:
  print(f'Ahora la variable animal es igual a: {animal}')

# Recorriendo la lista numeros y multiplicando cada valor por 10
for numero in numeros:
  resultado = numero * 10
  print(resultado)


# Iterando dos listas del mismo tamaño al mismo tiempo
for numero,animal in zip(animales,numeros):
  print(f'Recorriendo la lista 1: {numero}')
  print(f'Recorriendo la lista 2: {animal}')


# Forma no optima de recorrer una lista - no funciona en conjuntos
for num in range(len(numeros)):
  print(numeros[num])

# Forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
  indice = num[0]
  valor = num[1]
  print(f'El indice es: {indice} y el valor es: {valor}')

# Forma practica y elegante: for num, i in enumerate(numeros)
for num, i in enumerate(numeros):
  print(numeros)

# Usando el for/else
for numero in numeros:
  print(f"Ejecutando el ultimo bucle, valor actual: {numero}")
else:
  print('El bucle termino')

# Todo lo anterior funciona exactamente igual para tuplas y conjuntos