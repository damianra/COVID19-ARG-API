# COVID19FlaskAPI

API desarrollada en flask para manipular base de datos MySQL con los datos de los informes oficiales del COVID19 del Ministerio de Salud Argentino.

Ejemplo:
https://colab.research.google.com/drive/1K1ilzDK5F60_KeJ2aifrFOvBw9337T8Q

 La API tiene 3 endpoints:

rango entre fechas ej:
http://damianra.pythonanywhere.com/api/v1/range?startdate=2020-03-10&enddate=2020-04-10

por fecha ej:
http://damianra.pythonanywhere.com/api/v1/date?date=2020-03-25

todos los datos:
http://damianra.pythonanywhere.com/api/v1/alldata


Seguiremos trabajando para poder mantenerla actualizada. Los informes oficiales en PDF se pueden descargar de:
https://www.argentina.gob.ar/coronavirus/informe-diario
Tambien se usaron datasets ofrecidos por otras personas que tambien se tomaron el trabajo de hacer un seguimiento.
