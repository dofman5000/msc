"""
Nombre: Operaciones.py
Objetivo: Muestra operaciones selectivas, repetitivas y aritmeticas
Autor: Carlos Adolfo hernández Gutiérrez 
Fecha: 09/11/19
"""

#------------------------------------------------------------------
#Fucnion para sumar
#------------------------------------------------------------------
def suma(num1, num2):
	res = num1 + num2
	return res

#------------------------------------------------------------------
#Fucnion para restar
#------------------------------------------------------------------
def resta(num1, num2):
	res = num1 - num2
	return res

#------------------------------------------------------------------
#Fucnion para multiplicar
#------------------------------------------------------------------
def multiplica(num1, num2):
	res = num1 * num2
	return res

#------------------------------------------------------------------
#Fucnion para dividir
#------------------------------------------------------------------
def divide(num1, num2):
	res = num1 / num2
	return res

#------------------------------------------------------------------
#Fucnion para comparar
#------------------------------------------------------------------
def comparame(num1, num2):
	if (num1 > num2):
		print("El numero uno es el mayor: ", num1, ",", num2)
	elif (num2 > num1):
		print("El numero dos es el mayor: ", num1, ",", num2)
	else:
		print("Los numeros son iguales: ", num1, ",", num2)

#------------------------------------------------------------------
#Fucnion para contar de un entero hasta otro
#------------------------------------------------------------------
def contar(num1, num2):
	if (num2>num1):
		for i in range(num1, num2+1, 1):
			print(i)
	elif(num1>num2):
		for i in range(num1,num2-1, -1):
			print(i)
	else:
		print("No hay nada que contar los numeros son iguales")

#------------------------------------------------------------------
#Funcion main
#------------------------------------------------------------------

def main():

	ciclo = "S"
	while ciclo =="S" or ciclo =="s":
		
		print("---Operaciones basicas---")
		n1 = int(input("Introduce el primer numero: "))
		n2 = int(input("Introduce el segundo numero: "))
	
		print("La suma es: ", str (suma(n1, n2)))
		print("La resta es: ", str (resta(n1, n2)))
		print("La multilpicacion es: ", str (multiplica(n1, n2)))
		print("La division es: ", str (divide(n1, n2)))
		comparame(n1, n2)
		contar(n1, n2)

		ciclo = input("¿Otra operacion (S/N)?")
	else:
		print("*** Fin de programa")

if __name__=="__main__":
	main()