# Ronald Medina

# =============================================================
# Parte 1: Funciones sin retorno (Acciones directas)
# =============================================================

def mostrar_bienvenida(nombre):
    """
    Muestra un mensaje de bienvenida personalizado para el usuario.

    Parámetros:
    - nombre: El nombre del usuario a quien se le dará la bienvenida.
    """
    print(f"¡Hola, {nombre}! Bienvenido a clase hoy.")

# PREGUNTAS:
# 1. En la función mostrar_bienvenida(nombre), ¿cómo se llama la variable "nombre" dentro de los paréntesis?
# La variable "nombre" dentro de los paréntesis se llama parámetro.

# 2. ¿Qué le falta al código para ser completamente reutilizable?
# Falta que la función devuelva un valor en lugar de solo imprimirlo, si queremos reutilizar el mensaje en otras partes del programa.


# =============================================================
# Parte 2: Funciones con retorno (Procesamiento de datos)
# =============================================================

def calcular_descuento(precio, porcentaje=10):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final

def es_par(numero):
    return numero % 2 == 0

# PREGUNTAS:
# 3. ¿Qué palabra clave (keyword) de Python se utiliza para indicar que estamos definiendo una función?
# La palabra clave es "def".

# 4. Escribe los nombres de las dos funciones definidas arriba.
# Los nombres de las funciones son "calcular_descuento" y "es_par".

# 5. ¿Qué sucede cuando llamas a la función pasando solo un argumento, como calcular_descuento(100)?
# Se utiliza el valor por defecto del parámetro "porcentaje", que es 10.

# 6. ¿Qué ocurre si pasas dos argumentos, como calcular_descuento(200, 20)?
# Se utiliza el valor proporcionado para el parámetro "porcentaje", en este caso 20.


# =============================================================
# Parte 3: Pruebas de ejecución
# =============================================================

print("--- PRUEBA 1: Mostrar Bienvenida ---")
mostrar_bienvenida("Ana")
mostrar_bienvenida("Carlos")

print("\n--- PRUEBA 2: Cálculo de Descuentos ---")

compra_1 = calcular_descuento(100)
print(f"Precio con descuento por defecto: ${compra_1}")


compra_2 = calcular_descuento(200, 20)
print(f"Precio con 20% de descuento: ${compra_2}")

# PREGUNTAS:
# 7. Escribe el pseudocódigo de las funciones en la Parte 2.
# Pseudocódigo de calcular_descuento:
##función calcular_descuento(precio, porcentaje=10)
#descuento = precio * (porcentaje / 100)
#precio_final = precio - descuento
#retornar precio_final

#fin función

#Pseudocódigo de es_par:
#función es_par(numero) 
#retornar numero % 2 == 0

#fin función
# 8. Explícale una de las dos a tu compañera(o) de al lado e incluye el propósito del programa. Tu compañera(o) te debe explicar lo siguiente. Lleguen a un acuerdo para agregar lo esencial como comentarios.
# Propósito: calcular_descuento calcula el precio final después de aplicar un descuento, mientras que es_par verifica si un número es par.
# 9. Cambia las funciones para que acepten decimales en el precio.
# En Python, los números decimales se representan con el tipo de dato float. Por lo tanto, los parámetros "precio" y "porcentaje" pueden ser de tipo float para aceptar decimales.


# =============================================================
# Parte 4: Alcance (Scope) y Retorno
# =============================================================

# La función mostrar_bienvenida() usa print(), mientras que calcular_descuento() usa return.
# Si asignas la llamada de la bienvenida a una variable:

resultado = mostrar_bienvenida("Julio")
print(resultado)

# PREGUNTAS:
# 10. ¿Qué valor se guarda en la variable 'resultado' y por qué?
# El valor guardado en 'resultado' es None, porque la función mostrar_bienvenida() no retorna ningún valor, solo imprime un mensaje.

# 11. ¿Por qué es necesario usar return en calcular_descuento() para poder guardar el precio final en compra_1 y compra_2?
# Porque sin el return, la función no devolvería ningún valor y no podríamos asignar el resultado a una variable.
# 12. Intenta ejecutar la siguiente línea al final del documento: print(descuento) ¿Qué error muestra Python?
# Esto intenta imprimir una variable que solo existe dentro de la función calcular_descuento().
# Esto generará un error porque 'descuento' no está definido en este ámbito.
# 13. ¿Por qué la variable 'descuento' no es accesible fuera de la función?
# Porque 'descuento' es una variable local dentro de la función calcular_descuento() y solo existe durante la ejecución de esa función.
# 14. ¿Qué ocurre si dentro de calcular_descuento cambias 'return precio_final' por 'print(precio_final)' e intentas sumar 'compra_1 + 5'?
# Ocurrirá un error porque la función ya no devuelve un valor, por lo que 'compra_1' sería None y no se puede sumar con un número.
# 15. Investiga: ¿Cómo podrías llamar a la función 'calcular_descuento' asignando el porcentaje mediante su nombre de parámetro (keyword argument)?
# Ejemplo: calcular_descuento(precio=100, porcentaje=20) o calcular_descuento(100, porcentaje=20)
# 16. Añade un "docstring" (comentario multilínea con """) dentro de cada función para explicar brevemente qué hace.
# Ejemplo de docstring para calcular_descuento:

def calcular_descuento(precio, porcentaje):
     """
     Calcula el precio final después de aplicar un descuento.
     
     Parámetros:
     precio (float): El precio original del producto.
     porcentaje (float): El porcentaje de descuento a aplicar.
     
     Retorna:
     float: El precio final después de aplicar el descuento.
     """
     descuento = precio * (porcentaje / 100)
     precio_final = precio - descuento
     return precio_final