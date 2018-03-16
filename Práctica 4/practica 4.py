#Objeto set
T =['Pŕactica', 'Práctica', 'Tareas', 'Tareas', 'Grupo', 'Grupo', 'Grupo']
ConjuntoT = set(T)

print("Conjunto T: ",ConjuntoT)

#union: quita los elementos repetidos
A = set([1,2,3,4,5, 20, 34,25, 89, 100])
B = set([3,4,5,6,7, 20,40,60])
print ("A|B: ", A|B)

#Solo muestra los elementos en común
A = set([1,2,3,4,5,20,34,25,89,100])
B = set([3,4,5,6,7,20,40,70,7,60])
print ("A&B: ", A&B)

#Resta los elementos en comun de A - B
A = set([1,7,3,4,5,20,34,25])
B = set([1,2,3,4,5,8,23,90])
print ("A-B: ", A-B)

#Uso de pertenencia
A = set([1,2,3,4,5,8,35,23,90])
print ("6 pertenece al conjunto A: ", 6 in A)
print ("1 no pertenece al conjunto A: ", 1 not in A)
print ("56 pertenece al conjunto A: ", 56 in A)
print ("68 no pertenece al conjunto A: ", 68 not in A)
print ("1 no pertenece al conjunto A: ", 1 not in A)