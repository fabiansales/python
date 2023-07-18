year = int(input("Ingrese un año: "))

if year < 1582:
   print("Ingrese un año mayor a 1582 para que este dentro del calendario Gregoriano")
else:
    if year % 4 != 0:
      # año comun
      print("Año comun: ",)
    elif year % 100 != 0:
       # año bisiesto
       print("Año bisiesto: ",year)
    elif year % 400 != 0:
       print("Año comun: ",year)
    else:       
       print("Año bisiesto: ",year )
