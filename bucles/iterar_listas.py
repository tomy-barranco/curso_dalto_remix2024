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


for num in range(len(numeros)):
  print(numeros[num])