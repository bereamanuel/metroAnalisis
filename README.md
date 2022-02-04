# MetroAnalisis

El objetivo del estudio es estimar el volumen de pasajeros en los próximo días del Metro de Madrid, teniendo en cuenta datos metereológicos y calendario de la Comunida de Madrid (CAM), los datos de volumen de pasajeros no son reales, han sido estraidos de un conjunto de datos de la web UCI de volumen de tráfico en el metro de Minneapolis


DATOS:
    - Calendario [Datos Abiertos CAM](https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=9f710c96da3f9510VgnVCM2000001f4a900aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default)
    - Climatología [AEMET datos abiertos](https://opendata.aemet.es)
    - Metro volumen pasajeros  [Municipio Madrid banco datos](http://www-2.munimadrid.es/CSE6/control/seleccionDatos?numSerie=15050100012)


    CALENDARIO:
        - Día: Fecha en formato dd/MM/yyyy
        - Día de la semana: Lunes, Martes, Miércoles, Jueves, Sábado, Domingo
        - laborable/festivo/fin de semana: variable que toma 4 valores, Laborable, Festivo, Sábado, Domingo
        - tipo de festividad: Nacional/Local
        - Festividad: Nombre de la fiesta

    CLIMATOLOGÍA:
        Información en el archivo climatologia.json

    DATOS METRO original:
        - fecha
        - volumen pasajeros

Vamos a realizar un dataframe especial para este estudio, donde agruparemos el volumen de tráfico por día y uniremos por fecha con el calendario y la climatología (tambien agrupada por dia, tomando la media de las 3 estaciones de la ciudad de Madrid)

El conjunto final tomará el aspecto:
    
    DATOSFINAL:
    - dia
    - diaSemana
    - laborable
    - tipoFestividad
    - nombreFestividad
    - datosClimatología (todos agrupados y tomando la media de las 3 estaciones de la ciudad de madrid)
    - trafficVolume

Hemos creado una BD por si quisiesemos ir insertando datos.
