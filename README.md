# COVID19FlaskAPI
### Data

API desarrollada en flask para manipular base de datos MySQL con los datos de los informes oficiales del COVID19 del Ministerio de Salud Argentino.

Ejemplo:
 \
 [![Open In
Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1K1ilzDK5F60_KeJ2aifrFOvBw9337T8Q)

 La API tiene 6 endpoints:
API desarrollada en flask para manipular base de datos MySQL con los
datos de los informes oficiales del COVID19 del Ministerio de Salud
Argentino. \


### Uso de la API



-   Rango entre fechas, ejemplo: http://damianra.pythonanywhere.com/api/v1/range?startdate=2020-03-10&enddate=2020-04-10
-   Fecha especifica, ejemplo: http://damianra.pythonanywhere.com/api/v1/date?date=2020-03-25
-   Todos los datos: http://damianra.pythonanywhere.com/api/v1/alldata
-   Totales del dia por provincia (Wikipedia): (Datos de Wikipedia): http://damianra.pythonanywhere.com/api/v1/provinces
-   Totales por provincia (Todo el dataset): http://damianra.pythonanywhere.com/api/v1/provdata
-   Totales por provincia especifica: http://damianra.pythonanywhere.com/api/v1/prov?province=Tierra%20del%20Fuego%20e%20Islas%20Malvinas
("http://damianra.pythonanywhere.com/api/v1/prov?province=" + "Nombre de Provincia" (con mayusculas y espacios))



Nota: El dataset de totales por provincia comienza desde el 29/03/2020 dia en que empezaron a mostrar estos datos recolectados



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
