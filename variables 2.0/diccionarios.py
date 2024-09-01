# Creando diccionarios con dict()
diccionario = dict(nombre='lucas',apellido='dalto')

# Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(['dalto', 'rancio']):"jajas"}

# Creando diccionaros con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre", "apellido"])

# Creando diccionaros con fromkeys() valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre", "apellido"], "No se")

print(diccionario["nombre"])