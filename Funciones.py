"""
Nombre: Funciones.py
Objetivo: muestra el formato de funciones en Phyton
Autor: Carlos Adolfo hernández Gutiérrez 
Fecha: 09/11/19
"""
#---------------------------------------------------
#Funcion para imprimir un mensaje
#---------------------------------------------------
def printMensaje():
	print("Hola soy una funcion sin parametros")

#---------------------------------------------------
#Funcion para regresar un mensaje
#---------------------------------------------------
def printMensajeDos():
	return "Soy la funcion que regresa una cadena"

#---------------------------------------------------
#Funcion recibe un mensaje y lo imprime
#---------------------------------------------------
def printMensajeTres(cad):
	print("Mensaje recibido: ", cad)

#---------------------------------------------------
#Funcion main, la primer funcion que se ejecuta
#---------------------------------------------------
def main():
	printMensaje()
	print("El mensaje es:", printMensajeDos())
	printMensajeTres("Soy la funcion tres")

if __name__=="__main__":
	main()