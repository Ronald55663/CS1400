# gestion_tienda.py

# Este módulo contiene las funciones para gestionar el inventario de la tienda.
# Crear las 3 funciones que se describen a continuación:
# Una para agregar un producto, debe recibir inventario, nombre y precio.
# Esta debe tener un try except ValueError para manejar el error si el precio no es un número.
# Otra para buscar el precio de un producto, debe recibir inventario y nombre. Utiliza .get()
# Y una última función para listar todos los productos, debe recibir el inventario.
# Tener una opcion por si esta vacio el inventario.

# TODO #3 Agregar comenantarios a cada función explicando qué hace y cómo funciona.

def agregar_producto(inventario, nombre, precio):
    """
    Agrega un producto al inventario o actualiza su precio si ya existe.
    Recibe el inventario, el nombre del producto y el precio.
    Devuelve True si se agregó o actualizó correctamente, False si el precio no es un número.
    """
    try:
        # Convertimos a float para asegurar que sea un número
        precio_num = float(precio)
        inventario[nombre] = precio_num
        return True
    except ValueError:
        # Si no se puede convertir a número, devolvemos False
        return False

def buscar_precio(inventario, nombre):
    """
    Busca el precio de un producto en el inventario.
    Recibe el inventario y el nombre del producto.
    Utiliza .get() para obtener el precio del producto, devolviendo None si no existe.
    """
    # Usamos .get() para evitar que el programa falle si la llave no existe
    return inventario.get(nombre, None)

def listar_productos(inventario):
    """
    Muestra todos los productos registrados en el inventario.
    Si el inventario está vacío, imprime un mensaje correspondiente.
    Si contiene productos, recorre el diccionario y muestra cada producto con su precio.
    """
    if not inventario:
        print("\n> El inventario está vacío.")
    else:
        print("\n--- Inventario Actual ---")
        for producto, precio in inventario.items():
            print(f"• {producto}: ${precio:.2f}")