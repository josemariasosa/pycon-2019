#!/usr/bin/env python
# coding=utf-8
# author: jose maria sosa

import rubik as rk
import pandas as pd

filename = 'data/declaratorias_emergencia_desastre.csv'
tabla = pd.read_csv(filename, encoding='utf-8')

# # Eliminando todos los valores faltantes
# tabla = tabla.dropna()
# print(tabla.head())
# ------------------------------------------------------------------------------

# # Eliminando las muestras con magnitud de sismo faltante
# mask = tabla['magniud_sismo'].isnull()
# tabla = tabla[~mask].reset_index(drop=True)
# print(tabla.info())
# ------------------------------------------------------------------------------

# # Sustituyendo valores faltantes por un string
# columns = [
#     'declaratoria_emergencia_ordinaria',
#     'declaratoria_emergencia_extraordinaria',
#     'declaratoria_desastre'
# ]
# for column in columns:
#     tabla[column] = tabla[column].fillna('no-aplica')
# print(tabla.info())
# ------------------------------------------------------------------------------

# # Sustituyendo valores dinámicamente
# tabla['magniud_sismo'] = (tabla.groupby('estado')['magniud_sismo']
#                              .transform(lambda x: x.fillna(x.mean())))
# print(tabla.info())
# ------------------------------------------------------------------------------

# Funciones ffill() y bfill()
df = pd.DataFrame({
    "fecha": ["may-2019", None, None, "jun-2019", None, None],
    "estado": ["Jalisco", None, None, "Tamaulipas", None, None],
    "ciudad": [
        'Guadalajara', 'Pto Vallarta', 'Tonalá', 
        'Tampico', 'Nvo Laredo', 'Victoria'
    ],
    "recursos": [400, 366, 89, 511, 12, 22]
})

# print(df.ffill())
# ------------------------------------------------------------------------------
