import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#Tupla de computadoras y su precio
computadoras = (["Dell", 8800], ["HP", 7400], ["Asus", 9210.99])

#Tupla de procesadores y su precio
procesadores = (["i3", 4050], ["i5", 5105.99], ["i7", 6190.99])

carrito = [] #Carrito de compras
iva = 1.16 #porcentaje de impuestos

def elegir_producto(tipo, tupla_producto):
	index = 0

	print(tipo + " DISPONIBLES")
	for producto in tupla_producto:
		print ("\t" + str(index) + ".", producto)
		index = index + 1

	#se ingresa la opcion del usuario
	opcion = input("\n\tIngresa tu opcion: ")
	
	#precio del producto selecionado
	precio_producto = tupla_producto[int(opcion)][1] * iva

	#auxiliar del presupuesto
	disponible = 27000

	#se recorre el carrito, y para cada producto del carrito se disminuira el precio del auxiliar de presupuesto
	for producto in carrito:
		disponible = disponible - producto[1] * iva

	#si el presupuesto disponible es mayor al del producto seleccionada
	#se agregará producto al carrito
	if disponible > precio_producto:
		carrito.append(tupla_producto[int(opcion)])
		input("\n\tSe agrego el producto, enter para continuar... ")
	else:
		input("\n\tNo se agrego el producto, enter para continuar... ")


def total_carrito():
	print("TU CARRITO")

	subtotal = 0
	total = 0

	#Muestra todos los productos dentro del carrito
	for producto in carrito:
		print ("\t" + str(producto))
		subtotal = subtotal + producto[1]

	total = subtotal * iva
	print("\n\tSUBTOTAL: %.2f" % subtotal)
	print("\tTOTAL: %.2f" % total)

	#mensaje de salida
	input("\n\tEnter para continuar... ")

def modificar_carrito():
	index = 0
	print("TU CARRITO TIENE LOS PRODUCTOS")
	for producto in carrito:
		print ("\t" + str(index) + ".", producto)
		index = index + 1

	opcion = input("\n\tQuiero quitar el producto: ")
	carrito.remove(carrito[int(opcion)])

continuar = "si"
while continuar == "si":
	cls()
	print("MENU INICIAL")
	print("\t1. Ver computadoras")
	print("\t2. Ver procesadores")
	print("\t3. Ver mi carrito")
	print("\t4. Modificar mi carrito")
	print("\t5. Salir")

	opcion = input("\n\tIngresa tu opcion: ")
	cls()
	if opcion == "1":
		elegir_producto("COMPUTADORAS", computadoras)
	elif opcion == "2":
		elegir_producto("PROCESADORES", procesadores)
	elif opcion == "3":
		total_carrito()
	elif opcion == "4":
		modificar_carrito()
	elif opcion == "5":
		continuar = "no"
	else:
		print("\tOpción incorrecta")