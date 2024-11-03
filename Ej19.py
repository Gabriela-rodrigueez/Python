'''
Crear un programa para convertir una clasificación numérica (entre 0 y 10) a una letra ( de la F a la A).
'''

num=int(input("Ingresar un número del 0 al 10: "))

if num >= 9 and num <= 10:
    print("A")

if num >= 8 and num <= 9:
    print("B")

if num >= 7 and num <= 8:
    print("C")

if num >= 6 and num <= 7:
    print("D")

if num >= 0 and num <= 6:
    print("F")
    
else:
    print("Valor Desconocido")