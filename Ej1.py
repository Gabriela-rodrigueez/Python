'''Realizar un programa en Python para presentarte. La salida de tu programa debe ser similar al siguiente:
Nombre: Juan Perez
Edad: 28
Pais: Mexico
¡Ojo! En nombre y en país no puedo colocar ningún valor entero y en edad no puedo poner un valor alfabético.'''

nombre=input("Ingrese nombre y apellido: ")
edad=input("Ingresar edad: ")
pais=input("Ingrese el país de donde es: ")

# .split() divide la cadena para ingresar el nombre completo 
# .isalpha() para verificar si todos los caracteres de una cadena son letras
# .isdigit() verifica si los caracteres son digitos del 0 al 9
# not invierte de True a False y viceversa
if not all(letras.isalpha() for letras in nombre.split()):
    print("el nombre no puede contener números")
elif not edad.isdigit():
    print("la edad tiene que contener un valor numérico")
elif not pais.isalpha():
    print("el país no puede contener números")
else:
    print(f"Nombre: {nombre.title()}")
    print(f"Edad: {edad}")
    print(f"País: {pais.title()}")