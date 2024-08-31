texto = input("Escribi un texto: ")

palabras = texto.find(" ") - 1
pps = palabras * 2
segundos = palabras / 2

print(f'Dirias {palabras} palabras en {pps} segundos.')