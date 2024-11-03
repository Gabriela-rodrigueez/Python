'''Crear un sistema para validar los valores de usuario y password proporcionados.
Se deben definir dos constantes con los valores validos de usuario y password
Y el sistema debe comparar los valores validos contra los valores proporcionados. Se deben considerar 4 casos:
1.	Usuario y password válidos. Debe imprimir ‘Bienvenido al sistema’.
2.	Usuario inválido.
3.	Password inválido. 
4.	Usuario y password inválidos.
'''


print("""*** Sistema de Autenticación ***""")

valid_usuario=input("Cuál es tu usuario?: ")
valid_password=input("Cuál es tu password?: ")

usuario=("admin-acosta")
password=("863401HE")


if valid_usuario == usuario and valid_password == password:
    print("'Bienvenido al sistema'")
    
if valid_usuario != usuario:
    print("Usuario inválido")
     
if valid_password != password:
    print("Password inválido")
    
elif valid_usuario != usuario and valid_password != password:
    print("Usuario y password inválidos")
