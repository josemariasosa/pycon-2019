#!/usr/bin/env python
# coding=utf-8
# author: jose maria sosa

import json
import rubik as rk
import pandas as pd


class TransformarEstructura(object):
    """Modificar la estructura de la información."""
    def __init__(self):
        self.filename = 'data/productos.csv'

    def importar_productos(self):
        return pd.read_csv(self.filename, encoding='utf-8')

    def formato_imagen(self, images_list):
        return [x for x in images_list if len(x) > 0]

    def modificar_imagenes(self, productos):
        new_names = {
            'imagen_principal': 'main'
        }
        productos = productos.rename(columns=new_names)
        columnas = ['imagen_secundaria_1', 'imagen_secundaria_2']
        for columna in columnas:
            productos[columna] = productos[columna].fillna('')
        productos = rk.concat_to_list(productos, columnas, 'images_list')
        productos['images_list'] = productos['images_list'].map(self.formato_imagen)
        productos = rk.groupto_dict(productos, ['main', 'images_list'], 'image')
        return productos

    def modificar_atributos(self, productos):
        atributos = ['talla', 'color']
        for atributo in atributos:
            new_names = {atributo: 'value'}
            productos = productos.rename(columns=new_names)
            productos['name'] = atributo
            productos = rk.groupto_dict(productos, ['name', 'value'], atributo)
        productos = rk.concat_to_list(productos, atributos, 'attributes')
        return productos

    def formato_precio(self, precio):
        precio = precio.replace('$', '').replace('.', '').strip()
        precio = float(precio)
        return '{:.2f}'.format(precio)

    def modificar_precios(self, productos):
        new_names = {'precio': 'price'}
        productos = productos.rename(columns=new_names)
        productos['price'] = productos['price'].map(self.formato_precio)
        productos['currency'] = 'MXN'
        return productos

    def agrupando_variantes(self, productos):
        new_names = {
            'inventario': 'stock',
            'producto': 'product_name',
            'numero_parte': 'part_number',
            'marca': 'brand'
        }
        productos = productos.rename(columns=new_names)
        productos['stock'] = productos['stock'].astype(str)
        variante = ['price', 'stock', 'image', 'attributes', 'currency']
        productos = rk.groupto_dict(productos, variante, 'variants')
        columnas = ['product_name', 'part_number', 'brand']
        productos = rk.groupto_list(productos, columnas, 'variants')
        return productos

    def main(self):
        productos = self.importar_productos()
        productos = self.modificar_imagenes(productos)
        productos = self.modificar_atributos(productos)
        productos = self.modificar_precios(productos)
        productos = self.agrupando_variantes(productos)

        productos = productos.to_dict(orient='records')
        with open('data/productos.json', 'w') as f:
            json.dump(productos, f)
        print(productos)

if __name__ == '__main__':
    TransformarEstructura().main()
