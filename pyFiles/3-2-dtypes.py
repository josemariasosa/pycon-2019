#!/usr/bin/env python
# coding=utf-8
# author: jose maria sosa

import json
import rubik as rk
import pandas as pd

filename = 'data/conagua.json'
with open(filename, 'r') as f:
    data = json.load(f)
    resultados = data['results']
    tabla = pd.DataFrame(resultados)

# print(tabla.head())

resultados = tabla['probabilityofprecip'] + tabla['relativehumidity']
# print(resultados)

# Modificando el tipo de dato.
tabla['probabilityofprecip'] = tabla['probabilityofprecip'].map(int)
tabla['relativehumidity'] = tabla['relativehumidity'].astype(int)
tabla['tempc'] = tabla['tempc'].astype(int)
tabla['iconcode'] = tabla['iconcode'].astype(int)

resultados = tabla['probabilityofprecip'] + tabla['relativehumidity']
# print(resultados)

aux_fun = lambda s: round(float(s), 3)
tabla['latitude'] = tabla['latitude'].map(aux_fun)
tabla['longitude'] = tabla['longitude'].map(aux_fun)

# select = ['longitude', 'longitude']
# print(tabla[select].head())
# print(tabla.dtypes)

def standard_text_to_int(s):
    if isinstance(s, str):
        s = s.strip()
        if s.isdigit():
            return int(s)
    return 0

tabla['windspeedkm'] = tabla['windspeedkm'].map(standard_text_to_int)

date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
tabla['date-insert'] = pd.to_datetime(tabla['date-insert'], format=date_format)

date_format = "%Y%m%dT%H%M%S%fZ"
tabla['validdateutc'] = pd.to_datetime(tabla['validdateutc'], format=date_format)
tabla['lastreporttime'] = pd.to_datetime(tabla['lastreporttime'], format=date_format)

select = ['date-insert', 'validdateutc']
# print(tabla[select])


print(tabla.dtypes)


