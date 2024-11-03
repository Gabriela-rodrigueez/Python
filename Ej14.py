'''Se solicita calcular el área y perímetro de un rectángulo aplicando las siguientes formulas:
área = base * altura
perímetro = 2 * (base + altura)
'''

altura=0
base=0
altura=float(input("introducir la altura: "))
base=float(input("introducir la base: "))

area= base * altura
perimetro= 2*(base + altura)

print(f"El área del rectángulo es: {area} ")
print(f"El perímetro del rectángulo es: {perimetro} ")
