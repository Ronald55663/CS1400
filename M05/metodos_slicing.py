# Ronald Medina 

# Guía de Trabajo 2: Métodos, Slicing y Matemáticas en Python


# Sección 1: Conteo Inverso con range()


# Código 1.1:
num = int(input("Introduce el número inicial: "))

for i in range(num, 0, -1):
    print("Conteo:", i)


# Análisis:

# 1. Ejecuta el programa e introduce 10.
# Inicio: 10 | Fin: 1

# 2. ¿Por qué es necesario que el parámetro step sea negativo
#    al realizar un conteo descendente?
# Respuesta: Porque queremos que el contador disminuya en cada
# iteración. Un paso negativo hace que range() vaya hacia atrás.

# 3. ¿Por qué el valor final se configuró en 0 si queríamos
#    que el conteo se detuviera en el número 1?
# Respuesta: Porque el valor final de range() no se incluye.
# Por eso range(num, 0, -1) llega hasta 1, pero no imprime el 0.

# 4. Modifica el código para que cuente hacia atrás de 2 en 2,
#    comenzando desde el número elegido y deteniéndose exactamente
#    en 0 (inclusive).
#
# Respuesta:
# range(num, -1, -2)
#
# Nota: usar -1 como límite permite incluir el 0 cuando corresponde.
# Por ejemplo, si num = 10: 10, 8, 6, 4, 2, 0.

# Sección 2: Funciones Matemáticas de Python (math)


import math

decNum = -34.5678
intNum = 9

print(round(decNum, 2))       # Línea A
print(round(decNum, 0))       # Línea B
print(int(decNum))            # Línea C
print(abs(decNum))            # Línea D

print(math.pow(intNum, 2))    # Línea E
print(math.sqrt(intNum))      # Línea F


# 5. ¿Resultado de la Línea A round(decNum, 2)?
# Respuesta: -34.57

# 6. ¿Resultado de la Línea B round(decNum, 0)?
# Respuesta: -35.0

# 7. ¿Resultado de la Línea C int(decNum)?
# Respuesta: -34
# int() trunca la parte decimal en lugar de redondear.

# 8. ¿Resultado de la Línea D abs(decNum)?
# Respuesta: 34.5678
# abs() devuelve el valor absoluto, eliminando el signo negativo.

# 9. ¿Resultado de la Línea E math.pow(intNum, 2)?
# Respuesta: 81.0
# math.pow() devuelve el resultado como un número de tipo float.

# 10. ¿Resultado de la Línea F math.sqrt(intNum)?
# Respuesta: 3.0
# La raíz cuadrada de 9 es 3.

# Sección 3: Comparación de Textos mediante ASCII / Unicode


miMax = max("Banano", "manzana", "Zanahoria")
print("El máximo es:", miMax)


# 11. Antes de ejecutar: ¿Cuál crees que será el resultado
#     devuelto por max()?
# Predicción: manzana

# 12. Ejecuta el código. ¿Cuál fue el resultado real?
# Resultado: manzana

# 13. ¿Por qué "manzana" fue seleccionada como la mayor frente
#     a "Zanahoria"?
# Respuesta: Python compara las cadenas carácter por carácter
# usando sus valores Unicode. Las letras mayúsculas tienen valores
# menores que las letras minúsculas. Por eso "m" de "manzana"
# tiene un valor mayor que "Z" de "Zanahoria", haciendo que
# "manzana" sea considerada mayor.

# 14. Cambia max() a min(). ¿Qué valor obtienes ahora y por qué?
# Resultado: Banano
# Respuesta: "Banano" comienza con una letra mayúscula "B",
# y las letras mayúsculas tienen valores Unicode menores que
# las minúsculas. Además, "B" tiene un valor menor que "Z".
# Por eso "Banano" es el menor de los tres.

# Sección 4: Aplicación Práctica – Física y Matemáticas


import math

d = int(input("Ingresa la longitud de la huella de frenado (en metros): "))

# 15. Completa la asignación v usando math.sqrt() y la fórmula.
# Respuesta:
v = math.sqrt(20 * d)

print("Velocidad estimada del auto:", round(v, 2), "km/h")

# Sección 5: Segmentación de Cadenas (Slicing)

nombre = "Building Puentes"

print("Índice 0:", nombre[0])
print("Segmento:", nombre[8:15])


# 16. ¿Qué carácter imprime exactamente nombre[0]?
# Respuesta: B

# 17. ¿En qué posición (índice) exacta se encuentra el espacio
#     en blanco entre ambas palabras?
# Respuesta: 8

# 18. Modifica los índices para extraer exactamente "Puentes".
#
# Opción con 2 valores:
# nombre[9:16]
#
# Opción con límite implícito:
# nombre[9:]

# Sección 6: Filtrado e Inspección de Caracteres

texto = input("Ingresa una frase con letras y números: ")
contador_numeros = 0

for caracter in texto:
    if caracter >= "0" and caracter <= "9":
        contador_numeros += 1

print("Total de dígitos numéricos encontrados:", contador_numeros)


# 19. Ejecuta el programa e ingresa:
#     "3 tigres en 2 árboles"
#
# Respuesta: 2
# Hay dos dígitos numéricos: 3 y 2.

# 20. Explica cómo evalúa Python si un carácter individual
#     es un dígito numérico usando >= y <=.
#
# Respuesta: Python compara el carácter con "0" y "9".
# Si el carácter es mayor o igual que "0" y menor o igual que "9",
# significa que está dentro del rango de caracteres numéricos.
# Por eso la condición identifica los dígitos del 0 al 9.

# Sección 7: Investigación de Métodos de Cadenas

# 21. Método .rfind('a'):
#
# Respuesta: .rfind('a') busca la última aparición de la letra
# "a" dentro de una cadena y devuelve el índice donde se encuentra.
# Si no encuentra la letra, devuelve -1.


# 22. Método .isalpha():
#
# Respuesta: .isalpha() comprueba si todos los caracteres de una
# cadena son letras. Devuelve True si todos son letras y hay al
# menos un carácter; de lo contrario, devuelve False.


# 23. Método .isdigit():
#
# Respuesta: .isdigit() comprueba si todos los caracteres de una
# cadena son dígitos. Devuelve True si todos son dígitos y hay al
# menos un carácter; de lo contrario, devuelve False.