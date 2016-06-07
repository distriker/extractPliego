# extractPliego | Extractor de datos de Pliego
Script que permite extraer las imágenes y textos del sitio web de Numismática Pliego | Desarrollado para una tarea de Wikimedia España

### Cómo funciona.
El script funciona a partir de un archivo, **extraer.py**, y dos carpetas, "datos" e "img". La URL de la que extrae todos los datos es `subastas.numismaticaycoleccionismo.es/index/viewBatch/[NÚMERO DE FICHA]`, qué es donde guardan las imágenes. El número de ficha se consigue a partir de rangos concretos (00001 al 00010, 00010 al 00099, 00100 al 00999, 01000 al 09999 y 10000 al 18510) que determinan la ficha que hay que abrir y extraer.

Crea un archivo csv en la carpeta "datos", donde guarda todos los textos que extrae de cada ficha buscando elementos con la clase "description", que en este caso es un div que contiene el número y la descripción del lote; al mismo tiempo extrae las imágenes con la clase "list_logo" (1 o 2 de media) de las fichas.

### Uso:
Su uso es muy sencillo pero hay que tener algunas cosas en cuenta. Para iniciarlo se utiliza el comando `python extraer.py` en la misma carpeta del script:
1. Te pide que introduzcas el nombre para el archivo que se va a crear y en el que se guardarán los textos. No pongas ninguna extensión.
2. Te dice donde se guardará (`/datos/[NOMBRE ASIGNADO].csv`), y te pide que confirmes pulsando `s` o `n`.
3. Luego te pide elegir entre los rangos que te muestra.
4. A partir de aquí ya no necesita más intervención humana, extraerá de todas las fichas los textos y las imágenes.

### Tareas pendientes:
- **Perfeccionar los rangos**. Ahora mismo estoy comprobando que se extraen correctamente los datos y que todas las fichas tienen contenido y no están vacías. En algunos casos hay fichas vacías y por lo tanto, no extrae imágenes pero si el texto del div, porque existe; por lo tanto, es necesario comprobar hasta que ficha hay datos, para no obtener datos inútiles.
- **Unificar el proceso**. Evitar tener que señalar que rango usar y unificarlo en uno mismo que extraiga todo de una vez. He trabajado un poco en esta cuestión y no es complicado, pero antes de continuar con ello hay que resolver el problema de las fichas vacías.
- **Limpiar el texto obtenido**. Eliminar las etiquetas html con las que se extrae el texto, además de grandes espacios innecesarios.
- **Automatizar la subida**. Para que el script no se quede simplemente en un extractor, en el caso de que fuese seguro y se pudiese realizar sin perjuicio alguno, se podría automatizar la subida (supervisada quizás) a Commons.

### Fuentes.
Determinados sitios de los que se ha extraído código o han influenciado.
considerablemente en él.
- [Extraer datos estructurados de una página web con Python y BeautifullSoup](http://bit.ly/1ZpK4Ek) | protoinformatico.com
- [dumpimages.py](http://bit.ly/1VGtBg7) | Stackoverflow.
- [Intro to Beautiful Soup](http://bit.ly/25G3AA7) | Programming Historian.
- Por supuesto, mucha documentación oficial de los paquetes y funciones utilizadas.
