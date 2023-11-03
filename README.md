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
Para cada uno de estos archivos se realizo un ETL  
  







