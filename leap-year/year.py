year = int(input("Ingrese un año: "))

if year < 1582:
   print("\nIngrese un año mayor a 1582 para que este dentro del calendario Gregoriano\nEnter a year greater than 1582 to be within the Gregorian Calendar\n")
else:
    if year % 4 != 0:
      print("Año Común: ",year)
    elif year % 100 != 0:
       print("Año Bisiesto: ",year)
    elif year % 400 != 0:
       print("Año Común: ",year)
    else:       
       print("Año Bisiesto: ",year )
