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
    - volumenMetro: Volumen de pasajeros
    - tmed: Temperatura media mensual
    - prec: precipitación media mensual
    - tmin: Temperatura mínima media mensual
    - tmax: Temperatura máxima media mensual
    - dir: media de la dirección del viento
    - velmedia: Velocidad media del viento
    - racha: Racha máxima media mensual
    - presMax: presión máxima media mensual
    - presMin: presión mínima media mensual
    - tmedStd: desviación típica de la temperatura media mensual
    - precStd: desviación típica de la precipitación media mensual
    - tminStd: desviación típica de la temperatura mínima media mensual
    - tmaxStd: desviación típica de la temperatura máxima media mensual
    - dirStd: desviación típica de la media de la dirección del viento
    - velmediaStd: desviación típica de la velocidad media del viento
    - rachaStd: desviación típica de la media de rachas máximas medias mensuales
    - presMaxStd: desviación típica de la presión máxima media mensual
    - presMinStd: desviación típica de la presión mínima media mensual
    - volumenMetroMean6: media móvil 6 periodos del volumen de pasajeros
    - volumenMetroMean12: media móvil 12 periodos del volumen de pasajeros
    - volumenMetroDesv6: desviación típica móvil 6 periodos del volumen de pasajeros
    - volumenMetroDesv12: desviación típica móvil 12 periodos del volumen de pasajeros
    - volumenMetroMedi6: mediana móvil 6 periodos del volumen de pasajeros
    - volumenMetroMedi12: mediana móvil 12 periodos del volumen de pasajeros
    - volumenMetroDiff6: serie diferenciada a 6 periodos del volumen de pasajeros
    - volumenMetroDiff12: serie diferenciada a 12 periodos del volumen de pasajeros

Además tendremos las predicciones:
    
    PREDICCIONES:
    - F1: fecha
    - F2: predicciones