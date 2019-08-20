#!/usr/bin/env python
# coding=utf-8

# Importar JSON.

import json
import pandas as pd

filename = 'data/conagua.json'
with open(filename, 'r') as f:
    data = json.load(f)
    resultados = data['results']
    tabla = pd.DataFrame(resultados)

print(tabla.head())
