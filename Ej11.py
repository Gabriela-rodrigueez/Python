'''Se solicita crear un sistema para generar un ID único para cada persona. El sistema debe solicitar al usuario:
●	Nombre.
●	Apellido.
●	Año de nacimiento(YYYY)
1.	Del valor recibido de nombre, usar sólo las 2 primeras letras y convertirlas a mayúsculas.
2.	Del valor de apellido, usar las 2 primeras letras y convertirlas a mayúsculas.
3.	Del valor de año, tomar los 2 últimos dígitos.
Además, el sistema deberá generar un valor aleatorio de 4 dígitos, con ayuda de la función randint.
'''

print("**** Sistema Generador de ID Unico ***")

nombre=input("Cuál es tu nombre: ")
apellido=input("Cuál es tu apellido: ")
año_nacimiento=int(input("Cuál es tu año de nacimiento (YYYY): "))

iniciales_nombre= (nombre)[:2]
iniciales_apellido= (apellido)[:2]
num_año= str(año_nacimiento)[2:]

import random
aleatorio=random.randint(1000, 9999)

id=(f"{iniciales_nombre.upper()}{iniciales_apellido.upper()}{num_año}{aleatorio}")

print(f"""
Hola {nombre.title()},
	Tu nuevo número es identificación (ID) generado por el sistema es:
 	{id}
	Felicidades!""")

