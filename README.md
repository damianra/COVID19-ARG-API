# COVID19-ARG-API
### Data

API desarrollada en flask para manipular base de datos MySQL con los datos de los informes oficiales del COVID19 del Ministerio de Salud Argentino.

Ejemplo:
 \
Casos Argentina
 [![Open In
Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1K1ilzDK5F60_KeJ2aifrFOvBw9337T8Q)

Casos por provincias:
 [![Open In
Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1R8ahRAUTpn9kQKantkySWZErrkteOkVx?usp=sharing)

### Uso de la API
<br>

 La API tiene 6 endpoints:


-   Rango entre fechas, ejemplo: http://damianra.pythonanywhere.com/api/v1/range?startdate=2020-03-10&enddate=2020-04-10
-   Fecha especifica, ejemplo: http://damianra.pythonanywhere.com/api/v1/date?date=2020-03-25
-   Todos los datos: http://damianra.pythonanywhere.com/api/v1/alldata
-   Totales del dia por provincia (Wikipedia): (Datos de Wikipedia): http://damianra.pythonanywhere.com/api/v1/wikidata
-   Totales por provincia (Todo el dataset): http://damianra.pythonanywhere.com/api/v1/provincesdata 
-   Totales por provincia especifica: http://damianra.pythonanywhere.com/api/v1/province?prov=Tierra%20del%20Fuego%20e%20Islas%20Malvinas 
("http://damianra.pythonanywhere.com/api/v1/province?prov=" + "Nombre de Provincia" (con mayusculas y espacios)) 

Nota1: El dataset de totales por provincia comienza desde el 29/03/2020 dia en que empezaron a mostrar estos datos recolectados.<br>
Nota2: Con respecto al dataset, decidimos utilizar el seguimiento que comparte <a href="https://twitter.com/jorgeluisaliaga">Jorge Aliaga</a>, es mas completo de lo que veníamos recolectando y tiene mucha información. <a href="https://docs.google.com/spreadsheets/d/1M7uDgWSfy6z1MNbC9FP6jTNgvY7XchJ0m-BfW88SKtQ/edit?usp=sharing">link</a>
<br><br>
Todos los datos de la API: <a href="http://damianra.pythonanywhere.com/dataset">Dataset</a>
<br><br>
Seguiremos trabajando para poder mantenerla actualizada. Los informes oficiales en PDF se pueden descargar de:
https://www.argentina.gob.ar/coronavirus/informe-diario
Tambien se usaron datasets ofrecidos por otras personas que tambien se tomaron el trabajo de hacer un seguimiento.

### Fuente

\
 Los informes oficiales en PDF se pueden descargar de:
[https://www.argentina.gob.ar/coronavirus/informe-diario](https://www.argentina.gob.ar/coronavirus/informe-diario)
\
 Tambien se usaron datasets ofrecidos por otras personas que tambien se
tomaron el trabajo de hacer un seguimiento. \


### Desarrolladores

\
 Juan Colombo:
[Linkdin](https://www.linkedin.com/in/juan-carlos-colombo-336642152/) \
 Damian Ramirez:
[Linkdin](https://www.linkedin.com/in/damian-ramirez-677488172)
