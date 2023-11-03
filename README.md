# individual_01
Proyecto Individual 01 Data Enginer
<img width="887" alt="Captura de pantalla 2023-11-03 a la(s) 2 39 38 p m" src="https://github.com/teamlider/individual_01/assets/54252072/95cb86f4-31b8-44d0-96b4-2cf336c767da">
## _Desarrollo del Proyecto_
### El objetivo de esta primera parte del proyecto individual era realizar el ETL (Extracción, Transformación y Carga ), del data set de la plataforma STEAM, posteriormente el analisis exploratorio de datos con el objetivo de diseñar 5 funciónes y un modelo de MC a través de una sexta función.

# En este repositorio vas a encontrar varios archivos con la trazabilidad del proyecto de Data Enginer.
## Contenido


| Archivo | Contenido
| ------ | ------ |
| ETL_steam_games | proceso de Extracción, Limpieza y lectura del archivo. |
| ETL_user_reviews | proceso de Extracción, Limpieza y lectura del archivo. |
| ETL_users_items | proceso de Extracción, Limpieza y lectura del archivo. |
| steam_games.parquet | Archivo limpio listo para el EDA |
| user_reviews.parquet | Archivo limpio listo para el EDA |
| users_items.parquet | Archivo limpio listo para el EDA |
| EDA.ipynb | Analisis Exploratorio y selección de campos necesarios para las cinco funciones  |
| EDA_MC.ipynb | Analisis Exploratorio y selección de campos y muestra de datos para la función del MC |
| main.py | archivo de apis y funciones del proyecto |
| data_primera_funcion.parquet | Archivo producto del EDA de la primera función con los campos necesarios para la consulta |
| data_segunda_funcion.parquet | Archivo producto del EDA de la segunda función con los campos necesarios para la consulta |
| data_terceraCuarta_funcion.parquet | Archivo producto del EDA de la tercera  cuarta función con los campos necesarios para la consulta |
| datosquinta_funcion.parquet | Archivo producto del EDA de la quinta función con los campos necesarios para la consulta |
| data_mc.parquet | Archivo producto del EDA para la función MC con los campos necesarios para la consulta |
| requirements.txt | Bibliotecas necesarias para el render |


### Resumen del proceso de desarrollo.
Se descargo el dataset del la plataforma STEAM originalmente con tres archivos en formato json y comprimidos en gz.
- steam_games.json.gz
- user_reviews.json.gz
- users_items.json.gz
  
Para cada uno de estos archivos se realizo un ETL , proceso de Extracción, Transformación y Lectuta de datos. con el objetivo de alistar los datos para el EDA.en el primer archivo steam_games se descomprimio el archivo , se crea un dataframe y se eliminan bastantes datos nulos y vacios de este archivo y posteriormente se igualan o reinician los indices despues de la limpieza, se realizan algunas transformaciones necesarias como el en campo release_date que se pasa de categorica a formato datatime. en los archivos podrán realizar seguimiento al proceso en detalle.

<img width="427" alt="Captura de pantalla 2023-11-03 a la(s) 3 59 00 p m" src="https://github.com/teamlider/individual_01/assets/54252072/a8dbccfd-a12b-407b-ba22-7751903e2d1c">

En los archivos user_reviews y users_items el proceso de extracción fue mas complejo pues estos datos venian anidados dentro de diccionarios. pero basicamente despues de su extracción se les realizo el mismo tratamiento. y finalmente exporto los tres archivos limpios en formato.parquet para empezar a bajar el pesos de los datos.

<img width="1108" alt="Captura de pantalla 2023-11-03 a la(s) 4 01 38 p m" src="https://github.com/teamlider/individual_01/assets/54252072/de504ba6-1a5e-4b1f-86c8-d0c86c5b3aaf">

Con los tres archivos.parquet ya limpios, inicio el EDA , pero lo realizo con base en el requerimiento para cada función del MVP. Esto con el objeto de seleccionar solo los campos necesarios para cada función para optimizar recursos en cuanto al peso de los archivos y poder finalmente exportar solo el archivo con los campos necesarios para cada función. además de analizar graficamente la distribución de los campos en busca de relaciones para poder solucionar el problema para cada función. incluyo tambien el desarrollo de una función de prueba para testear el resultado y comprobar que las consultas se estan realizando de manera adecuada.





  







