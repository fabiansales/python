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
'''
x = 10
 
if x == 10: # True
    print("x == 10")
 
if x > 15: # False
    print("x > 15")
 
elif x > 10: # False
    print("x > 10")
 
elif x > 5: # True
    print("x > 5")
 
else:
    print("else no será ejecutado")

Si la condición para if es False, el programa verifica las condiciones de los bloques elif posteriores: 
el primer elif que sea True es el que se ejecuta. Si todas las condiciones son False, se ejecutará el bloque else.    

'''