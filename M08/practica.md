import traceback

try:
    num = int(input("Ingrese un número: "))
    print(10 / num)
except ValueError as e:
    print("⚠️ Capturamos un ValueError. Detalle técnico:")
    s = traceback.format_tb(e.__traceback__)
    print(s)

print("El programa continúa...")
