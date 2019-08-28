#!/usr/bin/env python
# coding=utf-8

# Importar CSV.

from statistics import mean
import rubik as rk
import pandas as pd

filename = 'data/declaratorias_emergencia_desastre.csv'
tabla = pd.read_csv(filename, encoding='utf-8')


# 1.1. Cuál es el promedio de la magnitud de los sismos por estado.
tabla_1 = (tabla.groupby('estado')['magniud_sismo']
                .mean()
                .rename('magnitud_promedio')
                .reset_index(drop=False))

# 1.2. En cuántas ciudades se registraron los sismos del estado.
tabla_2 = (tabla.groupby('estado')
                .size()
                .rename('registros_por_estado')
                .reset_index(drop=False))

# 1.3. Es posible realizar las dos operaciones en una misma tabla con agg.
tabla_3 = (tabla.groupby('estado')['magniud_sismo']
                .agg(['mean', 'size'])
                .reset_index(drop=False))

# 2.1. Cuántas fechas distintas se tienen registradas por estado.
calcular_fechas_unicas = lambda x: len(set(x.tolist()))
tabla_4 = (tabla.groupby('estado')['fecha_evento']
                .apply(calcular_fechas_unicas)
                .rename('fechas_unicas')
                .reset_index(drop=False))

# 2.2. Cuál es el promedio de la magnitud de los sismos registrados por fecha en cada estado.
def promedio_magnitud(df):
    df = rk.groupto_list(df, ['fecha_evento'], 'magniud_sismo')
    df['magniud_sismo'] = df['magniud_sismo'].map(mean)
    return df
tabla_5 = (tabla.groupby('estado')['magniud_sismo', 'fecha_evento']
                .apply(promedio_magnitud)
                .reset_index(drop=False)
                .drop('level_1', axis=1))


print(tabla_5)