import tkinter as tk

def check_leap_year():
    year = int(entry.get())

    if year < 1582:
        result_label.config(text="Ingrese un año mayor a 1582 para que esté dentro del calendario Gregoriano")
    else:
        if year % 4 != 0:
            result_label.config(text="Año Común: " + str(year))
        elif year % 100 != 0:
            result_label.config(text="Año Bisiesto: " + str(year))
        elif year % 400 != 0:
            result_label.config(text="Año Común: " + str(year))
        else:
            result_label.config(text="Año Bisiesto: " + str(year))

# Crear la ventana principal
window = tk.Tk() 
window.title("Verificar Año Bisiesto")
window.geometry("600x150")
window.config(background="Black")


# Etiqueta y campo de entrada para ingresar el año
entry_label = tk.Label(window, text="Ingrese un año:", background="pink")
entry_label.pack()

entry = tk.Entry(window)
entry.configure(background="green")
entry.pack()

# Botón para verificar el año
check_button = tk.Button(window, text="Verificar", command=check_leap_year,background="pink")
check_button.pack()

# Etiqueta para mostrar el resultado
result_label = tk.Label(window, text="",background="black",fg="yellow")
result_label.pack()

# Iniciar el bucle principal de la ventana
window.mainloop()
