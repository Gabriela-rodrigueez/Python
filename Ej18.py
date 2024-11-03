'''Se solicita proporcionar el valor de un mes (con valor numérico entre 1 y 12), e indicar la estación del año según lo siguiente:'''


mes= int(input("ingrese el mes en valor númerico entre 1 y 12: "))

if mes == 1 or mes == 2 or mes == 12 :
    print("La estación del año es Invierno")
    
if mes == 3 or mes == 4 or mes == 5:
    print("La estación del año es Primavera")
    
if mes == 6 or mes == 7 or mes == 8:
    print("La estación del año es Verano")
    
if mes == 9 or mes == 10 or mes == 11:
    print("La estación del año es Otoño")
    
if mes >= 13 or mes <=13 or mes<=0:
    print("Estación Desconocida")
    
