'''Crea un programa para indicar cual es el mayor de dos números.
El programa debe pedir al usuario dos números enteros.
Posteriormente se deben comparar y mandar a imprimir el número mayor.
'''

num1=0
num2=0

num1=int(input("Ingrese el primer número entero: "))
num2=int(input("Ingrese el segundo número entero: "))

if num1 > num2:
    print(f"el número mayor es: {num1} ")
    
elif num2 > num1:
    print(f"el número mayor es: {num2} ")
    
else:
    num1 == num2
    print("los dos números ingresados son iguales")

    
    