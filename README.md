# Automatizando el análisis y procesamiento de datos con pandas.

## Contenido de la presentación

- 1. Introducción a pandas
    - 1.1. Qué es pandas.
    - 1.2. Cómo instalar pandas.
    - 1.3. Dónde está la documentación oficial.

- 2. Importar datos utilizando pandas
    - 2.1. Importar y exportar JSON.
    - 2.2. Importar y exportar CSV.
    - 2.3. Importar EXCEL.
    - 2.4. Importar XML.

- 3. Conociendo nuestros datos
    - 3.1. Head, tail & info.
    - 3.2. Fechas y tipos de datos.
    - 3.3. Valores faltantes.

- 4. Introducción a rubik para Python

- 5. Casos de uso de pandas
    - 4.1. Transformar la estructura de la información.
    - 4.2. Extracción de información específica.
    - 4.3. Agrupar la información.

---

## 1. Introducción a pandas

### 1.1. Qué es pandas.

Consultado el [sitio oficial](https://pandas.pydata.org/), pandas es un conjunto de herramientas para estructurar, manipular y analizar datos mediante el lenguaje de programación Python. Permite estructurar la información de manera tabular mediante el uso de tablas conocidas como **DataFrames**.

Pandas es de código abierto y puede ser utilizado de manera gratuita bajo la [licencia BSD](https://en.wikipedia.org/wiki/BSD_licenses).

### 1.2. Cómo instalar pandas.

Instalar pandas puede resultar un poco enredos para usuarios inexpertos. La manera más simple de instalar pandas, junto con un listado de las librerías más populares, es a través de [Anaconda](https://www.anaconda.com/distribution/). También, si se desea tener más control sobre los paquetes o se tiene una conexión de internet limitada, existe una versión más reducida conocida como [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

También se puede instalar directamente desde la terminal, utilizando el administrador de paquetes de Python pip.

```bash
pip install pandas
```

Toda la información para la [instalación de pandas](https://pandas.pydata.org/pandas-docs/stable/install.html) se encuentra aquí.

### 1.3. Dónde está la documentación oficial.

La documentación oficial de pandas se encuentra disponible en inglés siguiendo la liga:

https://pandas.pydata.org/pandas-docs/stable/

## 2. Importar datos utilizando pandas

### 2.1. Importar y exportar JSON.

Para poder trabajar con archivos tipo JSON, hay que utilizar la función de la librería base [json **load()**](https://docs.python.org/3/library/json.html#basic-usage). El código se encuentra en el archivo **2-1-import-json.py**.

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

Para llevar a cabo el proceso inverso, y convertir un DataFrame a un formato JSON se utiliza el método de [pandas **to_dict(orient='records')**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html).

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

El código se encuentra en el archivo **2-2-import-csv.py**.

```python
import pandas as pd

filename = 'data/declaratorias_emergencia_desastre.csv'
tabla = pd.read_csv(filename, encoding='utf-8')

print(tabla.head())
```

Para exportar un DataFrame se utiliza la función de [pandas **to_csv()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html) como se muestra a continuación.

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

Descargamos, de la página oficial de [datos de gobierno](https://datos.gob.mx/busca/dataset/estaciones-de-servicio-gasolineras-y-precios-finales-de-gasolina-y-diesel), los archivos: **places.xml** y **prices.xml**. Para poder convertir la información contenida en los archivos a un DataFrame, no existe una manera directa de hacerlo. Sin embargo, Python nos permite procesar la información previamente para luego presentarla de manera tabular.

El código de esta sección se encuentra en el archivo **2-4-import-xml.py**.

El objeto base [**xml.etree.ElementTree()**](https://docs.python.org/2/library/xml.etree.elementtree.html) nos permite cargar un archivo xml, pero **requiere forzosamente** pasar por un proceso previo para poderlo convertir a una tabla. El siguiente código puede servir de apoyo para extraer la información necesaria de un xml.

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

Antes de realizar algún análisis o cualquier movimiento de la información hay que estar seguro de conocer a fondo nuestra información.

### 3.1. Head, tail & info.

Son los tres principales métodos para visualizar de manera preeliminar la información contenida dentro de un DataFrame.

La función de [pandas **head()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html) regresa las primeras n filas de una tabla. Es útil para comprobar que nuestro objeto contiene los tipos de datos correctos.

```python
df = pd.DataFrame({'animal':['alligator', 'bee', 'falcon', 'lion',
                  'monkey', 'parrot', 'shark', 'whale', 'zebra']})
df
#       animal
# 0  alligator
# 1        bee
# 2     falcon
# 3       lion
# 4     monkey
# 5     parrot
# 6      shark
# 7      whale
# 8      zebra

df.head()
#       animal
# 0  alligator
# 1        bee
# 2     falcon
# 3       lion
# 4     monkey
```

La función de [pandas **tail()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.tail.html) regresa las últimas n filas de una tabla. Es útil para verificar los datos después de haber sido ordenardos o al insertar (append) filas.

```python
df = pd.DataFrame({'animal':['alligator', 'bee', 'falcon', 'lion',
                  'monkey', 'parrot', 'shark', 'whale', 'zebra']})
df
#       animal
# 0  alligator
# 1        bee
# 2     falcon
# 3       lion
# 4     monkey
# 5     parrot
# 6      shark
# 7      whale
# 8      zebra

df.tail(3)
#    animal
# 4  monkey
# 5  parrot
# 6   shark
```

La función de [pandas **info()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html) imprime información acerca del DataFrame, incluyendo el [tipo de dato (dtype)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dtypes.html) de los índices y las columnas, los valores nulos y el uso de memoria.

```python
df
#    int_col text_col  float_col
# 0        1    alpha       0.00
# 1        2     beta       0.25
# 2        3    gamma       0.50
# 3        4    delta       0.75
# 4        5  epsilon       1.00

df.info()
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

Lo primero que debemos revisar, cuando comenzamos a trabajar con datos, son los [tipos de datos (dtype)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dtypes.html) con los que estamos trabajado. Es importante asegurarnos de estar utilizando el tipo de dato correcto, porque este es uno de esos puntos que se nos olvida revisar hasta que se genera un error o algún otro resultado inesperado.
 
Los tipos de datos de las columnas en pandas se conoce como **dtypes**. Los dtypes se enlistan a continuación: 

- object
- int64
- float64
- datetime64
- bool

Trabajando con la información cargada en la sección **2.1. Importar y exportar JSON**, nos aseguraremos de contar con los tipos de datos correcto. El código completo de esta sección se encuentra en **3-2-dtypes.py**.

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

Si queremos conocer los tipos de datos de un DataFrame, utilizamos el atributo de [pandas dtypes](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dtypes.html):

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

Otra opción es utilizando la función de [pandas **map()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html), para aplicar una función en **cada uno de los elementos** de una columna. La opción más directa sería:

```python
tabla['probabilityofprecip'] = tabla['probabilityofprecip'].map(int)
```

Esta sintaxis funciona de manera similar a **astype()**. Sin embargo, quizá querramos utilizar funciones más complicadas, como por ejemplo: convertir las columnas `latitud` y `longitud` en valores flotantes, conservando únicamente los valores redondeados hasta 3 decimales. 

Podemos utilizar una función lambda, que llamaremos **aux_fun()**, que convierta a tipo float y luego redondeé el valor a 3 decimales. Al final, podemos utilizar una variable auxiliar `select` para filtrar las columnas del DataFrame.

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

Para el siguiente caso, podríamos llevar a cabo la estandarización de un string, para interpretar correctamente su valor numérico, declarando una función en Python.

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

Es común que la fecha se almacene como string, si se desean utilizar las propiedades de las fechas, hay que convertir la columna a formato **datetime**. Una de las maneras de llevar a cabo esto es a través de la función de [pandas to_datetime()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html).

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

El dtype cambió a datetime64[ns]. Recomiendo revisar la [información completa](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior) de los formatos de fecha en Python, pero los formatos más comunes son: `"%d-%m-%Y"`, `"%d/%m/%Y"` y `"%m-%y"`; donde:

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

Para esta sección trabajaremos con el dataframe que importamos en la sección 2.2. Importar CSV, sobre las declaraciones de emergencia y desastres. El código de esta sección puede ser consultado en 3-3-nan.py. Cuando se imprimen los valores ausentes dentro de un data frame aparecen como NaN. 

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

También la función info() nos permite visualizar cuántos valores de la columna son faltantes. Para el caso de la columna `declaratoria_emergencia_ordinaria`, únicamente se cuenta con 75 objetos no nulos.

Es importante mencionar que cuando una **columna de valores enteros** cuenta con un valor faltante, automáticamente la lista se convierte del tipo flotante.

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

Es muy importante definir una estratégia sobre cómo se manejarán los valores ausentes. Las principales maneras de hacerlo son 3:

- Eliminar las muestras con valores faltantes.
- Establecer un valor que tendrán todos los valores faltantes.
- Cálculo de un valor.

Revisaremos a detalle cada una de ellas.

#### 3.3.1. Eliminar las muestras con valores faltantes.

Las cuatro columnas que tienen valores faltantes son:

```
# declaratoria_emergencia_ordinaria         75 non-null object
# declaratoria_emergencia_extraordinaria    325 non-null object
# declaratoria_desastre                     699 non-null object
# magniud_sismo                             722 non-null float64
```

Vamos a eliminar todas las muestras en donde se tenga algún valor faltante. La función dropna() nos permite eliminar las filas, o muestras, donde al menos uno de los valores esté ausente.

```python
tabla = tabla.dropna()
print(tabla.info())
# Empty DataFrame
# Columns: [estado, municipio, clave_inegi, declaratoria_emergencia_ordinaria, declaratoria_emergencia_extraordinaria, declaratoria_desastre, magniud_sismo, fecha_evento]
# Index: []
```

Podemos encontrar que el resultado es una tabla vacío, pues entro de todas las filas hay valores faltantes, entonces nos resulta poco útil abordar los valores faltantes bajo esta regla. Entonces lo que haremos es eliminar todas las observaciones únicamente en donde `magniud_sismo` se encuentre ausente.

Cuando queremos eliminar, de una sola columna, los valores ausentes, tenemos que crear una máscara que nos permita filtrar los valores correspondientes, en este caso los que son faltantes, mediante el método isnull(). Posteriormente, el símbolo `~` nos permite invertir los valores booleanos, debido a que si son nulos son True.

Por último, reset_index(drop=True) vuelve a establecer el orden del índice. Si se le indica drop=False, entonces los índices actuales se convierten en una columna más del dataframe. Aprender más sobre [reset_index](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html).

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

También existen casos en donde lo mejor es definir un valor arbitrario que sustituya los valores faltantes. Es común que se utilice el 0 para todas las muestras faltantes. Hay que asegurarnos que el valor que estamos definiendo sea consistente con las mediciones. En otras ocasiones, conviene utilizar un valor M, que representaría una muestra con un valor muy alto, o muy bajo. 

Por último, también es común definir los valores faltantes como strings. Para este ejemplo, continuaremos con los valores faltantes del ejemplo anterior, y para las siguientes tres columnas `declaratoria_emergencia_ordinaria`, `declaratoria_emergencia_extraordinaria` y `declaratoria_desastre` cambiaremos los valores faltantes por el string de **no-aplica**.

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

Para cada una de las columnas, se corre el método de fillna(), rellenando los valores faltantes con el valor asignado, en este caso un string.

En algunos casos en necesario completar los valores faltantes con una lista vacía. Existen múltiples maneras de hacer esto, pero presentaremos una de las funciones de rubik que nos permitirá hacer esto de manera rápida. Como se muestra en las siguientes tablas.

De la tabla original:

| Entry | Id        | Roles     |
|-------|-----------|-----------|
| 0     | user-123  | NaN       |
| 1     | user-452  | [1]       |
| 2     | user-21   | [5, 2]    |
| 3     | user-621  | NaN       |
| 4     | user-5512 | [3, 4]    |
| 5     | user-25   | [1, 2, 3] |

Obtener la siguiente tabla:

| Entry | Id        | Roles     |
|-------|-----------|-----------|
| 0     | user-123  | [ ]       |
| 1     | user-452  | [1]       |
| 2     | user-21   | [5, 2]    |
| 3     | user-621  | [ ]       |
| 4     | user-5512 | [3, 4]    |
| 5     | user-25   | [1, 2, 3] |

```python
new = rk.fillna_empty_list(original, 'Roles')
```

#### 3.3.3. Cálculo de un valor.

Por último, es común que también que se utilicen cálculos más complejos para el llenado de los valores faltantes, como por ejemplo utilizar alguna medida de tendencia central, como la media, mediana o moda. O por ejemplo, calcular la media de la familia a la que pertenece y utilizarla.

En nuestro ejemplo tenemos varias mediciones de la `magniud_sismo` que no se cuentan. Para poder obtener el valor de dichas se puede utilizar un aproximado, como por ejemplo el promedio de la magniud_sismo por estado. Podemos agrupar los valores y sacar la media para utilizarla posteriormente en los valores faltantes.

```python
mask = tabla['magniud_sismo'].isnull()
tabla = tabla[mask].reset_index(drop=True)

print(tabla)
#      estado           municipio  clave_inegi  \
# 0   Chiapas              Oxchuc         7064
# 1    Oaxaca  San Antonio Acutla        20106
# 2  Tlaxcala             Totolac        29036

#   declaratoria_emergencia_ordinaria declaratoria_emergencia_extraordinaria  \
# 0                               NaN                                     sí
# 1                                sí                                    NaN
# 2                               NaN                                    NaN

#   declaratoria_desastre  magniud_sismo fecha_evento
# 0                    sí            NaN   2017-09-07
# 1                    sí            NaN   2017-09-19
# 2                    sí            NaN   2017-09-19
```

Contamos con 3 estados con magnitudes faltantes, que podemos utilizar el promedio por estado.

```python
promedio_estado = tabla.groupby(['estado'])['magniud_sismo'].mean()

print(promedio_estado)
# estado
# CIudad de México                   7.100000
# Chiapas                            8.200000
# Guerrero                           7.100000
# Morelos                            7.100000
# México                             7.100000
# Oaxaca                             7.973973
# Puebla                             7.100000
# Tlaxcala                           7.100000
# Veracruz de Ignacio de la Llave    8.200000
# Name: magniud_sismo, dtype: float64
```

En este punto aplican las funciones dataframe.bfill() y dataframe.ffill() que nos permiten llenar hacia atrás (backward fill) o hacia adelante (forward fill) los valores NaN presentes en un data frame. Es muy común el uso de ffill() cuando los espacios en blanco significa que se debe de utilizar el último valor que se prenta.

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

    - 3.4. Niveles de agregación y validez estadística.
        - Muestra vs población.

## 4. Introducción a Rubik

### 4.1. Introducción

Rubik es un módulo de Python con un listado de funciones para trabajar con Pandas.

La documentación completa de rubik, con algunos ejemplos, puede ser encontrada en:

https://github.com/josemariasosa/rubik

### 4.2. Instalación

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

## 5. Casos de uso de Pandas

### 5.1. Transformar la estructura de la información.

Es muy común llevar a cabo transformaciones en la estructura de la información, sobre todo en los siguientes casos:

- Eficientar una base de datos.
- Limpieza y pre-procesamiento de información.
- Compartir datos con un tercero que solicita una estructura definida.
- Recibir datos de un tercero para almacenarnos siguiendo nuestra estructura.

Vamos a desarrollar un ejemplo en donde vamos a transformar la estructura de un listado de productos para poderla subir a un supuesto sitio de e-commerce.

#### Caso de uso: Automatizando la venta en línea

Contamos con un archivo en formato csv que almacena la información de un listado de productos. Para poder subir la información de nuestros productos a un sitio de e-commerce que se encargará de publicar nuestros productos en línea, debemos de envíar un archivo JSON con la siguiente estructura:

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

- **product_name** - Un string que representa el nombre del producto.
- **part_number** - Un string único por producto, ejemplos: SKU, UPC, GTIN.
- **brand** - Un string con la marca o vendedor del producto.
- **variants** - Una lista que a su vez contiene la información detallada de cada una de las variantes del producto. Para dar de alta una variante, se necesita crear un objeto por cada una con la siguiente información:
    - **price** - Un string con 2 decimales del precio.
    - **currency** - Un string indicando la moneda, ejemplos: USD, CAD, MXN.
    - **stock** - Un string con la cantidad del producto en stock.
    - **image** - Un diccionario que indique cuál es la imagen principal, y las imágenes secundarias, con la siguiente estructura.
        - **main** - Un string con el url donde está hosteada la imagen.
        - **images_list** - Una lista de strings con los urls de las imágenes secundarias. Si no hay imágenes entonces dejar la lista vacía.
    - **attributes** - Un listado de atributos, donde cada atributo cuenta con la siguiente información:
        - **name** - El nombre del atributo.
        - **value** - El valor del atributo.

Nuestro objetivo es realizar un script en Python que nos permita generar esta estructura de manera automatizada. La estructura con la que se cuenta ahora está en el archivo de productos. Todo el código que se mostrará a continuación se encuentra en el archivo 5-1-products.py.

Vamos a generar una clase con el nombre **TransformarEstructura** que contenga un método llamado main(). El método main() cuenta con 6 pasos que irán transformando poco a poco la tabla original de productos, la cual se importó con el nombre de `productos`, a la estructura deseada.

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

Para el primer paso, el método importar_productos(), importa el archivo csv de la misma manera que en la sección de importar un csv. A partir de ahí, se pone más interesante. El método modificar_imagenes(), primero modifica el nombre de la columnas y completa los valores faltantes con un string vacío.

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

Aquí vamos a utilizar el método de rubik concat_to_list() para concatenar en una misma lista las columnas de imágenes secundarias en una sola, posteriormente aplicaremos el método de nuestra clase formato_imagen() para eliminar las imágenes faltantes. Por último, el método de rubik groupto_dict() nos permite agrupar múltiples columnas en una sola como diccionario.

El paso 2, modificar_atributos(), genera primero la estructura de los atributos con name y value y luego aplica el método de rubik concat_to_list() que agrupa los objetos de múltiples columnas en una sola lista.

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

El paso 3 es modificar_precios(). Lo primero es actualizar el nombre de la columna de precios. Después, el método formato_precio() de nuestra clase, nos ayuda a estandarizar los precios, eliminando caracteres innecesarios. Al final, el número se convierte en un string con dos decimales.

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

El paso 4 es el último método de nuestra clase, agrupando_variantes(). Para este paso se utiliza otra función de rubik que tiene una funcionalidad muy interesante. Para revisar más sobre la función groupto_list() de rubik, revisar la documentación. Para nuestros datos, esta función nos permite agrupar todas las líneas de nuestra tabala original, en función de la información del producto y sus variantes, para reducirla únicamente a los 3 productos principales, con la información de las variantes en una lista.

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

En conclusión, Pandas nos facilita el trabajo para cambiar la estructura original de nuestra información con el fin de empatarla con otra estructura nueva. Sin importar que la estructura final no sea necesariamente una tabla, como pudimos observar en este ejmplo.

Rubik además permitió reducir la cantidad de código necesario para hacer operaciones complejas como agrupar los productos. Por favor, siéntete libre de trabajar con rubik y experimentar con todas las funciones que aparecen en la documentación de rubik.

### 5.2. Agrupación de información (groupby).

Pandas nos permite agrupar información con el objetivo de llevar a cabo cálculos, o cualquier función customizada, con los valores que pertenecen a cierto grupo. Una manera muy similar con lo que ocurre con las [tablas dinámicas de Excel](https://support.office.com/es-es/article/informaci%C3%B3n-general-sobre-tablas-din%C3%A1micas-y-gr%C3%A1ficos-din%C3%A1micos-527c8fa3-02c0-445a-a2db-7794676bce96).

Existe una infinidad de posibilidades para trabajar con la función de pandas groupby(). En esta sección realizaremos un ejemplo que nos permita visualizar dos casos, agrupar valores en una tabla y aplicar una función:

1. Predefinida (simple).
2. Customizada (cualquier función que se defina en Python).

#### Caso de uso: Estudio de las emergencias.

Partiendo de los datos en el archivo `declaratorias_emergencia_desastre.csv`, todo el código de esta sección se encuentra en el archivo 5-2-groupby.py.

Con el fin de aplicar una función predefinida, nos haremos las siguientes preguntas:

- 1.1. Cuál es el promedio de la magnitud de los sismos por estado.
- 1.2. En cuántas ciudades se registraron los sismos del estado.

Para aplicar una función customizada, nos haremos la siguiente pregunta:

- 2.1. Cuántas fechas distintas se tienen registradas por estado.
- 2.2. Cuál es el promedio de la magnitud de los sismos registrados por fecha en cada estado.

### 5.3. Uniendo múltiples fuentes de información (merge).

Con la información de las gasolineras obtenidas de los dos archivos: places.xml y prices.xml, importada en la sección 2.4. Importar XML. 

El verdadero valor de los archivos se obtiene al unir la información de las gasolineras con el precio y los productos (gasolina y diésel) que tienen a la venta.

Recordemos que después de importar y transformar la información de los archivos de las gasolineras y los precios las tablas lucen de la siguiente manera:

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

Podemos observar que tenemos una columna que funciona como pivote llamada place_id. La demás información está anidada en la columna de `gas` como una lista de diccionarios que almacenan el `precio` y el `tipo` de gasolina. Y en la columna de `estacion`, que almacena como un diccionario toda la información de la gasolinera.

El archivo 5-3-merge.py contendrá todo el código de esta sección. Para poder unir la información de las dos fuentes, vamos a tomar las funciones que utilizamos en la sección 2.4. Importar XML, para integrarlas en una clase que se va a llamar UnirGasolinaPrecio(). Dicha clase cuenta con un método llamado main() que corre los siguientes pasos:

- Paso 1: Importar y dar formato a los precios.
- Paso 2: Importar y dar formato a las estaciones.
- Paso 3: Llevar a cabo la unión de los precios y las estaciones.
- Paso 4: Filtrar las estaciones sin ningún precio.

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

Después de importar los precios en versión xml, vamos a darle formato. Lo primero que hacemos es la función de rubik ungroup_list(), con el fin de separar los tipos de casolina en cada fila del DataFrame. Posteriormente, mediante la función de rubik ungroup_dict() se separan en 2 columnas el precio y el tipo de gasolina.

Por último, la función nativa de [pandas pivot_table()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html
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

Posteriormente, después de importar las estaciones aplicamos dos veces la función de rubik ungroup_dict() para desanidar los diccionarios que contienen la info de la estación y de las coordenadas de las gasolineras.

```python
    def formato_estaciones(self, estaciones):
        estaciones = rk.ungroup_dict(estaciones, 'estacion')
        estaciones = rk.ungroup_dict(estaciones, 'location')
        new_names = {'x': 'coord_x', 'y': 'coord_y'}
        return estaciones.rename(columns=new_names)
```

Para el paso 3, lo primero que se recomienda antes de llevar a cabo la unión de dos o más DataFrames es:
1. Establecer la columna pivote, la cual se indica en el argumento by. Es importante asegurarse que las columnas tienen el mismo formato y tipo de dato.
2. Definir el método de unión, el cual se indica en el argumento de how. Personalmente, el 99% de las ocasiones utilizo left.

Ver más sobre pandas merge().

Por último, para poder conocer las estaciones en la tabla que no tienen registro alguno de precio para ningún tipo de gasolina, utilizamos una máscara que nos permita filtrar cuando en las tres columnas existan valores nulos, mediante el método de pandas isnull().

## 6. Seguimiento




Extraer información necesaria (eg. información estadística).
Agrupar información (eg. tablas dinámicas y groupby).


- 1. Modificar la estructura inicial de nuestros datos. Ejemplo: vamos a suponer que tenemos información sobre productos y los queremos publicarla en Shopify, Mercadolibre, Ebay, o cualquier otro Marketplace. En este ejemplo aprenderemos a reorganizar la información para homologarla con el formato de un tercero. Compartiré un conjunto de herramientas, y trucos, que permiten la fácil reestructuración de los datos.

2. Extraer información específica de los datos. Ejemplo: Cómo estandarizar la generación de un reporte de ventas que extraiga de todas las ventas individuales, el consolidado por cada canal de venta.

3. Realizar operaciones más complicadas de agrupación. Ejemplo: Cómo hacer cualquier tipo de tabla dinámica de Excel utilizando Pandas.
Por último, revisaremos algunos de los principios de automatización. Por qué Python es una excelente herramienta para eliminar la cantidad de trabajo repetitivo. Revisaremos algunas ideas sobre qué hacer una vez teniendo la información procesada y analizada:

- Exportar los archivos.
- Enviar la información por mail.
- Actualizar la información en una Spread Sheet compartida por el equipo de trabajo.
- Visualizar los resultados utilizando Data Studio de Google.
- Subir los cambios a una base de datos.








fuentes:
https://pbpython.com/pandas_dtypes.html
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dtypes.html
https://www.geeksforgeeks.org/python-pandas-dataframe-ffill/









Comenzaremos con una introducción general a la librería de Pandas utilizando la interfaz de Jupyter. Revisaremos, utilizando analogías, qué son los Data Frames, y cómo éstos almacenan y despliegan la información.

Posteriormente, revisaremos múltiples formatos en los que se pueden encontrar los datos (json, xml, csv) almacenados. Aprenderemos cómo cargar y manipular cualquier formato en Pandas, descargando un par de datasets de la página de datos abiertos de gobierno.

Durante la plática, aprenderemos a contestar las siguientes preguntas:

- ¿Qué nivel de agregación tienen nuestros datos?
- ¿Cuáles son los tipos de datos que tenemos en nuestro Data Frame?
- ¿Cómo modificar los tipos de datos?
- ¿Qué podemos hacer con los valores faltantes y NAs?
Aprovecharemos la mayor parte del tiempo de la plática para realizar 3 ejemplos prácticos, que nos permitirán comprender a grandes rasgos las ventajas de Pandas:

1. Modificar la estructura inicial de nuestros datos. Ejemplo: vamos a suponer que tenemos información sobre productos y los queremos publicarla en Shopify, Mercadolibre, Ebay, o cualquier otro Marketplace. En este ejemplo aprenderemos a reorganizar la información para homologarla con el formato de un tercero. Compartiré un conjunto de herramientas, y trucos, que permiten la fácil reestructuración de los datos.

2. Extraer información específica de los datos. Ejemplo: Cómo estandarizar la generación de un reporte de ventas que extraiga de todas las ventas individuales, el consolidado por cada canal de venta.

3. Realizar operaciones más complicadas de agrupación. Ejemplo: Cómo hacer cualquier tipo de tabla dinámica de Excel utilizando Pandas.
Por último, revisaremos algunos de los principios de automatización. Por qué Python es una excelente herramienta para eliminar la cantidad de trabajo repetitivo. Revisaremos algunas ideas sobre qué hacer una vez teniendo la información procesada y analizada:

- Exportar los archivos.
- Enviar la información por mail.
- Actualizar la información en una Spread Sheet compartida por el equipo de trabajo.
- Visualizar los resultados utilizando Data Studio de Google.
- Subir los cambios a una base de datos.
Tabla de contenido:

Introducción. (5 minutos)

Sobre mí.
Qué es Pandas.
Qué es un Data Frame.
Tipos de archivos y cómo importarlos en Python. (3 minutos)

Json
XML
CSV
Excel
Conociendo nuestra información. (3 minutos)

Niveles de agregación de la información
Validez estadística: muestra o población
Tipos de datos
Valores faltantes.
Procesamiento de información. (15 minutos)

Convertir información (eg. transformar el formato de la información).
Extraer información necesaria (eg. información estadística).
Agrupar información (eg. tablas dinámicas y groupby).
Automatización, seguimiento y cierre. (9 minutos)

Qué hacer con la información.
Exportar un archivo.
Almacenar en otra base de datos.
Enviar el reporte por mail.
Actualizar un Spread Sheet de Google.