'''Crear el detalle de un producto de una tienda online.
●	Nombre del producto.
●	Precio del producto.
●	Cantidad en el inventario.
●	Indicar si está disponible.
Hacer algunos cambios y mandar a imprimir nuevamente el nuevo valor de las variables.
'''

print("""*** Sistema de Tienda Online ***
Producto: Cámara digital
Precio: $ 399.99
Cantidad en el inventario: 20
Disponible: True

"""
)

nombre_producto=input("Ingrese nombre del producto: ")
precio_producto=1990.0
Cantidad_inventario= 34
disponibilidad= ("True")
    
print("""
*** Sistema de Tienda Online ***""")
print(f"""Producto : {nombre_producto.title()}
Precio: $ {precio_producto}
Cantidad en el inventario: {Cantidad_inventario}
Disponible: {disponibilidad}
""")
