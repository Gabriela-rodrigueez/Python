'''
Crea un programa para validar el usuario y password proporcionados por el usuario. 
Crea 2 constantes con los valores correctos y posteriormente compara que el usuario y password proporcionados por el usuario sean válidos.
Debe solicitar el usuario y el password al usuario y si son iguales que los valores correctos almacenados en las constantes deben imprimir True, de lo contrario debe imprimir False.
'''

print("""*** Sistema de Autenticación ***""")

valid_usuario=input("Cuál es tu usuario?: ")
valid_password=input("Cuál es tu password?: ")

usuario=("admin-acosta")
password=("863401HE")

if valid_usuario == usuario:
    print("Daros correctos? True")
    
elif valid_password != password:
    print("Daros correctos? False")