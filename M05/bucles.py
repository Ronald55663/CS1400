# Ronald Medina
# M05 - Bucles

# Sección 1: ¿Por qué usar un Bucle?

# Código 1:
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")
print("Hola, estudiante")


# 1. Si quisieras saludar a 100 estudiantes, ¿qué problema
#    presenta el enfoque mostrado en el Código 1?
#
# Respuesta: Tendríamos que escribir la misma instrucción muchas
# veces. Esto haría que el código fuera largo, repetitivo y difícil
# de modificar o mantener.


# 2. ¿Crees que este enfoque manual permite adaptar el número
#    de saludos dinámicamente si el usuario lo solicita?
# No. El código manual tiene un número fijo de
# instrucciones print(). Para hacerlo dinámico sería necesario
# utilizar un bucle que repita el código según el número indicado
# por el usuario.

# Sección 2: Bucle while

# Código 2:
respuesta = input("¿Deseas repetir el proceso? (si/no): ")

if respuesta == "si":
    print("Ejecutando el bloque...")
    respuesta = input("¿Deseas repetir el proceso? (si/no): ")

print("Programa finalizado.")


# 3. Si se introduce "si" en la primera pregunta y "si" en la
#    segunda, ¿el programa preguntó una tercera vez?
#  No. El programa finalizó después de la segunda
# pregunta porque un if solamente ejecuta su bloque una vez
# cuando la condición es verdadera. No repite automáticamente
# el bloque.

# Modificación 1A: Cambio a while


# Si cambiamos if por while, el código sería:
#
respuesta = input("¿Deseas repetir el proceso? (si/no): ")

while respuesta == "si":
    print("Ejecutando el bloque...") 
    respuesta = input("¿Deseas repetir el proceso? (si/no): ")

print("Programa finalizado.")


# 4. ¿Cómo cambia el comportamiento respecto al if?
# El while puede repetir el bloque varias veces
# mientras la condición sea verdadera. Por eso, si el usuario
# escribe "si" varias veces, el programa seguirá preguntando
# y ejecutando el bloque hasta que escriba algo diferente de "si".


# 5. ¿Es posible saber con exactitud de antemano cuántas veces
#    el usuario escribirá "si"?
# No. El número de repeticiones depende de las
# respuestas que introduzca el usuario durante la ejecución.

# Modificación 1B: Bucle infinito

# Si se comenta la línea que actualiza la respuesta:
 
respuesta = input("¿Deseas repetir el proceso? (si/no): ")

while respuesta == "si":
 print("Ejecutando el bloque...")
 respuesta = input("¿Deseas repetir el proceso? (si/no): ")

 print("Programa finalizado.")


# 6. ¿Qué sucede cuando no se actualiza la variable de control?
#
# Respuesta: Si la variable respuesta permanece con el valor "si",
# la condición del while siempre será verdadera y el programa
# entrará en un bucle infinito.


# 7. ¿Qué combinación de teclas se utiliza para detener un
#    bucle infinito en la terminal?
#
# Respuesta: Ctrl + C

# Sección 3: Bucle for y range()


num = int(input("Introduce un número límite: "))

for i in range(10):
    print("Iteración:", i)


# 8. Si se introduce 10, ¿cuántas veces se imprimió
#    "Iteración"? ¿Influyó el número ingresado?
# Se imprimió 10 veces. El número ingresado por el
# usuario no influyó en este primer intento porque el programa
# utiliza range(10) y no utiliza la variable num en el bucle.


# 9. ¿Cuál es el valor inicial y cuál es el valor final impreso?
#
# Valor inicial: 0
# Valor final: 9


# 10. ¿Se llegó a imprimir el número 10?
#
# Respuesta: No. Python excluye el límite superior de range().
# Por eso range(10) genera los valores desde 0 hasta 9.


# 11. Cambiar range(10) por range(0, 10), ¿produce alguna diferencia?
#
# Respuesta: No. Ambos producen exactamente los mismos valores:
# 0, 1, 2, 3, 4, 5, 6, 7, 8 y 9.

# Modificación 2A: Rango con Variable Límite

# El rango modificado es:

for i in range(1, num):
   print("Iteración:", i)


# 12. Si se ingresa 20, ¿el conteo se detuvo en 20 o en 19?
#
# Respuesta: Se detuvo en 19 porque el límite superior de range()
# no se incluye.


