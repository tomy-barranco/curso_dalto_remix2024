#todos los metodos son funciones pero no todas las funciones son metodos
cadena1 = "LUCA es el rey del mundo es la maquina"
cadena2 = "salomon"

dir(cadena1) #muestra todo lo que se puede hacer con determinado dato 
# print(dir(cadena1))

cadena1.upper() #convierte todo a mayuscula
cadena1.lower() #convierte todo a minuscula
cadena1.capitalize()#primer letra a mayuscula

busqueda_find = cadena2.find("a")#busca un valor que le pidamos
busqueda_index = cadena1.index("A") #si no encuentra nada tira un error
print(busqueda_find)

#si es numerico devuelve true, sino devuelve false
es_numerico = cadena1.isnumeric()

#si es alfanumerico devuelve true, sino devuelve false
es_alfanumerico = cadena1.isalpha()

#nos dice cuantas veces hay una cadena
busqueda_find = cadena2.find("a")

#cantidad de caracteres que tiene una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con una cadena dada
empieza_con = cadena1.startswith("LU")

#verificamos si una cadena empieza con una cadena dada
termina_con = cadena1.endswith("CA")

#remplaza un pedazo de la cadena dad por otra dada
cadena_nueva = cadena1.replace("CA", "CASSS")

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split("es")