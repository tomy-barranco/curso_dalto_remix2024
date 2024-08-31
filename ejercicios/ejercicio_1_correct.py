# EJERCICIO A
print("EJERCICIO A")

minimo = 2.5
promedio = 4
maximo = 7
este_curso = 1.5

# La funicon round() sirve para reducir la cantidad de decimales al numero dado

porcentaje_rapido = round(100 - (este_curso / minimo)*100, 2)
print(f'El porcentaje con el mas rapido es {porcentaje_rapido}%')

porcentaje_lento = round(100 - (este_curso / maximo)*100, 2)
print(f'El porcentaje con el mas lento es {porcentaje_lento}%')

porcentaje_promedio = round(100 - (este_curso / promedio)*100, 2)
print(f'El porcentaje con el promedio es {porcentaje_promedio}%')

#EJERCICIO B
print("EJERCICIO B")

crudo_promedio = 5
crudo_dalto = 3.5

inservible_promedio = crudo_promedio - promedio
inservible_dalto = crudo_dalto - este_curso

porcentaje_promedio = round((inservible_promedio / crudo_promedio)* 100, 2)
print(f'El porcentaje de material que se reduce en promedio es de: {porcentaje_promedio}%')

porcentaje_dalto = round((inservible_dalto / crudo_dalto)* 100, 2)
print(f'El porcentaje de material que Dalto reduce es de: {porcentaje_dalto}%')

# EJERCICIO C
print("EJERCICIO C")

veces_vistas = 10 / este_curso

equivalencia_minimo = round(veces_vistas * minimo, 2)
print(f'Ver 10hs de Dalto equivale a {equivalencia_minimo}hs del mas rapido')

equivalencia_maximo = round(veces_vistas * maximo, 2)
print(f'Ver 10hs de Dalto equivale a {equivalencia_maximo}hs del mas lento')

equivalencia_promedio = round(veces_vistas * promedio, 2)
print(f'Ver 10hs de Dalto equivale a {equivalencia_promedio}hs del promedio')