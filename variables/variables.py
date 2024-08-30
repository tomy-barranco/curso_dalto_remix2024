
# Definiendo una variable con camelCase
nombreCompleto = "Tomas Barranco"
# Definiendo una variable con snake_case (Recomendado)
nombre_completo = "Tomas"

# Concatenar con +
bienvenida = "Hola " + nombre_completo + "¿Como estas?"

# Concatenar con f-strings
bienvenida = f"Hola {nombre_completo} ¿Como estas?"


# Operadores de pertenencia (in / not in)

print("Tomas" in bienvenida) # True
print("Tomas" not in bienvenida) # False