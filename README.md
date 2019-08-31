# Automatizando el análisis y procesamiento de datos con pandas.

Slides: https://docs.google.com/presentation/d/1ZvgiMvP0QP7RMW7jKdsRXdujRtf_k87-7ypG9ma1Y_s/edit?usp=sharing

## Contenido de la presentación

1. [**Introducción a pandas**](https://github.com/josemariasosa/pycon-2019#1-introducci%C3%B3n-a-pandas)
    - 1.1. Qué es pandas.
    - 1.2. Cómo instalar pandas.
    - 1.3. Dónde está la documentación oficial.

2. [**Importar datos utilizando pandas**](https://github.com/josemariasosa/pycon-2019#2-importar-datos-utilizando-pandas)
    - 2.1. Importar y exportar JSON.
    - 2.2. Importar y exportar CSV.
    - 2.3. Importar EXCEL.
    - 2.4. Importar XML.

3. [**Conociendo nuestros datos**](https://github.com/josemariasosa/pycon-2019#3-conociendo-nuestros-datos)
    - 3.1. Head, tail & info.
    - 3.2. Fechas y tipos de datos.
    - 3.3. Valores faltantes.

4. [**Introducción a rubik**](https://github.com/josemariasosa/pycon-2019#4-introducci%C3%B3n-a-rubik)
    - 4.1. Introducción.
    - 4.2. Instalación.

5. [**Casos de uso de pandas + rubik**](https://github.com/josemariasosa/pycon-2019#5-casos-de-uso-de-pandas--rubik)
    - 5.1. Transformar la estructura de la información.
    - 5.2. Agrupación de información (groupby).
    - 5.3. Uniendo múltiples fuentes de información (merge).

---

## 1. Introducción a pandas

### 1.1. Qué es pandas.

Consultado el [sitio oficial](https://pandas.pydata.org/), pandas es un conjunto de herramientas para estructurar, manipular y analizar datos mediante el lenguaje de programación python. Permite estructurar la información de manera tabular mediante el uso de tablas conocidas como **DataFrames**.

Pandas es de código abierto y puede ser utilizado de manera gratuita bajo la [licencia BSD](https://en.wikipedia.org/wiki/BSD_licenses).

### 1.2. Cómo instalar pandas.

Instalar pandas puede resultar un poco enredos para usuarios inexpertos. La manera más simple de instalar pandas, junto con un listado de las librerías más populares, es a través de [Anaconda](https://www.anaconda.com/distribution/). También, si se desea tener más control sobre los paquetes o se tiene una conexión de internet limitada, existe una versión de tamaño más reducida conocida como [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

Sin embargo, la manera más directa es instalar pandas directamente desde la terminal, utilizando el administrador de paquetes de python pip.

```bash
pip install pandas
```

Para consultar la información completa sobre la instalación de pandas recomiendo revisar la [documentación oficial](https://pandas.pydata.org/pandas-docs/stable/install.html).

### 1.3. Dónde está la documentación oficial.

La documentación oficial de la versión más actualizada de pandas se encuentra disponible en inglés siguiendo la liga:

https://pandas.pydata.org/pandas-docs/stable/

## 2. Importar datos utilizando pandas

### 2.1. Importar y exportar JSON.

Para poder trabajar con archivos tipo JSON, hay que utilizar la función de la librería base [json **load()**](https://docs.python.org/3/library/json.html#basic-usage). El código se encuentra en el archivo [**2-1-import-json.py**](https://github.com/josemariasosa/pycon-2019/blob/master/pyFiles/2-1-import-json.py).

```python
import json
import pandas as pd

filename = 'data/conagua.json'
with open(filename, 'r') as f:
    data = json.load(f)
    resultados = data['results']
    tabla = pd.DataFrame(resultados)

print(tabla.head())
```

Para llevar a cabo el proceso inverso, y convertir un DataFrame a un formato JSON se utiliza el método de [pandas **to_dict()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html), incluyendo el argumento `orient='records'` como se muestra a continuación.

```python
json_structure = tabla.to_dict(orient='records')
```

Para **exportar** un DataFrame en formato JSON utilizamos la función de [json **dump()**](https://docs.python.org/3/library/json.html#basic-usage) como se muestra a continuación.

```python
productos = productos.to_dict(orient='records')
with open('data/productos.json', 'w') as f:
    json.dump(productos, f)
```

### 2.2. Importar y exportar CSV.

Para importar un archivo en formato CSV (comma separated values), se utiliza directamente la función de [pandas **read_csv()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html).

El código completo de esta sección se encuentra en el archivo [**2-2-import-csv.py**](https://github.com/josemariasosa/pycon-2019/blob/master/pyFiles/2-2-import-csv.py).

```python
import pandas as pd

filename = 'data/declaratorias_emergencia_desastre.csv'
tabla = pd.read_csv(filename, encoding='utf-8')

print(tabla.head())
```

Para exportar un DataFrame a un formato csv, se utiliza la función de [pandas **to_csv()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html) como se muestra a continuación.

```python
filename = 'data/tabla_nueva.csv'
tabla.to_csv(filename, index=False, encoding='utf-8')
```

### 2.3. Importar EXCEL.

Pandas permite la importación directa de archivos tipo xlsx, el cual es el formato utilizado en Microsoft Excel, mediante la función de [pandas **read_excel()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html).

```python
import pandas as pd

filename = 'data/declaratorias_emergencia_desastre.xlsx'
tabla = pd.read_excel(filename)

print(tabla.head())
```

### 2.4. Importar XML.

Para trabajar con datos en formato xml, descargamos un par de archivos sobre la información de los **precios de la gasolina** desde la página oficial de [datos de gobierno](https://datos.gob.mx/busca/dataset/estaciones-de-servicio-gasolineras-y-precios-finales-de-gasolina-y-diesel). Nombramos los archivos: **places.xml** y **prices.xml**.

No existe una manera directa de convertir el formato de la información contenida en un archivo xml a un formato tabular. Sin embargo, mediante python podemos pre-procesar los datos para convertirlos en un DataFrame.

El código completo de esta sección se encuentra en el archivo [**2-4-import-xml.py**](https://github.com/josemariasosa/pycon-2019/blob/master/pyFiles/2-4-import-xml.py).

Para cargar un archivo xml en python necesitamos de la función [**parse()**](https://docs.python.org/2/library/xml.etree.elementtree.html) contenida en la librería base [**xml.etree.ElementTree**](https://docs.python.org/2/library/xml.etree.elementtree.html). El siguiente código puede servir de apoyo para extraer la información necesaria de un xml.

```python
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
```

## 3. Conociendo nuestros datos

Antes de realizar cualquier análisis o procesamiento en los datos, hay que estar seguro de conocer a fondo nuestra información.

### 3.1. Head, tail & info.

Los tres principales métodos para visualizar de manera preeliminar la información contenida dentro de un DataFrame son: head, tail e info.

La función de [pandas **head()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html) regresa las primeras `n=5` filas de una tabla. Es útil para comprobar que nuestro objeto contiene los tipos de datos correctos.

```python
print(df.head())
#       animal
# 0  alligator
# 1        bee
# 2     falcon
# 3       lion
# 4     monkey
```

La función de [pandas **tail()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.tail.html) regresa las últimas `n=5` filas de una tabla. Es útil para verificar los datos después de haber sido ordenardos o al insertar (append) filas.

```python
print(df.tail(3))
#    animal
# 6   shark
# 7   whale
# 8   zebra
```

La función de [pandas **info()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html) imprime información acerca del DataFrame, incluyendo el [tipo de dato (dtype)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dtypes.html), los índices, las columnas, los valores nulos y el uso de memoria.

```python
print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5 entries, 0 to 4
# Data columns (total 3 columns):
# int_col      5 non-null int64
# text_col     5 non-null object
# float_col    5 non-null float64
# dtypes: float64(1), int64(1), object(1)
# memory usage: 248.0+ bytes
```

### 3.2. Fechas y tipos de datos.

Lo primero que debemos revisar, cuando comenzamos a trabajar con datos, son los [tipos de datos](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dtypes.html). Es importante asegurarnos de estar utilizando el tipo de dato correcto, porque este es uno de esos puntos que se nos olvida revisar hasta que se genera un error o algún otro resultado inesperado.
 
Los tipos de datos en pandas se conoce como **dtypes**. Los dtypes se enlistan a continuación: 

- object
- int64
- float64
- datetime64
- bool

Trabajando con la información cargada en la sección [**2.1. Importar y exportar JSON**](https://github.com/josemariasosa/pycon-2019#21-importar-y-exportar-json), nos aseguraremos de contar con los tipos de datos correcto.

El código completo de esta sección se encuentra en [**3-2-dtypes.py**](https://github.com/josemariasosa/pycon-2019/blob/master/pyFiles/3-2-dtypes.py).

```python
print(tabla.head())
#                         _id    cityid      validdateutc   ...
# 0  5952983359954a0adbf7ab09  MXAS0002  20170627T140000Z
# 1  5952983359954a0adbf7ab0a  MXAS0170  20170627T140000Z
# 2  5952983359954a0adbf7ab0b  MXAS0171  20170627T140000Z
# 3  5952983359954a0adbf7ab0c  MXAS0172  20170627T140000Z
# 4  5952983359954a0adbf7ab0d  MXAS0173  20170627T140000Z

#     skydescriptionlong stateabbr tempc  latitude iconcode windspeedkm
# 0  Tormentas dispersas       AGU    17  21.87982       96           6
# 1  Tormentas dispersas       AGU    15  22.23832       96           5
# 2  Tormentas dispersas       AGU    19  21.84691       96           2
# 3  Tormentas dispersas       AGU    17  22.36641       96           3
# 4  Tormentas dispersas       AGU    17  21.91887       96           3
```

Si quisieramos sumar los valores de las columnas `probabilityofprecip` y `relativehumidity`, lo llevaríamos a cabo de la siguiente manera.

```python
resultados = tabla['probabilityofprecip'] + tabla['relativehumidity']
print(resultados)
# 0     4090
# 1     6091
# 2     6084
# 3     5083
# 4     5084
#       ...
# 95     084
# 96    2082
# 97    2057
# 98    2079
# 99    2062
# Length: 100, dtype: object
```

Los resultados no son, claramente, los esperados. Queríamos sumar las cantidades de las dos columnas, y lo que se obtuvo fue concatenar los valores. Parte de la solución se encuentra en el **dtype: object** de la columna resultante. Un `object` es un string en pandas, por lo tanto, realiza operaciones de strings no aritméticas.

Si queremos conocer los tipos de datos de un DataFrame, utilizamos el atributo de [pandas **dtypes**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dtypes.html):

```python
print(tabla.dtypes)
# _id                      object
# cityid                   object
# validdateutc             object
# winddirectioncardinal    object
# probabilityofprecip      object
# relativehumidity         object
# name                     object
# date-insert              object
# longitude                object
# state                    object
# lastreporttime           object
# skydescriptionlong       object
# stateabbr                object
# tempc                    object
# latitude                 object
# iconcode                 object
# windspeedkm              object
# dtype: object
```

Todas las columnas, a pesar de contener algunas valores numéricos, fueron interpretadas en pandas como strings. Para convertir un tipo de dato en pandas existen tres opciones básicas:

- Utilizar [**astype()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.astype.html) para forzar el dtype adecuado.
- Crear una función customizada para convertir el tipo de dato.
- Utilizar las funciones de pandas [**to_numeric()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_numeric.html) o [**to_datetime()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html).

Revisaremos a detalle cada una de estas 3 opciones.

#### 3.2.1. El método astype().

El método más simple para convertir una columna a los diferentes tipos de datos es utilizar la función de [pandas **astype()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.astype.html). Por ejemplo, convertiremos las columnas `probabilityofprecip` y `relativehumidity` a valores numéricos para realizar la suma de manera correcta.

```python
# Convertir el tipo de dato de objeto a entero.
tabla['probabilityofprecip'] = tabla['probabilityofprecip'].astype(int)
tabla['relativehumidity'] = tabla['relativehumidity'].astype(int)

resultados = tabla['probabilityofprecip'] + tabla['relativehumidity']
print(resultados)
# 0     130
# 1     151
# 2     144
# 3     133
# 4     134
#      ...
# 95     84
# 96    102
# 97     77
# 98     99
# 99     82
# Length: 100, dtype: int64
```

#### 3.2.2. Creando una función customisada.

Otra opción es utilizando la función de [pandas **map()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html), para aplicar una función en **cada uno de los elementos** de la columna. La opción más directa sería:

```python
tabla['probabilityofprecip'] = tabla['probabilityofprecip'].map(int)
```

Esta sintaxis funciona de manera similar a **astype()**. Sin embargo, quizá querramos utilizar funciones que lleven a cabo más pasos. Vamos a realizar 2 ejemplos: 1) con una función lambda y 2) declarando una función. 

##### Ejemplo 1: Función lambda

Queremos convertir las columnas de `latitud` y `longitud` en valores flotantes, conservando únicamente los valores redondeados hasta 3 decimales. 

Nuestra función lambda convertirá el string a tipo float y luego redondeará el valor a 3 decimales. Al final, podemos utilizar una variable auxiliar `select` para filtrar las columnas del DataFrame.

```python
aux_fun = lambda s: round(float(s), 3)
tabla['latitude'] = tabla['latitude'].map(aux_fun)
tabla['longitude'] = tabla['longitude'].map(aux_fun)

select = ['longitude', 'longitude']
print(tabla[select].head())
#    longitude  longitude
# 0   -102.296   -102.296
# 1   -102.089   -102.089
# 2   -102.719   -102.719
# 3   -102.300   -102.300
# 4   -101.965   -101.965
```

##### Ejemplo 2: Declarando una función

Para este ejemplo, podríamos llevar a cabo la **limpieza** de un string, para interpretar correctamente su valor numérico.

```python
def standard_text_to_int(s):
    if isinstance(s, str):
        s = s.strip()
        if s.isdigit():
            return int(s)
    return 0

tabla['windspeedkm'] = tabla['windspeedkm'].map(standard_text_to_int)

select = 'windspeedkm'
print(tabla[select])
# 0      6
# 1      5
# 2      2
# 3      3
# 4      3
#      ...
# 95    11
# 96    11
# 97    10
# 98     8
# 99     0
# Name: windspeedkm, Length: 100, dtype: int64
```

Recordemos que la función [base **isinstance()**](https://docs.python.org/3/library/functions.html) regresa **True** si el objeto es un string. Posteriormente, el método de los [strings **strip()**](https://docs.python.org/3.7/library/string.html) elimina espacios innecesarios al inicio y al final. Por último, [**isdigit()**](https://docs.python.org/3.7/library/string.html) evalúa si es posible convertir un texto a un valor entero, previniendo errores en el código.

#### 3.2.3. Uso de tiempo y fechas.

Es común que la fecha se almacene como string, si se desean utilizar las propiedades de las fechas, hay que convertir la columna a formato **datetime**. Una de las maneras de llevar a cabo esto es a través de la función de [pandas **to_datetime()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html).

```python
date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
tabla['date-insert'] = pd.to_datetime(tabla['date-insert'], format=date_format)

select = 'date-insert'
print(tabla[select])
# 0    2017-06-27 17:36:43.084
# 1    2017-06-27 17:36:43.088
# 2    2017-06-27 17:36:43.088
# 3    2017-06-27 17:36:43.088
# 4    2017-06-27 17:36:43.089
#                ...
# 95   2017-06-27 17:36:43.107
# 96   2017-06-27 17:36:43.108
# 97   2017-06-27 17:36:43.108
# 98   2017-06-27 17:36:43.108
# 99   2017-06-27 17:36:43.108
# Name: date-insert, Length: 100, dtype: datetime64[ns]
```

El dtype cambió a datetime64[ns]. Recomiendo revisar la [información completa](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior) de los formatos de fecha en python, pero los formatos más comunes son: `"%d-%m-%Y"`, `"%d/%m/%Y"` y `"%m-%y"`; donde:

- **%d** - indica el día del mes en dos dígitos: 21, 04, 31 son válidos.
- **%m** - indica el mes en dos dígitos: 01, 12, 09 son válidos.
- **%b** - indica el mes abreviado con 3 letras: jan, feb, dec son válidos.
- **%Y** - indica el año con 4 dígitos: 2000, 1998 y 2019 son válidos.
- **%y** - indica el año con 2 dígitos: 99, 19, 00 son válidos.

Al final, después de revisar toda la información, los tipos de datos de nuestro DataFrame deben lucir de la siguiente manera.

```python
print(tabla.dtypes)
# _id                              object
# cityid                           object
# validdateutc             datetime64[ns]
# winddirectioncardinal            object
# probabilityofprecip               int64
# relativehumidity                  int64
# name                             object
# date-insert              datetime64[ns]
# longitude                       float64
# state                            object
# lastreporttime           datetime64[ns]
# skydescriptionlong               object
# stateabbr                        object
# tempc                             int64
# latitude                        float64
# iconcode                          int64
# windspeedkm                       int64
# dtype: object
```

### 3.3. Valores faltantes.

Cuando se imprimen los valores ausentes dentro de un DataFrame aparecen como [**NaN**](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html).

Para esta sección, trabajaremos con el DataFrame que importamos en la sección [**2.2. Importar y exportar CSV**](https://github.com/josemariasosa/pycon-2019#22-importar-y-exportar-csv), sobre la magnitud de sismos. 

El código completo de esta sección puede ser consultado en [**3-3-nan.py**](https://github.com/josemariasosa/pycon-2019/blob/master/pyFiles/3-3-nan.py).

```python
print(tabla.head())
#     estado   municipio  clave_inegi declaratoria_emergencia_ordinaria  \
# 0  Chiapas  Acacoyagua         7001                               NaN
# 1  Chiapas       Acala         7002                               NaN
# 2  Chiapas  Acapetahua         7003                               NaN
# 3  Chiapas  Altamirano         7004                               NaN
# 4  Chiapas      Amatán         7005                               NaN

#   declaratoria_emergencia_extraordinaria declaratoria_desastre  magniud_sismo  \
# 0                                     sí                    sí            8.2
# 1                                     sí                    sí            8.2
# 2                                     sí                    sí            8.2
# 3                                     sí                    sí            8.2
# 4                                     sí                    sí            8.2

#   fecha_evento
# 0   2017-09-07
# 1   2017-09-07
# 2   2017-09-07
# 3   2017-09-07
# 4   2017-09-07
```

La función de [pandas **info()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html) nos permite visualizar cuántos valores en una columna son faltantes. Por ejemplo, la columna `declaratoria_emergencia_ordinaria` únicamente cuenta con 75 objetos no nulos.

```python
print(tabla.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 725 entries, 0 to 724
# Data columns (total 8 columns):
# estado                                    725 non-null object
# municipio                                 725 non-null object
# clave_inegi                               725 non-null int64
# declaratoria_emergencia_ordinaria         75 non-null object
# declaratoria_emergencia_extraordinaria    325 non-null object
# declaratoria_desastre                     699 non-null object
# magniud_sismo                             722 non-null float64
# fecha_evento                              725 non-null object
# dtypes: float64(1), int64(1), object(6)
# memory usage: 45.4+ KB
```

Es importante mencionar que cuando una **columna de valores enteros** cuenta con un valor faltante, automáticamente la lista se convierte en tipo flotante.

Para poder trabajar con valores faltantes, en un DataFrame, es crucial definir una estrategia. Las principales maneras de hacerlo son 3:

- **Eliminar** las muestras con valores faltantes.
- Establecer un **valor fijo** que tendrán todos los valores faltantes.
- Cálculo de **valores dinámicos** para cada uno de los valores faltantes.

Revisaremos a detalle cada una de ellas.

#### 3.3.1. Eliminar las muestras con valores faltantes.

Las cuatro columnas que tienen valores faltantes son:

```
# declaratoria_emergencia_ordinaria         75 non-null object
# declaratoria_emergencia_extraordinaria    325 non-null object
# declaratoria_desastre                     699 non-null object
# magniud_sismo                             722 non-null float64
```

Para eliminar todas las muestras en donde exista al menos un valor faltante se utiliza la función de [pandas **dropna()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html).

```python
tabla = tabla.dropna()
print(tabla.info())
# Empty DataFrame
# Columns: [estado, municipio, clave_inegi, declaratoria_emergencia_ordinaria, declaratoria_emergencia_extraordinaria, declaratoria_desastre, magniud_sismo, fecha_evento]
# Index: []
```

Tristemente obtenemos un DataFrame vacío. No existe una sola muestra donde no haya al menos un valor faltante. Entonces, lo que haremos es eliminar todas las observaciones únicamente en donde `magniud_sismo` se encuentre ausente.

Cuando queremos eliminar, los valores ausentes de una columna, tenemos que crear una columna ficticia (conocida como **mask**) que nos permita filtrar los valores correspondientes, mediante el método de [pandas **isnull()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isnull.html). El símbolo `~` sobre **mask**, nos permite invertir los valores booleanos.

Por último, el método de [pandas **reset_index()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html) reinicia el la numeración de los índices. Si se le indica drop=False, entonces los índices actuales se convierten en una columna más del dataframe.

```python
mask = tabla['magniud_sismo'].isnull()
tabla = tabla[~mask].reset_index(drop=True)

print(tabla.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 722 entries, 0 to 721
# Data columns (total 8 columns):
# estado                                    722 non-null object
# municipio                                 722 non-null object
# clave_inegi                               722 non-null int64
# declaratoria_emergencia_ordinaria         74 non-null object
# declaratoria_emergencia_extraordinaria    324 non-null object
# declaratoria_desastre                     696 non-null object
# magniud_sismo                             722 non-null float64
# fecha_evento                              722 non-null object
# dtypes: float64(1), int64(1), object(6)
# memory usage: 45.2+ KB
```

#### 3.3.2. Establecer un valor único que tendrán todos los valores faltantes.

Existen casos en donde lo mejor es definir un **valor único** que sustituya los valores faltantes. Considerando que el valor que se defina sea consistente con las mediciones. Es común que se utilice un string, el valor 0, o algún otro estimador.

Para este ejemplo, continuaremos con los valores faltantes de la sección anterior. Para las columnas `declaratoria_emergencia_ordinaria`, `declaratoria_emergencia_extraordinaria` y `declaratoria_desastre` cambiaremos los valores faltantes por el string de **'no-aplica'** utilizando el método de [pandas **fillna()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html).

```python
columns = [
    'declaratoria_emergencia_ordinaria',
    'declaratoria_emergencia_extraordinaria',
    'declaratoria_desastre'
]
for column in columns:
    tabla[column] = tabla[column].fillna('no-aplica')

print(tabla.head())
#     estado   municipio  clave_inegi declaratoria_emergencia_ordinaria  \
# 0  Chiapas  Acacoyagua         7001                         no-aplica
# 1  Chiapas       Acala         7002                         no-aplica
# 2  Chiapas  Acapetahua         7003                         no-aplica
# 3  Chiapas  Altamirano         7004                         no-aplica
# 4  Chiapas      Amatán         7005                         no-aplica

#   declaratoria_emergencia_extraordinaria declaratoria_desastre  magniud_sismo  \
# 0                                     sí                    sí            8.2
# 1                                     sí                    sí            8.2
# 2                                     sí                    sí            8.2
# 3                                     sí                    sí            8.2
# 4                                     sí                    sí            8.2

#   fecha_evento
# 0   2017-09-07
# 1   2017-09-07
# 2   2017-09-07
# 3   2017-09-07
# 4   2017-09-07
```

##### Utilizando rubik para sustituir los valores faltantes por listas vacías.

En la sección [**4. Introducción a rubik**](https://github.com/josemariasosa/pycon-2019#4-introducci%C3%B3n-a-rubik) revisaremos el módulo de rubik, mientras tanto, introduciremos la función de [rubik **fillna_list()**](https://github.com/josemariasosa/rubik#1-the-rkfillna_list-function) que nos permite sustituir los valores faltantes por listas vacías.

```python
new = rk.fillna_list(original, 'Roles')
```

De la tabla original:

| Entry | Id        | Roles     |
|-------|-----------|-----------|
| 0     | user-123  | NaN       |
| 1     | user-452  | [1]       |
| 2     | user-21   | [5, 2]    |
| 3     | user-621  | NaN       |
| 4     | user-5512 | [3, 4]    |
| 5     | user-25   | [1, 2, 3] |

Se obtiene esta nueva tabla donde los valores faltantes son listas vacías:

| Entry | Id        | Roles     |
|-------|-----------|-----------|
| 0     | user-123  | [ ]       |
| 1     | user-452  | [1]       |
| 2     | user-21   | [5, 2]    |
| 3     | user-621  | [ ]       |
| 4     | user-5512 | [3, 4]    |
| 5     | user-25   | [1, 2, 3] |

#### 3.3.3. Cálculo de valores dinámicos para cada uno de los valores faltantes.

Por último, es común que también que se utilicen cálculos más complejos para el llenado de los valores faltantes. Por ejemplo, utilizar alguna medida de tendencia central, como la media, mediana o moda que estime el valor faltante a partir de la información con la que se cuenta.

##### Utilizando la función transform

En nuestro ejemplo tenemos varias mediciones de la `magniud_sismo` que están ausentes. Para poder obtener el valor de dichas mediciones ausentes se puede utilizar un estimado, como por ejemplo **el promedio de la magnitud del sismo por estado**. Podemos agrupar los valores y sacar la media para utilizarla posteriormente en los valores faltantes mediante la función de [pandas **transform()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.transform.html).

```python
tabla['magniud_sismo'] = (tabla.groupby('estado')['magniud_sismo']
                               .transform(lambda x: x.fillna(x.mean())))
print(tabla.info())
```

##### Utilizando las funciones bfill y ffill

Las funciones de [pandas **bfill()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.bfill.html) y [pandas **ffill()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.ffill.html) nos permiten llenar hacia atrás (backward fill) o hacia adelante (forward fill) los valores NaN presentes en un DataFrame.

En este ejemplo, la fecha y el estado no están presentes, pero se pueden definir a partir del último valor en la tabla.

```python
df = pd.DataFrame({
    "fecha": ["may-2019", None, None, "jun-2019", None, None],
    "estado": ["Jalisco", None, None, "Tamaulipas", None, None],
    "ciudad": [
        'Guadalajara', 'Pto Vallarta', 'Tonalá', 
        'Tampico', 'Nvo Laredo', 'Victoria'
    ],
    "recursos": [400, 366, 89, 511, 12, 22]
}) 
  
print(df.ffill())
#       fecha      estado        ciudad  recursos
# 0  may-2019     Jalisco   Guadalajara       400
# 1  may-2019     Jalisco  Pto Vallarta       366
# 2  may-2019     Jalisco        Tonalá        89
# 3  jun-2019  Tamaulipas       Tampico       511
# 4  jun-2019  Tamaulipas    Nvo Laredo        12
# 5  jun-2019  Tamaulipas      Victoria        22
```

## 4. Introducción a rubik

### 4.1. Introducción.

Rubik es un módulo sencillo para python que compila un listado de funciones para trabajar con pandas. Las funciones listadas en rubik llevan a cabo una abstracción de pasos concretos para permitir llevar a cabo transformaciones sencillas en la estructura de los DataFrames de pandas, con el fin de reducir la cantidad de código necesario para desempeñar dicha actividad.

Un buen ejemplo es la función de [rubik **ungroup_list()**](https://github.com/josemariasosa/rubik#3-the-rkungroup_list-function) permite transformar un DataFrame que tiene listas anidadas en una columna, por otro con las listas desplegadas en filas nuevas. Por otro lado, la función de [rubik **groupto_list()**](https://github.com/josemariasosa/rubik#5-the-rkgroupto_list-function) lleva a cabo la operación inversa, agrupa las filas de un DataFrame para generar listas.

El siguiente par de tablas describen perfectamente estos dos comportamientos.

La función de [rubik **ungroup_list()**](https://github.com/josemariasosa/rubik#3-the-rkungroup_list-function) permite ir de esta tabla a la siguiente.

| Entry | Id       | Roles  |
|-------|----------|--------|
| 0     | user-123 | [1, 2] |
| 1     | user-452 | [5, 7] |
| 2     | user-21  | [3]    |

Por el otro lado, la función de [rubik **groupto_list()**](https://github.com/josemariasosa/rubik#5-the-rkgroupto_list-function) permite ir de esta tabla a la anterior.

| Entry | Id       | Roles |
|-------|----------|-------|
| 0     | user-123 | 1     |
| 0     | user-123 | 2     |
| 1     | user-452 | 5     |
| 1     | user-452 | 7     |
| 2     | user-21  | 3     |

La documentación completa de rubik, con algunos ejemplos, puede ser encontrada en:

https://github.com/josemariasosa/rubik

### 4.2. Instalación.

Para instalar rubik desde la terminal, primero crear un ambiente virtual **venv**, posteriormente usar el comando de **pip install**.

```bash
python3 -m venv venv
source venv/bin/activate

pip install git+https://github.com/josemariasosa/rubik
```

Para asegurarse de que la instalación fue correcta, revisar la versión de rubik con el siguiente comando desde la terminal.

```bash
python -c 'import rubik; print(rubik.__version__)'
# 2.0.0
```

Para utilizar rubik dentro de tus scripts, importar el módulo de rubik utilizando el alias de rk.

```python
import rubik as rk
import pandas as pd
```

## 5. Casos de uso de pandas + rubik

### 5.1. Transformar la estructura de la información.

Es muy común llevar a cabo transformaciones en la estructura de la información, sobre todo en los siguientes casos:

- Eficientar una base de datos.
- Limpieza y pre-procesamiento de información.
- Compartir datos con un tercero que solicita una estructura definida.
- Recibir datos de un tercero para almacenarnos siguiendo una estructura pre-establecida.

Vamos a desarrollar un ejemplo en donde vamos a transformar la estructura de un listado de productos para poderla subir a un supuesto sitio de e-commerce.

#### Caso de uso: Automatizando la venta en línea.

Contamos con un archivo en formato csv, [**productos.csv**](https://github.com/josemariasosa/pycon-2019/blob/master/data/productos.csv), que almacena la información de un listado de productos. Para poder subir la información de nuestros productos a un sitio de e-commerce que se encargará de publicarlos en línea, debemos de envíar un archivo JSON con la siguiente estructura:

```json
[
    {
        "product_name": "Playera",
        "part_number": "t-0001",
        "brand": "Squalo",
        "variants": [
            {
                "price": "440.00",
                "stock": "2",
                "image": {
                    "main": "https://assets.squalo.com/images/t-0001-blue.jpg",
                    "images_list": [
                        "https://assets.squalo.com/images/t-0001-blue-1.jpg"
                    ]
                },
                "attributes": [
                    {
                        "name": "talla",
                        "value": "S"
                    },
                    {
                        "name": "color",
                        "value": "Azul"
                    }
                ],
                "currency": "MXN"
            }
        ]
    }
]
```

El JSON está conformado por los siguientes cuatro atributos principales, y subsecuentes atributos secundarios:

- **product_name** - Un *string* que representa el nombre del producto.
- **part_number** - Un *string* único por producto, ejemplos: SKU, UPC, GTIN.
- **brand** - Un *string* con la marca o vendedor del producto.
- **variants** - Una *lista* que a su vez contiene la información detallada de cada una de las variantes del producto. Para dar de alta una variante, se necesita crear un objeto por cada una con la siguiente información:
    - **price** - Un *string* con 2 decimales del precio.
    - **currency** - Un *string* indicando la moneda, ejemplos: USD, CAD, MXN.
    - **stock** - Un *string* con la cantidad del producto en stock.
    - **image** - Un *diccionario* que indique cuál es la imagen principal, y las imágenes secundarias, con la siguiente estructura.
        - **main** - Un *string* con el url donde está hosteada la imagen.
        - **images_list** - Una *lista* de strings con los urls de las imágenes secundarias. Si no hay imágenes entonces dejar la lista vacía.
    - **attributes** - Una *lista* de atributos, donde cada atributo cuenta con la siguiente información:
        - **name** - Un *string* con el nombre del atributo.
        - **value** - Un *string* con el valor del atributo.

Nuestro objetivo es realizar un script en Python que nos permita generar esta estructura de manera automatizada. Todo el código de esta sección se encuentra en el archivo [**5-1-products.py**](https://github.com/josemariasosa/pycon-2019/blob/master/pyFiles/5-1-products.py).

Vamos a generar una clase con el nombre **TransformarEstructura** que contenga un método llamado **main()**. El método **main()** cuenta con 6 pasos que irán transformando paso a paso la tabla original de productos a la estructura destino.

```python
    def main(self):
        productos = self.importar_productos()
        productos = self.modificar_imagenes(productos)
        productos = self.modificar_atributos(productos)
        productos = self.modificar_precios(productos)
        productos = self.agrupando_variantes(productos)

        productos = productos.to_dict(orient='records')
        print(productos)
```

El primer paso es cargar los productos mediante el método **importar_productos()**. El siguiente método, **modificar_imagenes()**, primero modifica el nombre de la columnas y completa los valores faltantes con un string vacío, tal como se muestra a continuación.

```python
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
```

Aquí vamos a utilizar el método de [rubik **concat_to_list()**](https://github.com/josemariasosa/rubik#2-the-rkconcat_to_list-function) para concatenar en una misma lista las columnas de imágenes secundarias en una sola. Posteriormente, aplicaremos el método **formato_imagen()** para eliminar las imágenes faltantes. Por último, la función de [rubik **groupto_dict()**](https://github.com/josemariasosa/rubik#8-the-rkgroupto_dict-function) nos permite agrupar múltiples columnas en una sola columna como diccionarios.

El paso 2, **modificar_atributos()**, genera primero la estructura de los atributos con `name` y `value` y luego aplica la función de [rubik **concat_to_list()**](https://github.com/josemariasosa/rubik#2-the-rkconcat_to_list-function) que agrupa los objetos de múltiples columnas en una sola lista.

```python
    def modificar_atributos(self, productos):
        atributos = ['talla', 'color']
        for atributo in atributos:
            new_names = {atributo: 'value'}
            productos = productos.rename(columns=new_names)
            productos['name'] = atributo
            productos = rk.groupto_dict(productos, ['name', 'value'], atributo)
        productos = rk.concat_to_list(productos, atributos, 'attributes')
        return productos
```

El paso 3 nos permite darle la estructura adecuada a los precios mediante la función **modificar_precios()**. Lo primero es actualizar el nombre de la columna de precios. Después, el método **formato_precio()**, nos ayuda a estandarizar los precios, eliminando caracteres innecesarios. Al final, el número se convierte en un string con 2 decimales.

```python
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
```

El paso 4 es el último método de nuestra clase: **agrupando_variantes()**. Para este paso se utiliza la función de [rubik **groupto_list()**](https://github.com/josemariasosa/rubik#5-the-rkgroupto_list-function). Esta función nos permite agrupar todas las líneas de nuestro DataFrame original, en función de la información del producto y sus variantes, para reducirla únicamente a los 3 productos principales, con la información de las variantes en una lista.

```python
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
```

Por último, la tabla resultante se convierte en formato JSON y se exporta la información.

```python
    productos = productos.to_dict(orient='records')
    with open('data/productos.json', 'w') as f:
        json.dump(productos, f)
```

En conclusión, pandas nos facilita el trabajo para cambiar la estructura original de nuestra información con el fin de empatarla con otra estructura nueva. Sin importar que la estructura final no sea necesariamente una tabla, como pudimos observar en este ejemplo.

Rubik permitió reducir la cantidad de código necesario para hacer operaciones complejas como agrupar los productos. Por favor, siéntete libre de trabajar con rubik y experimentar con todas las funciones.

### 5.2. Agrupación de información (groupby).

Pandas nos permite agrupar información con el objetivo de llevar a cabo cálculos simples, o aplicar cualquier función de python, con los elementos que pertenecen a cada grupo. Una manera muy similar con lo que ocurre con las [tablas dinámicas de Excel](https://support.office.com/es-es/article/informaci%C3%B3n-general-sobre-tablas-din%C3%A1micas-y-gr%C3%A1ficos-din%C3%A1micos-527c8fa3-02c0-445a-a2db-7794676bce96).

Existe una infinidad de posibilidades para trabajar con la función de [pandas **groupby()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html). Para encontrar información detallada revisar la [guía de pandas para groupby](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html).

En esta sección realizaremos un ejemplo que nos permita visualizar dos casos, agrupar valores de un DataFrame para posteriormente aplicar una función:

1. Predefinida (simple).
2. Customizada (cualquier función que se defina en python).

#### Caso de uso: Estudio de las emergencias.

Partiendo de los datos del archivo [**declaratorias_emergencia_desastre.csv**](https://github.com/josemariasosa/pycon-2019/blob/master/data/declaratorias_emergencia_desastre.csv), todo el código de esta sección se encuentra en el archivo [**5-2-groupby.py**](https://github.com/josemariasosa/pycon-2019/blob/master/pyFiles/5-2-groupby.py).

Con el fin de aplicar una **función predefinida**, nos haremos las siguientes preguntas:

##### I. ¿Cuál es el promedio de la magnitud de los sismos por estado?

El método **mean()** en el contexto de groupby, nos permite calcular el promedio de los sismos por estado.

```python
tabla_1 = (tabla.groupby('estado')['magniud_sismo']
                .mean()
                .rename('magnitud_promedio')
                .reset_index(drop=False))
```

##### II. ¿En cuántas ciudades se registraron los sismos del estado?

El método **size()** en el contexto de groupby, nos permite calcular el total de registros por estado.

```python
tabla_2 = (tabla.groupby('estado')
                .size()
                .rename('registros_por_estado')
                .reset_index(drop=False))
```

Es posible realizar las dos operaciones anteriores, en una misma tabla con la función de [pandas **agg()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.agg.html).

```python
tabla_3 = (tabla.groupby('estado')['magniud_sismo']
                .agg(['mean', 'size'])
                .reset_index(drop=False))
```

Para aplicar una **función customizada**, nos haremos las siguientes preguntas:

##### III. ¿Cuántas fechas distintas se tienen registradas por estado?

Es importante recalcar en esta sección que debido a que la selección de columnas para trabajar es solo una, en este caso `fecha_evento`, entonces el argumento de la función es una [pandas **Series**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html).

```python
calcular_fechas_unicas = lambda x: len(set(x.tolist()))
tabla_4 = (tabla.groupby('estado')['fecha_evento']
                .apply(calcular_fechas_unicas)
                .rename('fechas_unicas')
                .reset_index(drop=False))
```

##### IV. ¿Cuál es el promedio de la magnitud de los sismos registrados por fecha en cada estado?

El cálculo es notoriamente más complejo, por lo que se definió una nueva función en python. Al contrario del ejemplo anterior, cuando se selecciónan múltiples columnas para trabajar, en este caso `magniud_sismo` y `fecha_evento`, el argumento que recibe la función es un DataFrame.

```python
def promedio_magnitud(df):
    df = rk.groupto_list(df, ['fecha_evento'], 'magniud_sismo')
    df['magniud_sismo'] = df['magniud_sismo'].map(mean)
    return df
tabla_5 = (tabla.groupby('estado')['magniud_sismo', 'fecha_evento']
                .apply(promedio_magnitud)
                .reset_index(drop=False)
                .drop('level_1', axis=1))
```

### 5.3. Uniendo múltiples fuentes de información (merge).

Para esta sección vamos a trabajar con la información de las gasolineras obtenidas de los dos archivos: [**places.xml**](https://github.com/josemariasosa/pycon-2019/blob/master/data/places.xml) y [**prices.xml**](https://github.com/josemariasosa/pycon-2019/blob/master/data/prices.xml), importados en la sección [**2.4. Importar XML**](https://github.com/josemariasosa/pycon-2019#24-importar-xml).

El verdadero valor de estos 2 archivos se obtiene al unir la información de las estaciones de gas y el precio de la gasolina. Recordemos que después de importar y transformar la información de los archivos de las gasolineras y los precios las tablas lucen de la siguiente manera:

```python
print('Tabla de precios: ')
print(precios.head())
# Tabla de precios:
#   place_id                                                gas
# 0    11703  [{'tipo': 'regular', 'precio': '20.49'}, {'tip...
# 1    11702  [{'tipo': 'regular', 'precio': '19.69'}, {'tip...
# 2    11701  [{'tipo': 'regular', 'precio': '14.49'}, {'tip...
# 3    11700  [{'tipo': 'regular', 'precio': '18.56'}, {'tip...
# 4    11699            [{'tipo': 'premium', 'precio': '20.5'}]

print('\nTabla de estaciones: ')
print(estaciones.head())
# Tabla de estaciones:
#   place_id                                           estacion
# 0     2039  {'nombre': 'ESTACION DE SERVICIO CALAFIA, S.A....
# 1     2040  {'nombre': 'DIGEPE, S.A. DE C.V. (07356)', 'cr...
# 2     2041  {'nombre': 'DIAZ GAS, S.A. DE C.V.', 'cre_id':...
# 3     2042  {'nombre': 'COMBU-EXPRESS, S.A. DE C.V.', 'cre...
# 4     2043  {'nombre': 'PETROMAX, S.A. DE C.V.', 'cre_id':...
```

Podemos observar que tenemos una columna que funciona como pivote llamada `place_id`. La demás información está anidada en la columna de `gas`, como una lista de diccionarios que almacenan el `precio` y el `tipo` de gasolina. Y en la columna de `estacion`, que almacena como un diccionario toda la información de la gasolinera.

El archivo [**5-3-merge.py**](https://github.com/josemariasosa/pycon-2019/blob/master/pyFiles/5-3-merge.py) contendrá todo el código de esta sección. Para poder unir la información de las dos fuentes, vamos a integrar las funciones del archivo [**2-4-import-xml.py**](https://github.com/josemariasosa/pycon-2019/blob/master/pyFiles/2-4-import-xml.py), para integrarlas en una clase nueva **UnirGasolinaPrecio**. Dicha clase cuenta con un método llamado **main()** que corre los siguientes pasos:

- **Paso 1**: Importar y dar formato a los precios.
- **Paso 2**: Importar y dar formato a las estaciones.
- **Paso 3**: Llevar a cabo la unión de los precios y las estaciones.
- **Paso 4**: Filtrar las estaciones sin ningún precio.

La función **main()** de la clase **UnirGasolinaPrecio**, luce así:

```python
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
```

Vamos a darle formato a cada una de las tablas importadas. Comenzemos por darle formato a los precios. Para esto, utilizaremos la función de [rubik **ungroup_list()**](https://github.com/josemariasosa/rubik#3-the-rkungroup_list-function), con el fin de separar los tipos de gas en cada fila del DataFrame. Posteriormente, mediante la función de [rubik **ungroup_dict()**](https://github.com/josemariasosa/rubik#4-the-rkungroup_dict-function) se separan en 2 columnas el precio y el tipo de gasolina.

Por último, la función de [pandas **pivot_table()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html
) nos permite convertir la columna de `tipo` de gasolina en múltiples columnas que desplieguen el precio de la misma.

```python
    def formato_precios(self, precios):
        precios = rk.ungroup_list(precios, 'gas')
        precios = rk.ungroup_dict(precios, 'gas')
        precios['precio'] = precios['precio'].astype(float)
        precios = precios.pivot_table('precio', ['place_id'], 'tipo')
        precios = precios.reset_index(drop=False)
        return precios
```

Ahora es el turno de darle formato al DataFrame de estaciones. Aplicamos dos veces la función de [rubik **ungroup_dict()**](https://github.com/josemariasosa/rubik#4-the-rkungroup_dict-function) para desanidar los diccionarios que contienen la info de la estación y de las coordenadas de las gasolineras.

```python
    def formato_estaciones(self, estaciones):
        estaciones = rk.ungroup_dict(estaciones, 'estacion')
        estaciones = rk.ungroup_dict(estaciones, 'location')
        new_names = {'x': 'coord_x', 'y': 'coord_y'}
        return estaciones.rename(columns=new_names)
```

Para poder unir los dos DataFrames, hay que asegurarnos de definir lo siguiente:

1. Establecer la columna pivote, la cual se indica en el argumento **by** de la función de [pandas **merge()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html). Es importante asegurarse que las columnas tienen el mismo formato y tipo de dato.
2. Definir el método de unión, el cual se indica en el argumento de **how**. Personalmente, el 99% de las ocasiones utilizo el método: **left**.

Por último, para poder conocer las estaciones en la tabla que no tienen registro alguno de precio para ningún tipo de gasolina, utilizamos una máscara que nos permita filtrar cuando en las tres columnas existan valores nulos, mediante el método de [pandas **isnull()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isnull.html).

## Fuentes:

- https://github.com/josemariasosa/rubik
- https://pbpython.com/pandas_dtypes.html
- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dtypes.html
- https://www.geeksforgeeks.org/python-pandas-dataframe-ffill/
