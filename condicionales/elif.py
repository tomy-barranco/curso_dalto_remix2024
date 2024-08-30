ingreso_mensual = 70000
gasto_mensual = 59000

#if anidados y elif

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 100:
        print('estas en deficit')
    elif ingreso_mensual - gasto_mensual > 10000:
        print("sos rico")
    else:
        print("estas gastando mucho")

elif ingreso_mensual > 5000:
    print("estas bien")

elif ingreso_mensual > 1000:
    print("estas bien en argentina")

elif ingreso_mensual > 500:
    print("estas bien en venezuela")

else:
    print("sos pobre")