# 13. ¿Qué ajuste matemático permite incluir exactamente el número
#     ingresado por el usuario?
#
# Respuesta: Se debe sumar 1 al límite.
#
range(1, num + 1)


# Modificación 2B: Uso del argumento Step / Paso

# La línea modificada sería:
#
for i in range(2, 11, 2):
  print("Iteración:", i)


# 14. ¿Qué valores se imprimieron y qué función cumple el tercer
#     argumento?
#
# Respuesta: Se imprimieron 2, 4, 6, 8 y 10.
# El tercer argumento es el paso (step) y determina cuánto
# aumenta o disminuye el valor en cada iteración.

# Sección 4: Iteración sobre Secuencias


palabra = "Python"

print("--- Letras de la palabra ---")
for letra in palabra:
    print(letra)

frutas = ["manzana", "banana", "cereza"]

print("--- Lista de frutas ---")
for fruta in frutas:
    print(fruta)


# 15. ¿Qué representa la variable letra en cada paso?
#
# La variable letra representa cada carácter individual
# de la cadena "Python", uno por uno, en cada iteración del bucle.


# 16. ¿Cuál opción resulta más legible para un principiante?
#
# La iteración directa "for fruta in frutas:" resulta
# más legible para un principiante porque permite trabajar
# directamente con cada elemento de la lista sin tener que
# manejar índices manualmente.

# Sección 5: Sentencias de Control de Bucles

print("Demostración de continue:")

for num in range(1, 6):
    if num == 3:
        continue
    print("Número:", num)


print("\nDemostración de break:")

for num in range(1, 6):
    if num == 3:
        break
    print("Número:", num)


# 17. ¿Qué número falta en la demostración de continue?
#
# Falta el número 3 porque continue hace que Python
# salte el resto de la iteración actual y continúe con la siguiente.


# 18. ¿Qué números se imprimieron en la demostración de break?
#
# Se imprimieron 1 y 2.
# Cuando num llega a 3, break termina completamente el bucle.


# 19. Si tenemos while True para solicitar una clave, ¿qué
#     sentencia permite salir cuando la clave es correcta?
#
# break

# Sección 6: Patrones de Acumulación y Conteo

numeros = [4, 7, 2, 9, 10, 5]
suma_total = 0
mayores_a_cinco = 0

for num in numeros:
    suma_total += num

    if num > 5:
        mayores_a_cinco += 1

print("Suma total:", suma_total)
print("Cantidad de números mayores a 5:", mayores_a_cinco)


# 20. ¿Con qué valor deben inicializarse las variables?
#
# Ambas deben inicializarse en 0:
#
# suma_total = 0
# mayores_a_cinco = 0
#
# Si se inicializaran dentro del bucle, sus valores se reiniciarían
# en cada iteración y no se acumularían correctamente los resultados.


# 21. Diferencia entre acumulador y contador:
#
# Respuesta: Un acumulador suma o acumula diferentes valores.
# En este caso, suma_total += num va agregando cada número a la suma.
#
# Un contador cuenta cuántas veces ocurre una condición.
# En este caso, mayores_a_cinco += 1 aumenta en uno cada vez que
# encuentra un número mayor que 5.

# Sección 7: Normalización de Textos con .lower()


sujeto1 = "Python"
sujeto2 = "python"

if sujeto1 == sujeto2:
    print("Iguales")
else:
    print("Diferentes")


# 22. ¿Cuál es la diferencia visual y cuál es el resultado?
#
# "Python" comienza con una P mayúscula, mientras que
# "python" comienza con una p minúscula.
# La comparación inicial da como resultado "Diferentes" porque
# Python distingue entre mayúsculas y minúsculas.


# 23. Modifica la condición usando .lower().
#
# La condición sería:
#
if sujeto1.lower() == sujeto2.lower():
 print("Iguales")
else:
   print("Diferentes")
#
# Resultado: Iguales
#
# .lower() convierte todos los caracteres de una cadena a
# minúsculas, permitiendo comparar los textos sin importar
# las diferencias entre mayúsculas y minúsculas.


# 24. ¿Por qué es útil aplicar .lower() a las respuestas del usuario?
#
# Respuesta: Porque permite aceptar diferentes formas de escribir
# una misma respuesta. Por ejemplo, "SI", "Si", "sI" y "si"
# se convierten todas en "si". Esto facilita la validación de
# respuestas dentro de un bucle while.