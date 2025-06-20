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
        nombre.append(nom)
        edad.append(ed)
        domicilio.append(dom)
        retardos.append(0)
        faltas.append(0)
