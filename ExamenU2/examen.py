#HERNANDEZ HERNANDEZ CRISTIAN NICOLAS
#NO.CTROL 15210528
#INSTITUTO TECNOLOGICO DE TIJUANA
#LENGUAJES Y AUTOMATAS II, GRUPO B

import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#Solicitar empleados
cls() #Limpio pantalla
print(" Agrega los nombres de los empleados")
programador_1 = input("\tIngresa un usuario: ")
programador_2 = input("\tIngresa otro usuario: ")
	
#Los empleados son guardados en tuplas
tupla_programadores = (programador_1, programador_2)

lista_horas= [0, 0]
#metodo para agregar horas a los empleados

def agregar_horas():
	index = 0
	for programador in tupla_programadores:
		print ("\t" + str(index) + ".", programador)
		index = index + 1

	#se ingresa la opcion del usuario
	opcion = int(input("\n\tA que empleado le vas agregar las horas: "))
	
	#Valida que la opcion ingresada sea correcta
	if opcion > len(tupla_programadores):
		input("\n\tNo existe este programador")
		return
	
	cantidad = int(input("\tCuantas horas: "))

	if cantidad > 0:
		lista_horas[opcion] = lista_horas[opcion] + cantidad	
		input("\tSe ha guardado la cantidad de horas, enter...")
	else:
		input("\tLa hora es menor o igual a cero, enter...")

def generar_reporte():
	print("\tTRABAJADOR")
	for empleado in zip(tupla_programadores, lista_horas):
		if(int(empleado[1]) <= 40):
			print("\t",empleado[0])
			print("\t\tHoras totales:",empleado[1])
			print("\t\tHoras extras: 0")
			print("\t\tSueldo:", empleado[1] * 300)
		else:
			horas_extras = int(empleado[1]) - 40
			sueldo_normal = 40 * 300
			sueldo_extra = horas_extras * (300 * 1.05)
			print("\t",empleado[0])
			print("\t\tHoras trabajadas:",empleado[1])
			print("\t\tHoras extras:",horas_extras)
			print("\t\tSueldo rutina normal:", sueldo_normal)
			print("\t\tSueldo extra:",sueldo_extra)
			print("\t\tSueldo total:",(sueldo_normal + sueldo_extra))

	input("\n\tenter para continuar...")	

#Bandera
continuar = "si"

#ciclo de menú
while continuar == "si":
	cls()
	print("MENU INICIAL")
	print("\t1. Agregar horas trabajadas")
	print("\t2. Ver informe")
	print("\t3. Salir")

	opcion = input("\n\tIngresa tu opcion: ")
	cls()
	if opcion == "1":
		agregar_horas()
	elif opcion == "2":
		generar_reporte()
	elif opcion == "3":
		continuar = "no"
	else:
		print("\tOpción incorrecta")