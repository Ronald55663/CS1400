¿Qué hace el bloque try/except ValueError? ¿Qué pasaría si el usuario escribe “veinte” y quitamos ese bloque?
El bloque try/except ValueError permite manejar errores cuando el usuario introduce un dato que no se puede convertir a numero entero

Diccionarios y funciones (los refranes)
4. ¿Por qué guardamos los refranes en un diccionario y no en una lista? ¿Qué ventaja tiene que el refrán sea la clave y el significado el valor?
Utilizamos un diccionario porque permite relacionar cada refrán con su significado

5. ¿Para qué sirven las funciones decir_refran() y decir_refran_especifico()? ¿En qué se diferencian?
La funcion decir_refran() muestra un refran elegido al azar junto con su significado. En cambio decir_refran_especifico() muestra un refran que nosotros seleccionamos. La diferencia es que una elige aleatoriamente y la otra muestra uno especifico

6. Si quisieras agregar un refrán de tu propia abuela, ¿qué línea tendrías que modificar? ¿Hay que cambiar algo más? 
ndría que agregar una nueva pareja de clave y valor dentro del diccionario REFRANES, colocando el refrán y su significado. No es necesario cambiar nada más porque la función refran_al_azar() incluirá automáticamente el nuevo refrán.

Decisiones (if / elif / else)
7. En el programa, ¿qué refrán recibe una persona de 18 años? ¿Y una de 17? Explica por qué.
Una persona de 18 años recibe el refrán "Uno pone y Dios dispone", porque cumple la condición edad >= 18. Una persona de 17 años recibe "Haz el bien y no mires a quien", porque no cumple las condiciones anteriores y entra en el bloque else.

8. ¿Qué pasaría si cambiáramos el orden y pusiéramos primero if edad >= 18 y después elif edad >= 60? ¿Alguien recibiría alguna vez el refrán de “Agua que no has de beber”?
Nadie recibiría ese refrán porque una persona de 60 años o más también cumple la condición edad >= 18. Por eso, Python ejecutaría primero ese bloque y nunca llegaría a evaluar edad >= 60.

API y JSON (Parte 2)
9. ¿Qué convierte json.loads() y en qué se transforma? ¿Y json.dumps(), qué hace en dirección contraria?
La función json.loads() convierte un texto en formato JSON en un objeto de Python, como un diccionario o una lista. En cambio, json.dumps() convierte un objeto de Python en un texto con formato JSON.

10. Para obtener la ciudad del usuario, escribimos datos['address']['city']. ¿Por qué necesitamos dos pares de corchetes?

Porque estamos accediendo a un diccionario dentro de otro diccionario. Primero utilizamos datos['address'] para entrar a la dirección del usuario y después ['city'] para obtener el nombre de la ciudad.

11. Hay tres tipos de error en esa parte (HTTPError, URLError y JSONDecodeError). ¿Cuál ocurriría si no tienes internet? ¿Y si el servidor responde con una página rota?
Si no tenemos internet, normalmente ocurre un URLError porque el programa no puede conectarse al servidor. Si el servidor responde con una página que no contiene JSON válido, puede ocurrir un JSONDecodeError. Si responde con un código HTTP de error, como 404 o 500, ocurre un HTTPError

12. ¿Por qué es buena idea usar timeout=10 al hacer la petición?
Porque establece un límite de 10 segundos para esperar la respuesta del servidor. Esto evita que el programa se quede esperando demasiado tiempo si la conexión es lenta o el servidor no responde.

Juego y reflexión general (Parte 3)
13. En el juego “Completa el refrán”, ¿cómo divide el programa el refrán en dos mitades? ¿Qué hacen split(), join() y //?
El programa utiliza split() para separar el refrán en palabras y convertirlo en una lista. Después utiliza // para calcular la mitad de la cantidad de palabras mediante una división entera. Finalmente, utiliza join() para unir las palabras y formar las dos partes del refrán.

14. ¿Para qué sirve el bloque if __name__ == "__main__": al final del archivo?
Sirve para ejecutar la función main() solamente cuando abrimos y ejecutamos ese archivo directamente. Si el archivo se importa desde otro programa, la función principal no se ejecuta automáticamente.

15. Pregunta abierta: si tuvieras que agregar una cuarta parte al programa, ¿qué agregarías y qué conceptos nuevos necesitarías usar?
Agregaría una cuarta parte donde el usuario pueda escribir sus propios refranes y guardarlos para utilizarlos después. Para hacerlo necesitaría utilizar archivos JSON, diccionarios y funciones para guardar y leer la información. Así, los refranes no se perderían cuando se cierre el programa.