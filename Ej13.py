'''Solicitar al usuario un valor entre 0 y 5 e indicarle si el valor proporcionado está dentro de rango. 
Se deben definir 2 constantes, VALOR_MINIMO = 0 y VALOR_MAXIMO = 5.
Y debemos comprobar si el valor proporcionado se encuentra en el rango entre 0 y 5.
Finalmente se debe imprimir:
Valor dentro de rango: True/False
'''


num=float(input("ingrese un num entre 0 y 5: "))
valor_minimo=0
valor_maximo=5

if num <= valor_maximo and num >= valor_minimo:
    print("Valor dentro del rango: True")
else:
    num >= valor_maximo and num <= valor_minimo
    print("Valor dentro del rango: False")