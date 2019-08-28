#!/usr/bin/env python
# coding=utf-8

import rubik as rk
import pandas as pd

filename = 'data/declaratorias_emergencia_desastre.csv'
tabla = pd.read_csv(filename, encoding='utf-8')

# tabla = tabla.dropna()
# print(tabla.head())

# mask = tabla['magniud_sismo'].isnull()
# tabla = tabla[~mask].reset_index(drop=True)
# print(tabla.info())

# columns = [
#     'declaratoria_emergencia_ordinaria',
#     'declaratoria_emergencia_extraordinaria',
#     'declaratoria_desastre'
# ]
# for column in columns:
#     tabla[column] = tabla[column].fillna('no-aplica')

# print(tabla.head())

# mask = tabla['magniud_sismo'].isnull()
# tabla = tabla[mask].reset_index(drop=True)
# print(tabla)

# promedio_por_estado = tabla.groupby(['estado'])['magniud_sismo'].mean()
# print(promedio_por_estado)

# Creating the dataframe  
df = pd.DataFrame({
    "fecha": ["may-2019", None, None, "jun-2019", None, None],
    "estado": ["Jalisco", None, None, "Tamaulipas", None, None],
    "ciudad": [
        'Guadalajara', 'Pto Vallarta', 'Tonalá', 
        'Tampico', 'Nvo Laredo', 'Victoria'
    ],
    "recursos": [400, 366, 89, 511, 12, 22]
}) 
  
# Print the dataframe 
print(df.ffill())