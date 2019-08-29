#!/usr/bin/env python
# coding=utf-8
# author: jose maria sosa

import rubik as rk
import pandas as pd

import xml.etree.ElementTree as ET


class UnirGasolinaPrecio(object):
    """La siguiente clase permite unir la información de las gasolineras y los 
    precios."""
    def __init__(self):
        self.gasoli_file = './data/places.xml'
        self.precio_file = './data/prices.xml'

    def importar_precios(self):
        filename = self.precio_file
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

    def importar_estaciones(self):
        filename = self.gasoli_file
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

    def formato_precios(self, precios):
        precios = rk.ungroup_list(precios, 'gas')
        precios = rk.ungroup_dict(precios, 'gas')
        precios['precio'] = precios['precio'].astype(float)
        precios = precios.pivot_table('precio', ['place_id'], 'tipo')
        precios = precios.reset_index(drop=False)
        return precios

    def formato_estaciones(self, estaciones):
        estaciones = rk.ungroup_dict(estaciones, 'estacion')
        estaciones = rk.ungroup_dict(estaciones, 'location')
        new_names = {'x': 'coord_x', 'y': 'coord_y'}
        return estaciones.rename(columns=new_names)

    def main(self):
        precios = self.importar_precios()
        precios = self.formato_precios(precios)

        estaciones = self.importar_estaciones()
        estaciones = self.formato_estaciones(estaciones)

        # print(precios.info(), estaciones.info())

        resultados = pd.merge(estaciones,
                              precios,
                              on='place_id',
                              how='left')

        print('Todas las estaciones: ')
        print(resultados.head())

        mask = (resultados['diesel'].isnull()
                & resultados['premium'].isnull()
                & resultados['regular'].isnull())
        estaciones_sin_precio = resultados[mask].reset_index(drop=True)
        print('Estaciones sin precio: ')
        print(estaciones_sin_precio.head())

# ------------------------------------------------------------------------------


if __name__ == '__main__':
    UnirGasolinaPrecio().main()
