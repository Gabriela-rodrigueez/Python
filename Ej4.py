'''Crea un sistema de reserva de Hoteles que contenga la siguiente información de una reserva:
●	Nombre.
●	Días de estancia.
●	Tarifa diaria.
●	Indicar si el cuarto tiene vista al mar.
Después mandar a imprimir los valores de cada variable.
Hacer algunos cambios y re imprimir de cada variable.
'''


print("""*** Sistema de Reserva de Hoteles ***
Clientes: Laura Martínez
Días de estancia: 5
Tarifa diaria: 1200.0
Habitación con vista al mar? True

"""
)

cliente=input("Ingrese nombre y apellido para realizar cambios en la reserva: ")
dias=input("Ingrese la cantidad de dias de estadia: ")
tarifa=1800.0
vista=input("Desea una habitacion con vista al mar? (si/no): ")


print("""
*** Sistema de Reserva de Hoteles ***""")
print(f"""Clientes: {cliente.title()}
Días de estancia: {dias}
Tarifa diaria: {tarifa}""")


if vista == "si":
    print("Habitación con vista al mar? True")
else:
    vista =="no"
    print("Habitación con vista al mar? False")
