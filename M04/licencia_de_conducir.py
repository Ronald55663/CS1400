
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