#!/usr/bin/env python
# coding=utf-8

# Importar CSV.

import rubik as rk
import pandas as pd

filename = 'data/declaratorias_emergencia_desastre.csv'
tabla = pd.read_csv(filename, encoding='utf-8')

print(tabla.head())
