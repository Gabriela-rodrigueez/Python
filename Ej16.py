'''Se solicita crear un sistema de reservación de un hotel. Se debe pedir la siguiente información al usuario:
●	Nombre de cliente.
●	Días de estadía en el hotel.
●	¿Cuánto con vistas al mar?
El hotel tiene las siguientes tarifas:
●	Cuarto sin vista al mar: $10.000 por día.
●	Cuarto con vistas al mar: $15.000 por día.
El sistema debe calcular el costo total de la estadía dependiendo si escogió un cuarto con vistas al mar o no. Además de indicar si escogió un cuarto con vistas al mar o no.
'''



nombre=input("ingrese su nombre: ")
dias=int(input("Ingrese la cantidad de días en el hotel: "))
vista=input("Cuarto con vista al mar? (si/no): ")
sin_vista= 10000.00*dias
con_vista= 15000.00*dias

if vista == "si":
    print("Habitación con vista al mar")
    print(f"El costo total de su estadia en el hotel es: $ {con_vista}")
else:
    vista =="no"
    print("Habitación sin vista al mar")
    print(f"El costo total de su estadia en el hotel es: $ {sin_vista}")

