
# Creando una lista (Se pueden modificar)
lista = ["Tomas Barranco","Soy Dalto",True,1.76]

# Creando una tupla (No se pueden modificar)
tupla = ("Tomas Barranco","Soy Dalto",True,1.76)

# Esto es válido
lista[3] = "Maquinola"

# Esto no
# tupla[3] = "Maquinola"

# Esto es válido
#print(tupla[3])

# Esto no
#print(tupla(3))

# Creando un conjunto (set) (No se accede a los elementos por su indice, no almacena datos duplicados)

conjunto = {"Tomas Barranco","Soy Dalto",True,1.76}

# Esto es válido
#conjunto = {"Jajaja maquina te jodi"}
#tupla = {"Jajaja maquina te jodi"}

# Esto no
#conjunto[1] = "Pedrin" -> no se puede cambiar un dato

# Esto es válido
print(conjunto)

# Esto no
#print(conjunto[1]) -> no se puede acceder

# No se pueden repetir valores
#conjunto = {"Tomas Barranco","Soy Dalto",True,1.76, "SoyDalto"}

# Creando un diccionario (dict) (La estructura es key : value y separamos con comas)
diccionario = {
  "nombre": "Tomas Barranco",
  "usuario": "Tomy-dev",
  "esta_emocionado": True,
  "altura": 1.76,
  "dato_duplicado": "Tomy-dev"
}

print(diccionario["nombre"])
print(lista[0]) # Es lo mismo
