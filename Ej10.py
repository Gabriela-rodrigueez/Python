'''Crea un programa para solicitar algunos valores importantes para una receta de cocina.
Los valores que debe introducir el usuario son:
●	Nombre de la receta.
●	Ingredientes.
●	Tiempo de preparación (en minutos).
●	Dificultad (“Fácil, Media, Alta”).
'''

nom_receta=input("Ingrese el nombre de la receta: ")
ingredientes=input("Ingresar lo ingredientes, separados por coma(,): ")
tiempo=input("Ingrese el tiempo de preparación (en minutos): ")
dificultad=input("ingresar dificultad (Fácil, Media, Alta): ")


print(f"""
*** Receta de Cocina ***
Receta: {nom_receta.title()}
Ingredientes: {ingredientes.title()}
Tiempo de preparación: {tiempo}
Dificultad: {dificultad.title()}""")

