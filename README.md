# Automatizando el análisis y procesamiento de datos con Pandas.

## Contenido de la presentación

- 1. Introducción a Pandas

    - 1.1. Qué es Pandas.
    - 1.2. Cómo instalar Pandas.
    - 1.3. Dónde está la documentación oficial.
    - 1.4. Qué es un DataFrame.
        - Comparación contra un JSON.

- 2. Importar datos utilizando Pandas

    - 2.1. Importar JSON.
    - 2.2. Importar CSV.
    - 2.3. Importar EXCEL.
    - 2.4. Importar XML.

- 3. Conociendo nuestros datos

    - 3.1. Head, tail & info.
    - 3.2. Fechas y tipos de datos.
    - 3.3. Valores faltantes.
    - 3.4. Niveles de agregación y validez estadística.
        - Muestra vs población.

- 4. Casos de uso de Pandas

    - 4.1. Transformar la estructura de la información.
    - 4.2. Extracción de información específica.
    - 4.3. Agrupar la información.

- 5. Seguimiento

---

## 1. Introducción a Pandas

### 1.1. Qué es Pandas.

Del [sitio oficial de Pandas](https://pandas.pydata.org/). Pandas es un conjunto de herramientas para estructurar, manipular y analizar datos mediante el lenguaje de programación Python. Permite estructurar la información de manera tabular mediante el uso de tablas conocidas como **DataFrames**. A partir de un DataFrame, se vuelve relativamente sencillo la manipulación numérica y de series de tiempo.

Pandas es de código abierto y puede ser utilizado de manera gratuita bajo la [licencia BSD](https://en.wikipedia.org/wiki/BSD_licenses).

### 1.2. Cómo instalar Pandas.

Instalar Pandas puede resultar un poco enredos para usuarios inexpertos. La manera más simple de instalar Pandas y un listado de las librerías más populares es a través de [Anaconda](https://www.anaconda.com/distribution/). También existe una versión de tamaño más reducida, si se desea tener más control sobre los paquetes o se tiene una conexión de internet limitada, conocida como [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

También se puede instalar directamente desde la terminal, utilizando el administrador de paquetes de Python pip.

```bash
pip install pandas
```

Toda la información para la [instalación de Pandas](https://pandas.pydata.org/pandas-docs/stable/install.html) se encuentra aquí.

### 1.3. Dónde está la documentación oficial.

La documentación oficial de pandas se encuentra disponible en inglés siguiendo la liga:

https://pandas.pydata.org/pandas-docs/stable/


    - 1.4. Qué es un DataFrame.
        - Comparación contra un JSON.

## 2. Importar datos utilizando Pandas

### 2.1. Importar JSON.

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

Para hacer el proceso inverso, y convertir de un data frame a un JSON se utiliza el método to_dict(orient='records').

```python
json_structure = tabla.to_dict(orient='records')
```

### 2.2. Importar CSV.

```python
import pandas as pd

filename = 'data/declaratorias_emergencia_desastre.csv'
tabla = pd.read_csv(filename, encoding='utf-8')

print(tabla.head())
```

### 2.3. Importar EXCEL.

```python
import pandas as pd

filename = 'data/declaratorias_emergencia_desastre.xlsx'
tabla = pd.read_excel(filename)

print(tabla.head())
```

### 2.4. Importar XML.

https://datos.gob.mx/busca/dataset/estaciones-de-servicio-gasolineras-y-precios-finales-de-gasolina-y-diesel

## 3. Conociendo nuestros datos

### 3.1. Head, tail & info.

Son los tres principales métodos para visualizar de manera preeliminar la información contenida dentro de un DataFrame.

La [**Función Head**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html) regresa las primeras n filas de una tabla. Es útil para comprobar que nuestro objeto contiene los tipos de datos correctos.

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

La [**Función Tail**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.tail.html) regresa las últimas n filas de una tabla. Es útil para verificar los datos después de haber sido ordenardos o al insertar (append) de filas.

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

La [**Función Info**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html) imprime información acerca del DataFrame, incluyendo el tipo (dtype) del índice y de las columnas, los valores nulos y el uso de memoria.

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

object
int64
float64
datetime64
bool

Cuando comencemos a trabajar con información, lo primero que tenemos que revisar los tipos de datos con los que estamos trabajado. (Qué pasa si sumamos dos números aue son strings). En pandas pasa igual, pero el tipo de dato es por toda la columna.

Los tipos de datos es uno de esos puntos que se nos olvida revisar hasta que se genera un error o algún otro resultado inesperado. Es algo que sd debe revisar primero cuando se importa un nuevo dataset a pandas para su subsecuente análisis.

Cuando estemos haciendo cualquier tipo de analisis, es importante asegurarnos de estar utilizando el tipo de dato correcto. En el caso de pandas, inferirá de manera correcta los tipos de datos de las columnas, si este es el caso, se puede proseguir el análisis sin ningún tipo de modificación.

Sin embargo, es probable que en algún punto del proceso de análisis de datos, se requiera explícitamente concertir de un tipo de dato a otro. 

Los tipos de datos de las columnas en pandas se conoce como dtypes.

Continuando el punto 2.1 cuando cargamos el dataset de conagua mediante un archivo json. El código completo de esta sección se encuentra en 3-2-dtypes.py.

```python
print(tabla.head())
#                         _id    cityid      validdateutc winddirectioncardinal  \
# 0  5952983359954a0adbf7ab09  MXAS0002  20170627T140000Z                   SSE
# 1  5952983359954a0adbf7ab0a  MXAS0170  20170627T140000Z                     S
# 2  5952983359954a0adbf7ab0b  MXAS0171  20170627T140000Z                     E
# 3  5952983359954a0adbf7ab0c  MXAS0172  20170627T140000Z                     S
# 4  5952983359954a0adbf7ab0d  MXAS0173  20170627T140000Z                   SSO

#   probabilityofprecip relativehumidity            name  \
# 0                  40               90  Aguascalientes
# 1                  60               91        Asientos
# 2                  60               84        Calvillo
# 3                  50               83           Cosío
# 4                  50               84        El Llano

#                 date-insert  longitude           state    lastreporttime  \
# 0  2017-06-27T17:36:43.084Z   -102.296  Aguascalientes  20170627T092449Z
# 1  2017-06-27T17:36:43.088Z  -102.0893  Aguascalientes  20170627T092453Z
# 2  2017-06-27T17:36:43.088Z  -102.7188  Aguascalientes  20170627T092453Z
# 3  2017-06-27T17:36:43.088Z     -102.3  Aguascalientes  20170627T092453Z
# 4  2017-06-27T17:36:43.089Z  -101.9653  Aguascalientes  20170627T092453Z

#     skydescriptionlong stateabbr tempc  latitude iconcode windspeedkm
# 0  Tormentas dispersas       AGU    17  21.87982       96           6
# 1  Tormentas dispersas       AGU    15  22.23832       96           5
# 2  Tormentas dispersas       AGU    19  21.84691       96           2
# 3  Tormentas dispersas       AGU    17  22.36641       96           3
# 4  Tormentas dispersas       AGU    17  21.91887       96           3
```

Si por alguna razón quisieramos sumar los valores de la columna `probabilityofprecip` y `relativehumidity` entonces utilizando pandas sumaremos los valores de dos columnas se haría de la siguiente manera.

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

Los resultados no son, notoriamente, los esperados de una suma correcta. Queríamos sumar las cantidades de las dos columnas, y lo que se consiguió es un string más largo. Y parte de la solución se encuentra en el dtype de la columna de resultados (dtype: object). Un `object` es un string en pandas por lo tanto realiza operaciones de strings no matemáticas.

Si queremos conocer los tipos de datos de un dataframe, utilizar el atributo tabla.dtypes:

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

Como se puede apreciar, todas las columnas, a pesar de que algunas contenían valores numéricos, fueron registradas en pandas como object.

Para convertir un tipo de dato en pandas existen tres opciones básicas:

- Utilizar astype() para forzar el dtype adecuado.
- Crear una función para convertir el tipo de dato.
- Utilizar una función de pandas como to_numeric() or to_datetime().

Revisaremos a detalle cada una de estas.

#### 3.2.1. El método astype().

El método más simple de convertir una columna de pandas a los diferentes tipos es utilizar astype(). Por ejemplo, convertamos las columnas `probabilityofprecip` y `relativehumidity` a valores numéricos y hagamos la suma de manera correcta.

```python
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

El método astype() nos permitió interpretar los valores como enteros, en lugar de líneas de caracteres, para poder realizar la suma.

#### 3.2.2. Creando una función customisada.

Otra opción es utilizando la función map, para aplicar una función en toda la columna. La opción más directa sería:

```python
tabla['probabilityofprecip'] = tabla['probabilityofprecip'].map(int)
```

Esta sintaxis funciona igual que astype(). Sin embargo, quizá querramos utilizar funciones más complicadas, como por ejemplo: convertir latitud y longitud en valores flotantes, conservando únicamente los valores redondeados hasta 3 decimales. Podemos utilizar una función lambda, aux_fun(), que convierta a tipo float y luego convierta el valor a 3 decimales. Al final, podemos utilizart una variable auxiliar `select` para filtrar las columnas de mi data frame e imprimir los valores de esas 2 columns.

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

Para el siguiente caso podríamos utilizar una pequeña estandarización de un string para interpretar correctamente su valor numérico definiendo una función en python. Añadiendo un pequeño condicional para evitar que si el string no puede ser identificado como numérico, no nos arroje un error, y regrese un valor nulo, 0.

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

Recordemos que la función isinstance() regresa True si el objeto dato es un string. Posteriormente, el método de los strings strip() elimina espacios innecesarios al inicio y al final. Y por último, isdigit() evalúa si es posible convertir un texto a un valor entero, evitando de esta manera algún error en el código.

#### 3.2.3. Uso de tiempo y fechas.

Es muy común que la fecha se almacene como string, es importante si se desean utilizar los valores como fechas, se interpreten de esta manera. Una de las maneras es a través de la función `pd.to_datetime()`.

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

El dtype cambió a datetime64[ns]. Se puede revisar la [información completa](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior) de los formatos de fecha en Python, pero los más comunes son: "%d-%m-%Y", "%d/%m/%Y" y "%m-%y"; donde:

- **%d** - indica el día del mes en dos dígitos: 21, 04, 31 son válidos.
- **%m** - indica el mes en dos dígitos: 01, 12, 09 son válidos.
- **%b** - indica el mes abreviado con 3 letras: jan, feb, dec son válidos.
- **%Y** - indica el año con 4 dígitos: 2000, 1998 y 2019 son válidos.
- **%y** - indica el año con 2 dígitos: 99, 19, 00 son válidos.

Al final, los tipos de datos de nuestro dataframe deben lucir de la siguiente manera.

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

#### 3.3.2. Establecer un valor que tendrán todos los valores faltantes.

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

Pandas dataframe.bfill() is used to backward fill the missing values in the dataset. It will backward fill the NaN values that are present in the pandas dataframe.

Pandas dataframe.ffill() function is used to fill the missing value in the dataframe. ‘ffill’ stands for ‘forward fill’ and will propagate last valid observation forward.


    - 3.4. Niveles de agregación y validez estadística.
        - Muestra vs población.

###########- introducir nueva sección sobre instalación y mención: de rubik

## 4. Casos de uso de Pandas

    - 4.1. Transformar la estructura de la información.
    - 4.2. Extracción de información específica.
    - 4.3. Agrupar la información.

## 5. Seguimiento




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