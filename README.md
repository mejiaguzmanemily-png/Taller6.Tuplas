# Taller6.Tuplas
Taller 6. Lógica de programación
Valery Velandia, David López, Emily Mejia
Descripción 
el analizador de comentarios es aplicacion de consola desarrollada en Python que permite a una 
plataforma registrar, gestionar y analizar comentarios. El programa procesa las entradas de texto 
aoplicando operaciones de normalización, búsqueda  por palabra indicada, conteo de caracteres y 
palabras y genera un resumen estructurado en tuplas inmutables, utilizando estructuras basicas, 
funciones propias y estructuras nativas.
Instrucciones
El programa mostrara un menú interactivo con 7 opciones numéricas. Ingresa el número correspondiente a la acción que deseas realizar. 
1. Escribe un comentario textual para agregar a la lista.
2. Visualiza la lista completa de todos los comentarios ingresados.
3. Busca y filtra que comentarios contienen una palabra especifica.
4. Calcula y muestra cuántas palabras componen cada comentario.
5. Cuenta las apariciones exactas de una palabra dentro de un comentario selecccionado.
6. Genera y muestra un resumen estadístico estructurado en un tupla.
7. Finaliza y cierra la ejecución del programa.
   
2.8 PREGUNTAS DE ANÁLISIS
1. Al aplicar lower () crea y devuelve una cadena de texto con las letras convertidas a
   minúsculas, sin modificar la cadena original. Al modificar directamente un carácter de la
   cadena genera un error, ya que las cadenas son inmutables.
2. El Split () está pensado para colecciones de elementos, donde la cantidad de fragmentos varía
   según el texto mutabilidad. Las tuplas son para agrupaciones de datos fijos que no deben cambiar
3. El resultado obtenido es 2.
   Primero la función. lower () convierte la cadena completa en minúsculas. Luego, la función.
   count()cuenta las apariciones no superpuestas de la subcadena dentro del texto, encontrando el
   inicio y el final de la cadena.
4. Se produce un error en tiempo de ejecución. Ya que las tuplas son estructuras inmutables, no
   permite reemplazar, agregar o eliminar directamente sus elementos.
5. Sería más conveniente utilizar una lista en situaciones donde los datos necesiten cambiar con
   el tiempo. Cuando se requiere agregar nuevos elementos mediante eliminar registro o modificar
   su contenido
Cadenas (str) permitieron capturar y manipular el texto de forma individual mediante métodos de normalización y búsqueda
Listas (list) proporcionaron flexibilidad para almacenar y gestionar la colección variable de comentarios agregados por los usuarios
Tuplas (tuple) garantizaron la seguridad e integridad de los datos en los resúmenes estadísticos, ofreciendo una estructura inmutable para agrupar métricas fijas que no
debían ser alteradas.
 
