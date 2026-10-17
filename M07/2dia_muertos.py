#Ronald Medina
# Tarea 2: El Registro de los Ancestros (Diccionarios y Conjuntos)

# Tarea 2: Registro de visitas y ofrendas asignadas

# Diccionario con el ancestro (llave) y su platillo favorito (valor)
altares_familiares = {
    "Abuela Coco": "Tamales de dulce",
    "Tío Héctor": "Mole poblano",
    "Bizabuelo Julio": "Atole de chocolate"
}

# Lista con flores traídas por los visitantes (contiene duplicados)
flores_recibidas = ["Cempasúchil", "Nube", "Cempasúchil", "Terciopelo",
 "Nube", "Cempasúchil"]

#4. Iteración en Diccionarios: Escribe un bucle for utilizando el método .items()
for ancestro, platillo in altares_familiares.items():
    print(f"Para {ancestro} preparamos: {platillo}")

#5. Usa los métodos .keys() y .values() por separado para mostrar en pantalla
#  únicamente los nombres de los ancestros y luego únicamente los platillos.
print("\nNombres de los ancestros:")
for ancestro in altares_familiares.keys():
    print(ancestro)

# Mostrar los platillos usando .values()
print("\nPlatillos favoritos:")
for platillo in altares_familiares.values():
    print(platillo)


#6. Uso de Sets (Conjuntos): Para evitar contar flores repetidas en el inventario,
flores_unicas = set(flores_recibidas)

print("\nFlores únicas:")
print(flores_unicas)
#7. Reflexión: ¿Cuántos elementos tenía la lista original de flores y cuántos quedaron

print("\nReflexión:")
print("La lista original tenía 6 elementos y el conjunto tiene 3 elementos únicos.")
print("Los conjuntos son ideales para limpiar datos porque eliminan automáticamente los elementos duplicados.")

