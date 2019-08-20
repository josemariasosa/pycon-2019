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


    - 3.2. Fechas y tipos de datos.
    - 3.3. Valores faltantes.
    - 3.4. Niveles de agregación y validez estadística.
        - Muestra vs población.

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