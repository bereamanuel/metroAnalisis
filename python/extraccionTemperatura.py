import requests
import pandas as pd

key = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJtYmFiZXJlYXJlbGxhbm9AZ21haWwuY29tIiwianRpIjoiMzY5ZDNlOTktMzEwOS00Y2UyLWE2NjEtMmI1OThmOTdjMjE1IiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE2NDM4MzM0MDEsInVzZXJJZCI6IjM2OWQzZTk5LTMxMDktNGNlMi1hNjYxLTJiNTk4Zjk3YzIxNSIsInJvbGUiOiIifQ.9LQH5oE7YpuNQck7UBkNwfATvYa6C8ySB-I2-1RZBuo'
estaciones = ['3195','3194U','3195']  #Retiro , CIU , Cuatro Vientos


columns = ['fecha', 'indicativo', 'nombre', 'provincia', 'altitud', 'tmed', 'prec',
       'tmin', 'horatmin', 'tmax', 'horatmax', 'dir', 'velmedia', 'racha',
       'horaracha', 'presMax', 'horaPresMax', 'presMin', 'horaPresMin']
       
temperaturaMadrid = pd.DataFrame(columns= columns)


for i in [2,3,4,5,6,7,8]:
    for estacion in estaciones:
        f_inicio = f'201{i}-01-01T00:00:00UTC'
        f_fin = f'201{i}-12-31T23:59:59UTC'
        url = f'https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/{f_inicio}/fechafin/{f_fin}/estacion/{estacion}/?api_key={key}'
        path= f'./data/tiempoMadrid201{i}.csv'
        r = requests.get(url)
        rs = requests.get(r.json()['datos'])
        aux = pd.DataFrame(rs.json())
        temperaturaMadrid = temperaturaMadrid.append(aux)


temperaturaMadrid.sort_values(by = 'fecha').to_csv('../data/temperaturaMadrid20122018.csv')