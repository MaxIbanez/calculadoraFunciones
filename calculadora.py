	#INT = es un numero entero
	#STR = es una palabra o letra o numero (no tiene valor matematico)
	#FLOAT = es un decimal
	#BOOL = es un valor binario (True, False)

def Suma(listaSum):
	total = 0
	indice = 0
	while(indice < len(listaSum)):		
		total = total + listaSum[indice]
		indice+=1
	print (total)

def Resta(listaRest):
	total = 0
	indice = 0
	while(indice < len(listaRest)):
		total = total - listaRest[indice]
		indice+=1
	print (total)

def Division(div1,div2):
	divi = div1/div2
	print (divi)


def Multiplicar(multi1,multi2):
	multi = multi1*multi2
	print (multi)

def Porcentaje(n1,n2):
	porcen = (n2*100)/n1
	print (porcen)


def Raiz(r):
	raiz = r**(1/2)
	print(raiz)

def Potencia(n1,n2):
	total = n1**n2
	print(total)




def calculadora():
	n1 = 0
	n2 = 0
	lista = []

	
	print("BIENVENIDO a la calculadora")
	print("1) calcular Potencia entre 2 numeros")
	print("2) calcular raiz cuadrada de un numero") 
	print("3) calcular porcentaje entre 2 numeros") 
	print("4) Multiplicar 2 numeros") 
	print("5) Dividir 2 numeros")
	print("6) Restar numeros") 
	print("7) Sumar numeros")
	print ("Que accion desea hacer? (elegir etre 1 y 7) -> ")

	opcion = int(input())

	if opcion == 1:
		n1 = int(input("Ingrese 1er numero: "))
		n2 = int(input("Ingrese 2do numero: "))
		Potencia(n1,n2)
		n1 = 0
		n2 = 0
	elif opcion == 2:
		n1 = int(input("Ingrese numero: "))
		Raiz(n1)
		n1 = 0
	elif opcion == 3:
		n1 = int(input("Ingrese 1er numero: "))
		n2 = int(input("Ingrese 2do numero: "))
		Porcentaje(n1,n2)
		n1 = 0
		n2 = 0
	elif opcion == 4:
		n1 = int(input("Ingrese 1er numero: "))
		n2 = int(input("Ingrese 2do numero: "))
		Multiplicar(n1,n2)
		n1 = 0
		n2 = 0
	elif opcion == 5:

		n1 = int(input("Ingrese 1er numero: "))
		n2 = int(input("Ingrese 2do numero: "))
		Division(n1,n2)
		n1,n2 = 0,0
	elif opcion == 6:

		maximo = int(input("Cuantos numeros desea sumar?: "))
		contador = 0
		#[0,1,2,3,4,5,6...,n-1]


		while contador < maximo:
			numero = int(input("Ingrese numeros: "))
			print (lista)
			lista.append(numero)
			contador+=1
		Resta(lista)
		
		lista = []
	elif opcion == 7:
		maximo = int(input("Cuantos numeros desea Restar?: "))
		contador = 0
		#[0,1,2,3,4,5,6...,n-1]


		while contador < maximo:
			numero = int(input("Ingrese numeros: "))
			lista.append(numero)
			contador+=1
		Suma(lista)
		lista = []
	else:
		print ("La opcion elegida no existe, ejecutar programa nuevamente.")

calculadora()