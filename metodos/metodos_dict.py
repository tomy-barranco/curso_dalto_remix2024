diccionario = {
    "nombre" : "luca",
    "apellido" : "salomon",
    "campeon" : "del mundo"
}

#devuelve las claves
claves = diccionario.keys()
print(claves)

#si pongo la clave nos da el elemento
valor_de_elemento = diccionario.get("apellido")

#elimina un elemento del diccionario
diccionario.pop("nombre")

#obtener un elemento dict_iter iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)
#elimina todo el diccionario
diccionario.clear()