# extractPliego | Extractor de datos de Numismática Pliego
Script que permite extraer los datos e imágenes de las fichas de las subastas de monedas y billetes realizadas en el sitio web de Numismática Pliego.

Desarrollado para una tarea de [Wikimedia España](https://wikimedia.es).

**Tabla de contenido**
- [Cómo funciona.](#cmo-funciona)
- [Uso:](#uso)
	- [Problemas no resueltos a tener en cuenta](#problemas-no-resueltos-a-tener-en-cuenta)
- [Tareas pendientes:](#tareas-pendientes)
- [Fuentes.](#fuentes)

----
### Cómo funciona.
El script consta de un único archivo encargado de la extracción,  **extraer.py**, y dos carpetas, "**datos**" e "**img**", donde se almacenan los datos e imágenes extraídas de las fichas.

Los datos se extraen a partir de la URL base de las fichas:
`subastas.numismaticaycoleccionismo.es/index/viewBatch/[NÚMERO DE FICHA]`

El número de ficha se consigue a partir de rangos concretos (00001 al 00010, 00010 al 00099, 00100 al 00999, 01000 al 09999 y 10000 al 18510) que determinan de que ficha hay que extraer los datos.

Extrae una a una todas las imágenes (normalmente una o dos) con la clase `list_logo` de cada ficha. Por cada imagen que extrae introduce una fila en el CSV, donde introduce los datos de la ficha. *Véase [README de la carpeta "datos"](https://github.com/distriker/extractPliego/tree/master/datos)*.

### Uso:
1. [Descarga el script](https://github.com/distriker/extractPliego/archive/master.zip) y extráelo.
2. Abre la terminal/cmd donde hayas extraído el script e introduce: `python extraer.py`
3. Introduce el nombre para el archivo que se creará y en el que se guardarán los datos extraídos. **No pongas ninguna extensión** (se asignará automáticamente su correspondiente .csv).
4. Para estar seguro, te pide que confirmes si el nombre asignado (`/datos/[NOMBRE ASIGNADO].csv`) es correcto. Introduce `s` o `n`.
5. Luego te pide elegir entre los rangos que te muestra ([1] [2] [3] [4] [5]) o extraer todos los datos e imágenes de las fichas ([6]); **ten en cuenta que la prueba del rango 6 tardó 3 horas y 42 minutos**.
6. A partir de aquí ya no necesita más intervención humana. En el caso de que "termine" sin extraer todos los datos o emita algún error, [házmelo saber](https://github.com/distriker/extractPliego/issues).

#### Problemas no resueltos a tener en cuenta
He detectado que el script tiene problemas al extraer dos fichas concretas: [00168](http://subastas.numismaticaycoleccionismo.es/index/viewBatch/00168) y [10371](http://subastas.numismaticaycoleccionismo.es/index/viewBatch/10371). El problema deriva en que al llegar a ambas fichas el script colapsa y deja de extraer datos, teniendo que pararlo e iniciarlo de nuevo. Para que esto no suceda **ambas fichas están excluidas de la extracción**, hasta que consiga arreglarlo.

### Tareas pendientes:
- **Arreglar el problema de las fichas 00168 y 10371**. Tengo la hipótesis de que en el caso de la *10371* podría deberse a que no hay imagen que extraer. En lo que respecta a la *00168*, desconozco absolutamente la causa.
- **Comprobación**. Comprobar si las monedas descargadas están ya subidas a Commons y señalarlo en el CSV (ya subida/no subida).
- **Fusionar las imágenes**. Utilizar [PIL](http://pythonware.com/products/pil/) o [Pillow](http://python-pillow.org/) para unir en una misma imagen los anversos y reversos.
- **Pre-procesar la información**. Generar un modelo de ficha para Commons (descripción, autor, fuente...) a partir de los datos extraídos.
- **Adaptar CSV para subirlo a Commons con [CSV a Commons](https://github.com/davidabian/csv-a-commons)**. Unificar en una única línea aquellos datos extraídos para anverso y reverso.

### Fuentes.
Determinados sitios de los que se ha extraído código o han influenciado.
considerablemente en él.
- [Extraer datos estructurados de una página web con Python y BeautifullSoup](http://bit.ly/1ZpK4Ek) | protoinformatico.com
- [dumpimages.py](http://bit.ly/1VGtBg7) | Stackoverflow.
- [Intro to Beautiful Soup](http://bit.ly/25G3AA7) | Programming Historian.
- Por supuesto, mucha documentación oficial de los paquetes y funciones utilizadas.
