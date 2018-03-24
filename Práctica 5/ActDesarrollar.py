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
	
	if int(opcion) > len(carrito):
		input("\n\tEl producto no está disponible")
		return
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

	print("\n\ingresa ", len(carrito) + 1, " para cancelar")
	opcion = input("\tQuiero quitar el producto: ")

	if int(opcion) > len(carrito):
		return

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

	# opcion = input("\n\tIngresa tu opcion: ")
	opcion = "5"
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


print("\n Variables que se manejaron y su LITERAL")
print("\tcomputadoras\n\t\tValor",computadoras,"\n\t\tTipo: ", type(computadoras))
print("\tprocesadores\n\t\tValor",procesadores,"\n\t\tTipo: ", type(procesadores))
print("\tcarrito\n\t\tValor:",carrito,"\n\t\tTipo: ", type(carrito))
print("\tiva\n\t\tValor",iva,"\n\t\tTipo: ", type(iva))
print("\tcontinuar\n\t\tValor",continuar,"\n\t\tTipo: ", type(continuar))
print("\ttotal_carrito\n\t\tValor",total_carrito,"\n\t\tTipo: ", type(total_carrito))
print("\telegir_producto\n\t\t",elegir_producto,"\n\t\tTipo: ", type(elegir_producto))
print("\tmodificar_carrito\n\t\tValor",modificar_carrito,"\n\t\tTipo: ", type(modificar_carrito))

print("\n Literales que se utilizaron:")
print("\tSUBTOTAL: %.2f % subtotal")
print("\tTOTAL: %.2f")
print("\tingresa , len(carrito) + 1,  para cancelar")