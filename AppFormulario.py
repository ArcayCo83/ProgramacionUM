
import tkinter as tk
import pandas as pd
from datetime import date
from tkinter import ttk, messagebox
import os
import sys

## Añadir ruta del ejecutable
ruta_app = os.path.dirname(os.path.abspath(__file__))

# Crear un DataFrame vacío para almacenar la información
columns = ['Nombre', 'Apellido', 'Fecha de Nacimiento', 'Género', 'Edad']
df = pd.DataFrame(columns=columns)

# Función para guardar el DataFrame en un archivo CSV
def save_to_csv():
    path = os.path.join(ruta_app, 'informacion.csv')
    df.to_csv(path, index=False)

# Función para calcular la edad
def calcular_edad(fecha_nac):
    delta = date.today() - fecha_nac
    edad = delta.days // 365
    return edad

# Función cuando se presiona el botón "Enviar"
def on_button_click():
    global df
    
    try:
        fecha_nac = date(int(fecha_nacimiento_year.get()), int(fecha_nacimiento_month.get()), int(fecha_nacimiento_day.get()))
        edad = calcular_edad(fecha_nac)
        
        # Crear un DataFrame temporal con la nueva fila
        new_data = {
            'Nombre': [nombre.get()],
            'Apellido': [apellido.get()],
            'Fecha de Nacimiento': [fecha_nac],
            'Género': [genero_var.get()],
            'Edad': [edad]
        }
        df_temp = pd.DataFrame(new_data)
        
        # Usar concat para añadir la nueva fila al DataFrame principal
        df = pd.concat([df, df_temp], ignore_index=True)
        
        # Guardar la información en el archivo CSV
        save_to_csv()
        
        messagebox.showinfo("Información", f"Información agregada con éxito!\n\nNombre: {nombre.get()}\nApellido: {apellido.get()}\nFecha de Nacimiento: {fecha_nac}\nGénero: {genero_var.get()}\nEdad: {edad} años")
        
        # Limpiar los campos
        nombre.delete(0, tk.END)
        apellido.delete(0, tk.END)
        fecha_nacimiento_day.set(1)
        fecha_nacimiento_month.set(1)
        fecha_nacimiento_year.set(2000)
        genero_var.set("Masculino")
    except Exception as e:
        messagebox.showerror("Error", f"Error al agregar la información: {e}")


# Crear una ventana principal
window = tk.Tk()
window.title("Formulario de Información")

# Variables para guardar la información del formulario
nombre = ttk.Entry(window, width=30)
apellido = ttk.Entry(window, width=30)
fecha_nacimiento_day = tk.IntVar(value=1)
fecha_nacimiento_month = tk.IntVar(value=1)
fecha_nacimiento_year = tk.IntVar(value=2000)
genero_var = tk.StringVar(value="Masculino")

# Elementos de la interfaz
ttk.Label(window, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
nombre.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(window, text="Apellido:").grid(row=1, column=0, padx=10, pady=5)
apellido.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(window, text="Fecha de Nacimiento:").grid(row=2, column=0, padx=10, pady=5)
ttk.Spinbox(window, from_=1, to=31, textvariable=fecha_nacimiento_day, width=5).grid(row=2, column=1, padx=(10, 0), pady=5, sticky='w')
ttk.Spinbox(window, from_=1, to=12, textvariable=fecha_nacimiento_month, width=5).grid(row=2, column=1, padx=(70, 0), pady=5, sticky='w')
ttk.Spinbox(window, from_=1900, to=2100, textvariable=fecha_nacimiento_year, width=7).grid(row=2, column=1, padx=(140, 10), pady=5, sticky='w')

ttk.Label(window, text="Género:").grid(row=3, column=0, padx=10, pady=5)
ttk.Radiobutton(window, text="Masculino", variable=genero_var, value="Masculino").grid(row=3, column=1, padx=10, pady=5, sticky='w')
ttk.Radiobutton(window, text="Femenino", variable=genero_var, value="Femenino").grid(row=4, column=1, padx=10, pady=5, sticky='w')
ttk.Radiobutton(window, text="Otro", variable=genero_var, value="Otro").grid(row=5, column=1, padx=10, pady=5, sticky='w')

ttk.Button(window, text="Enviar", command=on_button_click).grid(row=6, column=0, columnspan=2, pady=20)

window.mainloop()

