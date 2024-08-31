texto = input("Escribi un texto: ")

frase = texto.split()
palabras = len(frase)


pps = 2
segundos = palabras / pps

if segundos < 60:
  print(f'Dirias {palabras} palabras en {segundos} segundos.')
else:
  print("Para flaco tampoco te pedí un testamento... mamita querida... Dalto te caes a pedazos...")

pps_dalto = 2.60
segundos_dalto = round(palabras / pps_dalto, 2)
print(f'Alto lento amigo, Dalto lo diria en {segundos_dalto} segundos. KUCHAU')