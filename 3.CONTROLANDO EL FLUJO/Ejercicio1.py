#CONTROLANDO EL FLUJO

#Ejercicio 1
#Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

Mostrar una suma de los dos números

Mostrar una resta de los dos números (el primero menos el segundo)

Mostrar una multiplicación de los dos números

En caso de introducir una opción inválida, el programa informará de que no es correcta.


#Ejercicio 2
#Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente.


#Ejercicio 3
#Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100.

Puedes utilizar la funciones sum() y range() para hacerlo más fácil.
El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números, pruébalo.


#Ejercicio 4
#Realiza un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética.


#Ejercicio 5
#Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:

La sintaxis [valor] in [lista] permite comprobar si un valor se encuentra en una lista (devuelve True o False).


#Ejercicio 6
#Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

Todos los números del 0 al 10 [0, 1, 2, ..., 10]

Todos los números del -10 al 0 [-10, -9, -8, ..., 0]

Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]

Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]

Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

Se pueden generar saltos en el range() estableciendo su tercer parámetro range(inicio, fin, salto), experimenta.


#Ejercicio 7
#Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']

lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']



#COLECCIONES DE DATOS

#Ejercicio 1
#Realiza un programa que siga las siguientes instrucciones:

Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos

Crea un conjunto llamado administradores con los administradores Juan y Marta.

Borra al administrador Juan del conjunto de administradores.

Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.

Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no.

Los conjuntos se pueden recorrer dinámicamente utilizando el bucle for de forma similar a una lista.
También cuentan con un método llamado .discard(elemento) que sirve para borrar o descartar un elemento.


#Ejercicio 2
#Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada clase de personaje jugable. Partiendo que la estadística base es 2, debes cumplir las siguientes condiciones:

El caballero tiene el doble de vida y defensa que un guerrero.

El guerrero tiene el doble de ataque y alcance que un caballero.

El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance.

Muestra como quedan las propiedades de los tres personajes.


#Ejercicio 3
#Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).

¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?

Para ordenar automáticamente una lista es posible utilizar el método .sort(), deberias probarlo.



#ENTRADA Y SALIDA DE DATOS

#Ejercicio 1
#Formatea los siguientes valores para mostrar el resultado indicado:

"Hola Mundo" → Alineado a la derecha en 20 caracteres

"Hola Mundo" → Truncamiento en el cuarto carácter (índice 3)

"Hola Mundo" → Alineamiento al centro en 20 caracteres con truncamiento en el segundo carácter (índice 1)

150 → Formateo a 5 números enteros rellenados con ceros

7887 → Formateo a 7 números enteros rellenados con espacios

20.02 → Formateo a 3 números enteros y 3 números decimales


#Ejercicio 2
#Crea un script llamado tabla.py que realice las siguientes tareas:

Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.

El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.

En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.

El script contendrá un bucle for que itere el número de veces del primer argumento.

Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.

Dentro del segundo for ejecuta una instrucción print(" * ", end=''), (**end=''* evita el salto de línea)*.

Ejecuta el código y observa el resultado.

Intenta deducir dónde y cómo añadir otra instruccion print() para dibujar una tabla.

Recordatorio: Los argumentos se envían como cadenas separadas por espacios, si quieres enviar varias palabras como un argumento deberás indicarlas entre comillas dobles "esto es un argumento". Para capturar los argumentos debes utilizar el módulo sys y su lista argv:

import sys

print(sys.argv) # argumentos enviados


#Ejercicio 3
#Crea un script llamado descomposicion.py que realice las siguientes tareas:

Debe tomar 1 argumento que será un número entero positivo.

En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.

El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número 3647:

python descomposicion.py 3647

El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo:

0007

0040

0600

3000

Pista

Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas, números y viceversa

#PROGRAMACIÓN DE FUMCIONES

#Ejercicio 1
#Realiza una función llamada area_rectangulo(base, altura) que devuelva el área del rectangulo a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura:

Recordatorio

El área de un rectángulo se obtiene al multiplicar la base por la altura.

Ejercicio 2

Realiza una función llamada area_circulo(radio) que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio:

Recordatorio

El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi. Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math:

import math


print(math.pi)

3.141592653589793

Ejercicio 3

Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo siguiente:

Si el primer número es mayor que el segundo, debe devolver 1.

Si el primer número es menor que el segundo, debe devolver -1.

Si ambos números son iguales, debe devolver un 0.

Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'.

Ejercicio 4

Realiza una función llamada intermedio(a, b) que a partir de dos números, devuelva su punto intermedio. Cuando lo tengas comprueba el punto intermedio entre -12 y 24:

Recordatorio

El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2

Ejercicio 5

Realiza una función llamada recortar(numero, minimo, maximo) que reciba tres parámetros. El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:

Devolver el límite inferior si el número es menor que éste

Devolver el límite superior si el número es mayor que éste.

Devolver el número sin cambios si no se supera ningún límite.

Comprueba el resultado de recortar 15 entre los límites 0 y 10.

Ejercicio 6

Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.

Por ejemplo:

pares, impares = separar([6,5,2,1,7])

print(pares)

print(impares)

[2, 6]

[1, 5, 7]

Sugerencia

Para ordenar una lista automáticamente puedes utilizar el método .sort().

Ejercicios « Errores y excepciones
Ejercicio 1
Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

resultado = 10/0

Ejercicio 2
Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

lista = [1, 2, 3, 4, 5]

lista[10]

Ejercicio 3
Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 

colores['blanco']

Ejercicio 4
Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

resultado = 15 + "20"

Ejercicio 5
Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:

Error: Imposible añadir elementos duplicados => [elemento].

Cuando tengas la función intenta añadir los siguiente valores a la lista 10, -2, "Hola" y luego muestra su contenido.

Sugerencia

Puedes utilizar la sintaxis "elemento in lista"

elementos = [1, 5, -2]