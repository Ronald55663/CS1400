
"""
TODO
Crea un programa interactivo que evalúe si una persona mayor de edad está en
condiciones de conducir. Usa como referencia lo visto en la M3 Tarea de Sentencias.
Requisitos:
Entrada de datos: Solicita la edad del usuario y al menos 2 o 3 condiciones
 adicionales.
Sentencias de control: Usa estructuras condicionales (if, else if, else)
 y operadores lógicos (AND, OR, NOT) para evaluar la combinación de datos.
Salida clara: Muestra un mensaje personalizado indicando si la persona puede
 conducir o si debe entregar las llaves inmediatamente.
¡Usa tu creatividad! 
 Piensa en situaciones cómicas o extremas de la vida real.
   ¿Qué imprudencia o descuido no le permitirías a tu abuela antes de subirse al auto?
     (Ejemplo: "¿Olvidó los lentes en la cocina?")
"""

# Ronald Medina
# M04 - Licencia de conducir
# Este programa determina si una persona puede conducir
# dependiendo de su edad y otras condiciones.

print("EVALUACIÓN PARA CONDUCIR")

# Pedimos la edad del usuario y la convertimos a un número entero.
edad = int(input("¿Cuántos años tienes? "))

# Preguntamos si la persona tiene sus lentes puestos.
lentes = input("¿Tienes tus lentes puestos? (si/no): ").lower()

# Preguntamos si la persona tiene puesto el cinturón.
cinturon = input("¿Tienes puesto el cinturón? (si/no): ").lower()

# Preguntamos si la persona ha tomado alcohol.
alcohol = input("¿Has tomado alcohol? (si/no): ").lower()

print("\n--- Resultado")

# Si la persona es menor de 18 años, no puede conducir.
if edad < 18:
    print("No puedes conducir porque eres menor de edad.")

# Si tomó alcohol O no tiene sus lentes, debe entregar las llaves.
elif alcohol == "si" or lentes == "no":
    print("¡ENTREGA LAS LLAVES INMEDIATAMENTE!")
    print("No estás en condiciones seguras para conducir.")

# Si no tiene puesto el cinturón, primero debe ponérselo.
elif cinturon == "no":
    print("Ponte el cinturón antes de conducir.")

# Si todas las condiciones son correctas, puede conducir.
elif edad >= 18 and lentes == "si" and cinturon == "si" and not alcohol == "si":
    print("Puedes conducir.")
    print("¡Abuela, arranca el carro, pero cuidado!")

# Si ninguna de las condiciones anteriores se cumple,
# mostramos un mensaje de seguridad.
else:
    print("Algo no está bien. Mejor no conduzcas.")

  # ANÁLISIS M04
#
# 1. ¿Cuántos commits hiciste?
# Hice ___ commits durante esta tarea.
#
# 2. ¿Qué método te pareció más fácil de usar para guardar y subir tus
# cambios a GitHub: los comandos en la terminal o la interfaz visual de
# Visual Studio Code? ¿Por qué?
# Me pareció más fácil usar la interfaz visual de Visual Studio Code
# porque puedo ver los cambios y los archivos modificados de una manera
# más sencilla antes de hacer el commit.
#
# 3. ¿Para qué sirve ejecutar el comando git status antes de empezar
# a trabajar?
# git status sirve para revisar el estado del repositorio. Me permite
# saber qué archivos fueron modificados, cuáles son nuevos y cuáles
# están pendientes de guardar en un commit.
#
# 4. ¿Por qué es fundamental descargar (git pull) los cambios más
# recientes del repositorio de la profesora?
# git pull es importante porque descarga los cambios más recientes del
# repositorio de la profesora. Esto permite trabajar con la versión
# más actualizada y ayuda a evitar conflictos al subir mis cambios.
#
# 5. ¿Cuál es la diferencia entre hacer un fork y clonar un repositorio?
# Un fork crea una copia del repositorio en mi propia cuenta de GitHub.
# Un clone descarga una copia del repositorio desde GitHub a mi
# computadora para poder trabajar con los archivos localmente.
#
# 6. ¿Por qué es buena práctica escribir mensajes claros y descriptivos
# en cada commit?
# Es una buena práctica porque los mensajes claros permiten saber qué
# cambio se realizó en cada commit. Mensajes como "cambios" o "listo"
# no explican exactamente qué se modificó.
#
# 7. ¿Qué tipos de mensajes agregaste?
# Agregué mensajes relacionados con los cambios que fui realizando
# en el código, como crear, modificar y mejorar partes de la tarea M04.
#
# 8. ¿Cuál es tu sentencia preferida?
# Mi sentencia preferida es if porque permite que el programa tome
# decisiones dependiendo de si una condición es verdadera o falsa.
#
# 9. ¿Cuándo entra el programa a la segunda sentencia de tu tarea?
# El programa entra a la segunda sentencia cuando la condición de la
# primera sentencia no se cumple y necesita comprobar la siguiente
# condición.
#
# 10. ¿Qué aprendiste del README.md en tu carpeta M04?
# Aprendí que el README.md contiene instrucciones importantes sobre
# la tarea y explica lo que debo realizar. También aprendí que los
# comentarios ayudan a explicar el código y hacen que sea más fácil
# de entender para otras personas y para mí mismo.