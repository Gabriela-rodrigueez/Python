'''Crear un sistema que ofrezca descuentos dependiendo del monto de la compra, o si es miembro de la tienda.
Se deben revisar las siguientes condiciones:
1.	Si ha comprado más de $1000 y es miembro -> Descuento de 10%.
2.	Si sólo es miembro -> Descuento de 5%.
3.	Si no es miembro -> Descuento de 0%.
'''
monto_compra=0
descuento1=(0.9) 
si_miembro=(0.05)
no_miembro=(0)

monto_compra=float(input("ingrese el monto de su compra: "))
miembro=input("¿Es miembro de la tienda? (si/no): ").strip().lower()=='si'

if miembro:
    if monto_compra >= 1000:
        print("Por su compra superior a $1000 y ser miembro, obtuvo un descuento del 10%","y su total es: ", (monto_compra*descuento1))
    
    else:    
        print("Por ser miembro obtuvo un descuento del 5% "," y su total es: ", (monto_compra*(1-si_miembro)))    
else:
    print("No es miembro y su descuento es del 0% ","y su total es: ", (monto_compra))