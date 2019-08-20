#!/usr/bin/env python
# coding=utf-8

# ------------------------------------------------------------------------------
# From XML-file to Pandas DataFrame
# ------------------------------------------------------------------------------
# jose maria sosa

import rubik as rk
import pandas as pd

import xml.etree.ElementTree as ET


def importar_precios(filename):

    tree = ET.parse(filename)
    root = tree.getroot()

    data = []
    for node in root:
        precios = []
        for child in node:
            precios.append({
                'tipo': child.attrib['type'],
                'precio': child.text
            })
        to_insert = {
            'place_id': node.attrib['place_id'],
            'gas': precios
        }
        data.append(to_insert)

    tabla = pd.DataFrame(data)
    return tabla

def importar_estaciones(filename):

    tree = ET.parse(filename)
    root = tree.getroot()

    data = []
    for node in root:
        estacion = {}
        for child in node:
            if child.tag == 'name':
                estacion.update({
                    'nombre': child.text
                })
            elif child.tag == 'cre_id':
                estacion.update({
                    'cre_id': child.text
                })
            elif child.tag == 'location':
                location = {}
                for loc in child:
                    if loc.tag == 'x':
                        location.update({
                            'x': loc.text
                        })
                    elif loc.tag == 'y':
                        location.update({
                            'y': loc.text
                        })
                estacion.update({
                    'location': location
                })
        to_insert = {
            'place_id': node.attrib['place_id'],
            'estacion': estacion
        }
        data.append(to_insert)

    tabla = pd.DataFrame(data)
    return tabla


def main():

    file_precios = './data/prices.xml'
    file_estaciones = './data/places.xml'
    precios = importar_precios(file_precios)
    estaciones = importar_estaciones(file_estaciones)

    print('Tabla de precios: ')
    print(precios.head())
    print('\nTabla de estaciones: ')
    print(estaciones.head())

# ------------------------------------------------------------------------------

if __name__ == '__main__':
    main()