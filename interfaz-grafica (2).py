import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
ID = []
nombre = []
domicilio = []
edad = []
retardos = []
faltas = []
def registrar_trabajador():
    def guardar():
        id_trab = entrada_id.get()
        nom = entrada_nombre.get()
        try:
            ed = int(entrada_edad.get())
        except ValueError:
            messagebox.showerror("Error", "Edad inválida.")
            return
        dom = entrada_domicilio.get()

        if not id_trab or not nom or not dom:
            messagebox.showwarning("Atención", "Todos los campos son obligatorios.")
            return
        ID.append(id_trab)
         messagebox.showinfo("Éxito", "¡Trabajador registrado con éxito!")
        ventana_registro.destroy()
    ventana_registro = tk.Toplevel(ventana)
    ventana_registro.title("Registrar Trabajador")
    tk.Label(ventana_registro, text="ID:").grid(row=0, column=0, padx=10, pady=5)
    entrada_id = tk.Entry(ventana_registro)
    entrada_id.grid(row=0, column=1)
    tk.Label(ventana_registro, text="Nombre:").grid(row=1, column=0, padx=10, pady=5)
    entrada_nombre = tk.Entry(ventana_registro)
    entrada_nombre.grid(row=1, column=1)
    tk.Label(ventana_registro, text="Edad:").grid(row=2, column=0, padx=10, pady=5)
    entrada_edad = tk.Entry(ventana_registro)
    entrada_edad.grid(row=2, column=1)
    tk.Label(ventana_registro, text="Domicilio:").grid(row=3, column=0, padx=10, pady=5)
    entrada_domicilio = tk.Entry(ventana_registro)
    entrada_domicilio.grid(row=3, column=1)
    tk.Button(ventana_registro, text="Guardar", command=guardar).grid(row=4, column=0, columnspan=2, pady=10)
def mostrar_trabajadores():
    ventana_lista = tk.Toplevel(ventana)
    ventana_lista.title("Lista de Trabajadores")
    ventana_lista.geometry("800x300")
    columnas = ('#', 'ID', 'Nombre', 'Edad', 'Domicilio', 'Retardos', 'Faltas')
    tabla = ttk.Treeview(ventana_lista, columns=columnas, show='headings')
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, anchor='center', width=100)
    tabla.pack(expand=True, fill='both', padx=10, pady=10)
        nombre.append(nom)
        edad.append(ed)
        domicilio.append(dom)
        retardos.append(0)
        faltas.append(0)
