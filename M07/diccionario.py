# Ejemplo de conteo de palabras
text = "sana sana curita de rana sana sana pomada de sapo sana sana hoy y manana manana y hoy"

lst = text.split()
plbList = dict()

for x in lst:
    if x not in plbList:
        plbList[x] = 1
    else:
        plbList[x] += 1

for i in plbList:
    print (i, plbList[i])

# Ejemplo de conteo de calificaciones
notas = "A A A B B A C A B C C E A B A C C C A B B B A B A A A C D A B B C C A A A B A B A C A B B A"
listaNotas = notas.split()
notasDiccionario = dict()

for i in listaNotas:
  if i not in notasDiccionario:
    notasDiccionario[i] = 1
  else:
    notasDiccionario[i] += 1

for i in notasDiccionario:
  print(i, notasDiccionario[i])