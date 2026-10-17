#Ronald Medi
"""Tarea 1: Preparando la Oferta (Listas y Tuplas)

"""

# Tarea 1: Lista de elementos para el altar de muertos

# Lista de ofrendas editables (pueden agregarse o quitarse elementos)
ofrendas = ["Pan de muerto", "Flor de cempasúchil", "Velas", "Calaverita de azúcar"]

# Tupla con los niveles tradicionales del altar (constante, no debe cambiar)

NIVELES_ALTAR = ("Cielo", "Tierra", "Inframundo")

# Mostrar la segunda ofrenda (índice 1)
print("Segunda ofrenda:", ofrendas[1])

"""
Ejecuta el código. Observa qué elemento se imprime al pedir el índice 1.
#1. Modificación 1 (Listas): Agrega un nuevo elemento a la lista ofrendas usando
 .append("Incienso copal") y luego ordena la lista alfabéticamente usando
 la función .sort().  ¿Qué notas del variable en linea #12?

#2. Modificación 2 (Tuplas): Intenta modificar el primer elemento de la tupla escribiendo
 NIVELES_ALTAR[0] = "Gloria".
 ¿Qué sucede al ejecutar el código y por qué no permite realizar este cambio?

#3. Utiliza la función enumerate() dentro de un bucle for para imprimir cada ofrenda
 de tu lista junto con su número de posición en el altar.
"""

 # Respuesta a la Modificación 1
 # Al agregar un nuevo elemento a la lista ofrendas y ordenarla alfabéticamente, la lista se actualiza y se reorganiza según el orden alfabético de los elementos. La variable ofrendas ahora contiene el nuevo elemento "Incienso copal" y todos los elementos están en orden alfabético.
 
# 2. Respuesta a la Modificación 2
# Al intentar modificar el primer elemento de la tupla NIVELES_ALTAR, se produce un error de tipo TypeError. Esto ocurre porque las tuplas son inmutables, lo que significa que no se pueden cambiar sus elementos una vez que se han creado. Por lo tanto, no es posible asignar un nuevo valor a un elemento de la tupla.

# 3. Utilizar enumerate() para imprimir cada ofrenda con su posición 
print("Ofrendas con su número de posición:")
# Respuesta 3: # La función enumerate() permite recorrer una lista y obtener # tanto el número de posición como el elemento correspondiente. # Con start=1, la numeración comienza en 1.