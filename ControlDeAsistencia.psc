Algoritmo ControlDeAsistencia
	Dimension ID[100], nombre[100], domicilio[100]
	Dimension edad[100], retardos[100], faltas[100]
	Definir ID, nombre, domicilio Como Cadena
	Definir edad, retardos, faltas Como Entero
	Definir i, opcion, cont, idx Como Entero
	Definir hora, turnoEntrada Como Real
	i <- 1
	cont <- 0
	Repetir
		Escribir "------ MENÚ PRINCIPAL ------"
		Escribir "1. Registrar trabajador"
		Escribir "2. Mostrar trabajadores"
		Escribir "3. Mostrar horario actual"
		Escribir "4. Registrar asistencia"
		Escribir "5. Salir"
		Escribir "Selecciona una opción:"
		Leer opcion
		Segun opcion Hacer
			1:
				RegistraNombre(ID, nombre, edad, i, domicilio, retardos, faltas)
				i <- i + 1
				cont <- cont + 1
			2:
				MostrarTrabajadores(ID, nombre, edad, i, domicilio, cont)
			3:
				Escribir "Ingresa la hora actual (ejemplo: 14.5 para 2:30 pm):"
				Leer hora
				MostrarHorario(hora)
			4:
				Si cont = 0 Entonces
					Escribir "No hay trabajadores registrados aún."
				SiNo
					Escribir "Ingresa el número del trabajador (1 a ", cont, "):"
					Leer idx
					Si idx >= 1 Y idx <= cont Entonces
						Escribir "Ingresa la hora de entrada programada (ej. 7.0):"
						Leer turnoEntrada
						Escribir "Ingresa la hora actual:"
						Leer hora
						RegistrarAsistencia(hora, turnoEntrada, idx, retardos, faltas, nombre)
					SiNo
						Escribir "Número de trabajador inválido."
					FinSi
				FinSi
			5:
				Escribir "Saliendo del programa..."
			De Otro Modo:
				Escribir "Opción no válida. Intente nuevamente."
		FinSegun
	Hasta Que opcion = 5
	
FinAlgoritmo
Funcion RegistraNombre(ID, nombre, edad, i, domicilio, retardos, faltas)
    Escribir "Registro del trabajador ", i
    Escribir "Ingresa el ID del trabajador:"
    Leer ID[i]
    Escribir "Ingresa el nombre del trabajador:"
    Leer nombre[i]
    Escribir "Ingresa la edad del trabajador:"
    Leer edad[i]
    Escribir "Ingresa tu domicilio:"
    Leer domicilio[i]
    retardos[i] <- 0
    faltas[i] <- 0
    Escribir "¡Te has registrado con éxito!"
FinFuncion
Funcion MostrarTrabajadores(ID, nombre, edad, i, domicilio, cont)
    Si cont > 0 Entonces
        Escribir "Registros actuales: ", cont
        Para f <- 1 Hasta cont Con Paso 1 Hacer
            Escribir "ID: ", ID[f], " - Nombre: ", nombre[f], " - Edad: ", edad[f], " - Domicilio: ", domicilio[f]
        Fin Para
    SiNo
        Escribir "No se han encontrado registros."
    Fin Si
FinFuncion
Funcion MostrarHorario(hora)
    Si hora >= 6 Y hora < 12 Entonces
        Escribir "Horario actual: Mañana"
    SiNo
        Si hora >= 12 Y hora < 18 Entonces
            Escribir "Horario actual: Tarde"
        SiNo
            Escribir "Horario actual: Noche"
        Fin Si
    Fin Si
FinFuncion
Funcion RegistrarAsistencia(hora, turnoEntrada, i, retardos, faltas, nombre)
    Si hora <= turnoEntrada + 0.1667 Entonces  // 10 minutos de tolerancia
        Escribir "Asistencia registrada a tiempo para ", nombre[i]
    SiNo
        Escribir "Retardo registrado para ", nombre[i]
        retardos[i] <- retardos[i] + 1
        Si retardos[i] >= 3 Entonces
            faltas[i] <- faltas[i] + 1
            retardos[i] <- 0
            Escribir "¡Se ha registrado una falta para ", nombre[i], " por acumulación de retardos!"
        Fin Si
    Fin Si
FinFuncion