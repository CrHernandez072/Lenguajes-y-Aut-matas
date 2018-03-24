#HERNANDEZ HERNANDEZ CRISTIAN NICOLAS
#NO.CTROL 15210528
#INSTITUTO TECNOLOGICO DE TIJUANA
#LENGUAJES Y AUTOMATAS II, GRUPO B

import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
diccionaro = {'XL3 Extra': 'Gripa y cuerpo cortado', 'Glipizida': 'Diabetes', 'MedlinePlus': 'Problemas del riñon', 'Fligain': 'Presión alta'}

medicamentos = ["Fligain", "MedlinePlus", "Glipizida", "Xl3 Extra"]
dosis = ["Tomar una cada 6 horas", "Tomar una cada 8 horas", "Tomar una cada 12 horas", "Tomar una cada 24 horas"]

aplicaciones = list(zip(medicamentos, dosis))

#Conjuntos
c_medicamentos = set(medicamentos)
c_dosis = set(dosis)
c_aplicaciones = set(aplicaciones)

def ver_receta():
	for aplicacion in c_aplicaciones:
		print ("\t",aplicacion[0], "\t", aplicacion[1])

	print("\n\n MENU ORDENAMIENTO")
	print("\t1. Enumerar receta (ENUMERATE)")
	print("\t2. Invertir receta (REVERSED)")
	print("\t3. Medicamento y sintoma (ITERITEMS)")

	opcion = int(input("\n\tIngresa tu opcion: "))
	if opcion == 1:
		for index, dosis in enumerate(c_aplicaciones, start = 1):
			print("\t\t", index, dosis)
	elif opcion == 2:
		receta_invertida = list(reversed(list(c_aplicaciones)))
		for producto, dosis in receta_invertida:
			print("\t\t", producto,"\t", dosis)
	elif opcion == 3:
		for medicamento, sintoma in diccionaro.items():
			print("\t\t", medicamento,"\t", sintoma)
	else:
		print("\tOpción incorrecta")

	input("\tenter para continuar...")

#Bandera
continuar = "si"

#ciclo de menú
while continuar == "si":
	cls()
	print("MENU INICIAL")
	print("\t1. Ver mi receta")
	print("\t2. Consultar por horas de aplicacion")
	print("\t3. Consultar por medicina")
	print("\t4. Salir")

	opcion = int(input("\n\tIngresa tu opcion: "))
	cls()
	if opcion == 1:
		ver_receta()
	elif opcion == 2:
		hora = int(input("\n\tQuiero saber mi medicamento que aplico cada (horas): "))
		
		valor = "Tomar una cada %s horas" % hora

		for aplicacion in c_aplicaciones:
			if(aplicacion[1] == valor):
				print("\t\t",aplicacion[0])
				input("\tenter para continuar...")
	elif opcion == 3:
		medicina = input("\n\tQuiero saber la hora de la medicina: ")

		for aplicacion in c_aplicaciones:
			if(aplicacion[0] == medicina):
				print("\t\t",aplicacion[1])

				input("\tenter para continuar...")
				
	elif opcion == 4:
		continuar = "no"
	else:
		print("\tOpción incorrecta")