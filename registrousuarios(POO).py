ID = []
nombre = []
domicilio = []
edad = []
retardos = []
faltas = []
def registra_nombre():
    print(f"Registro del trabajador {len(ID) + 1}")
    ID.append(input("Ingresa el ID del trabajador: "))
    nombre.append(input("Ingresa el nombre del trabajador: "))
    edad.append(int(input("Ingresa la edad del trabajador: ")))
    domicilio.append(input("Ingresa tu domicilio: "))
    retardos.append(0)
    faltas.append(0)
    print("¡Te has registrado con éxito!\n")
def mostrar_trabajadores():
    if len(ID) > 0:
        print(f"Registros actuales: {len(ID)}")
        for i in range(len(ID)):
            print(f"ID: {ID[i]} - Nombre: {nombre[i]} - Edad: {edad[i]} - Domicilio: {domicilio[i]}")
    else:
        print("No se han encontrado registros.")
    print()
def mostrar_horario(hora):
    if 6 <= hora < 12:
        print("Horario actual: Mañana")
    elif 12 <= hora < 18:
        print("Horario actual: Tarde")
    else:
        print("Horario actual: Noche")
    print()
def registrar_asistencia(hora, turno_entrada, idx):
    if hora <= turno_entrada + 0.1667:  # 10 minutos de tolerancia
        print(f"Asistencia registrada a tiempo para {nombre[idx]}")
    else:
        print(f"Retardo registrado para {nombre[idx]}")
        retardos[idx] += 1
        if retardos[idx] >= 3:
            faltas[idx] += 1
            retardos[idx] = 0
            print(f"¡Se ha registrado una falta para {nombre[idx]} por acumulación de retardos!")
    print()
while True:
    print("------ MENÚ PRINCIPAL ------")
    print("1. Registrar trabajador")
    print("2. Mostrar trabajadores")
    print("3. Mostrar horario actual")
    print("4. Registrar asistencia")
    print("5. Salir")
    opcion = input("Selecciona una opción: ")
    if opcion == '1':
        registra_nombre()
    elif opcion == '2':
        mostrar_trabajadores()
    elif opcion == '3':
        hora = float(input("Ingresa la hora actual (ejemplo: 14.5 para 2:30 pm): "))
        mostrar_horario(hora)
    elif opcion == '4':
        if len(ID) == 0:
            print("No hay trabajadores registrados aún.\n")
        else:
            idx = int(input(f"Ingresa el número del trabajador (1 a {len(ID)}): ")) - 1
            if 0 <= idx < len(ID):
                turno_entrada = float(input("Ingresa la hora de entrada programada (ej. 7.0): "))
                hora_actual = float(input("Ingresa la hora actual: "))
                registrar_asistencia(hora_actual, turno_entrada, idx)
            else:
                print("Número de trabajador inválido.\n")
    elif opcion == '5':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.\n")