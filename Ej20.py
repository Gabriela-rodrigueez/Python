'''Crea un programa para determinar el costo de envío de un paquete según el destino o internacional, y el peso del paquete.
El programa debe solicitar 2 valores: 
1.	Destino(nacional o internacional).
2.	Peso(kilogramos) del paquete.
Al final debe imprimir el costo de envío del paquete

'''

destino=input("Ingrese el destino (nacional o internacional): ")
peso=float(input("Ingrese el peso del paquete en kilogramos: "))

costos = (destino , peso)
costo_envio = costos(destino, peso)
costo1= 10*peso
costo2 = 20*peso

def costos(destino, peso):
    if destino.lower() == "nacional":
        return costo1
      
    elif destino.lower() == "internacional":
        return costo2


if costo_envio:
    print(f"El costo del paquete es: {costo_envio}")
        
else:
    print("El destino es inválido")