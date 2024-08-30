#and    las dos condiciones tienen que ser verdaderas
resultado  = 4 + 8 < 3 & 4 + 4 == 8
resultado2 = True & False
resultado3 = False & True
resultado4 = False & False

#or   si una de las condiciones se cumples

resultado5 = True or True
resultado6 = True or False
resultado7 = 4+4<4 or 5+5==10 #False or True
resultado8 = 4 + 8 <4 or 3+3 == 6 #False or False

#not   invierte el valor
resultado9 = not True
resultado10 = not False 

print(resultado7)