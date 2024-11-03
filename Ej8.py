'''Crea un programa para generar un email a partir de los siguientes datos:
●	Nombre: Alfredo Vazquez
●	Empresa/Terciario: Instituto Educativo Superior Manuel Belgrano
●	Dominio: com.ar
Resultado: 
Email: alfredo.vazquez@iesmb.com.ar
Este es el resultado del programa: 
'''

nombre="Alfredo Vazquez"
empresa_terciario="Instituto Educativo Superior Manuel Belgrano"
dominio=(".com.ar")

nombre_normalizado= nombre.lower().replace(" ",".")

# split lo de contiene empresa_terciaria_normalizada en cadena
# "".join justa la cadena
# letra[0(primera letra)] for letra in empresa_terciario

empresa_terciario_normalizado= "".join([letra[0] for letra in empresa_terciario.split()])
email= (f"{nombre_normalizado}@{empresa_terciario_normalizado}{dominio}")

print(f"""*** Generador de Email***
Nombre usuario: {nombre}
Nombre usuario normalizado: {nombre_normalizado}

Nombre empresa: {empresa_terciario}
Extensión del dominio: {dominio}
Dominio de email normalizado: {empresa_terciario_normalizado.lower()}

Email final generado: {email.lower()}"""
)
