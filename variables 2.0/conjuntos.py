# Creando un conjunto set ()
conjunto = set(['Dato 1'])

# Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(['dato 1', 'dato2'])
conjunto2 = {conjunto1, 'dato3'}
print(conjunto)

# Teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {2,4,6,8}

# Verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

# Verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

# Verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)