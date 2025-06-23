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
    for i in range(len(ID)):
        tabla.insert('', 'end', values=(i+1, ID[i], nombre[i], edad[i], domicilio[i], retardos[i], faltas[i]))
def registrar_asistencia():
    if not ID:
        messagebox.showwarning("Atención", "No hay trabajadores registrados.")
        return
    ventana_asistencia = tk.Toplevel(ventana)
    ventana_asistencia.title("Registrar Asistencia")
    def procesar():
        try:
            idx = int(entry_num.get()) - 1
            if idx < 0 or idx >= len(ID):
                raise ValueError
            turno = float(entry_turno.get())
            actual = float(entry_actual.get())
        except ValueError:
            messagebox.showerror("Error", "Datos inválidos.")
            return
        if actual <= turno + 0.1667:
            messagebox.showinfo("Asistencia", f"Asistencia registrada a tiempo para {nombre[idx]}")
        else:
            retardos[idx] += 1
            mensaje = f"Retardo registrado para {nombre[idx]}"
            if retardos[idx] >= 3:
                faltas[idx] += 1
                retardos[idx] = 0
                mensaje += f"\n¡Falta registrada por acumulación de retardos!"
            messagebox.showwarning("Asistencia", mensaje)
        ventana_asistencia.destroy()
    tk.Label(ventana_asistencia, text="Número de trabajador (1 a {}):".format(len(ID))).pack()
    entry_num = tk.Entry(ventana_asistencia)
    entry_num.pack()
    tk.Label(ventana_asistencia, text="Hora de entrada programada (ej. 7.0):").pack()
    entry_turno = tk.Entry(ventana_asistencia)
    entry_turno.pack()
    tk.Label(ventana_asistencia, text="Hora actual (ej. 7.2):").pack()
    entry_actual = tk.Entry(ventana_asistencia)
    entry_actual.pack()
    tk.Button(ventana_asistencia, text="Registrar", command=procesar).pack(pady=10)
def ver_horario():
    try:
        hora = float(simpledialog.askstring("Hora Actual", "Ingresa la hora actual (ej. 14.5 para 2:30 pm):"))
    except:
        messagebox.showerror("Error", "Hora inválida.")
        return
    if 6 <= hora < 12:
        mensaje = "Horario actual: Mañana"
    elif 12 <= hora < 18:
        mensaje = "Horario actual: Tarde"
    else:
        mensaje = "Horario actual: Noche"
    messagebox.showinfo("Horario", mensaje)
ventana = tk.Tk()
ventana.title("Menú Principal - Control de Asistencia")
ventana.geometry("400x400")
tk.Label(ventana, text="CONTROL DE ASISTENCIA", font=("Arial", 16, "bold")).pack(pady=20)
tk.Button(ventana, text="Registrar Trabajador", width=30, height=2, command=registrar_trabajador).pack(pady=5)
tk.Button(ventana, text="Mostrar Trabajadores", width=30, height=2, command=mostrar_trabajadores).pack(pady=5)
tk.Button(ventana, text="Registrar Asistencia", width=30, height=2, command=registrar_asistencia).pack(pady=5)
tk.Button(ventana, text="Ver Horario Actual", width=30, height=2, command=ver_horario).pack(pady=5)
tk.Button(ventana, text="Salir", width=30, height=2, command=ventana.quit).pack(pady=20)
ventana.mainloop()
