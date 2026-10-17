playerNames = ["Adam", "Bethanie", "Carrie", "Doug", "Eddie"]
playerNumbers = [5, 2, 6, 13, 0]

# 1. Eliminar a Adam de la lista.
playerNames.remove("Adam")

# 2. Eliminar el primer número de la lista.
playerNumbers.pop(0)

# 3. Agregar a Lucas y su número.
name = "Lucas"
num = 7

playerNames.append(name)
playerNumbers.append(num)

# 4. Agregar a Raven y su número al principio.
playerNames.insert(0, "Raven")
playerNumbers.insert(0, 1)

# Imprimir las listas finales.
print(playerNames)
print(playerNumbers)

def Even_Numbers(lista_origen):
    even = []

    for num in lista_origen:
        if num % 2 == 0:
            even.append(num)

    return even


def Ten_Or_Less(lista_origen):
    numbers = []

    for num in lista_origen:
        if num <= 10:
            numbers.append(num)

    return numbers


def Calcular_Diferencias(lista_origen):
    diferencias = []

    for i in range(len(lista_origen) - 1):
        diferencia = abs(lista_origen[i] - lista_origen[i + 1])
        diferencias.append(diferencia)

    return diferencias