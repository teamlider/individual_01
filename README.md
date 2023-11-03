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

### Bibliotecas utilizadas en el desarrollo del proyecto.
  
Para cada uno de estos archivos se realizo un ETL , proceso de Extracción, Transformación y Lectuta de datos. con el objetivo de alistar los datos para el EDA.en el primer archivo steam_games se descomprimio el archivo , se crea un dataframe y se eliminan bastantes datos nulos y vacios de este archivo y posteriormente se igualan o reinician los indices despues de la limpieza, se realizan algunas transformaciones necesarias como el en campo release_date que se pasa de categorica a formato datatime. en los archivos podrán realizar seguimiento al proceso en detalle.

<img width="427" alt="Captura de pantalla 2023-11-03 a la(s) 3 59 00 p m" src="https://github.com/teamlider/individual_01/assets/54252072/a8dbccfd-a12b-407b-ba22-7751903e2d1c">

En los archivos user_reviews y users_items el proceso de extracción fue mas complejo pues estos datos venian anidados dentro de diccionarios. pero basicamente despues de su extracción se les realizo el mismo tratamiento. y finalmente exporto los tres archivos limpios en formato.parquet para empezar a bajar el pesos de los datos.

<img width="1108" alt="Captura de pantalla 2023-11-03 a la(s) 4 01 38 p m" src="https://github.com/teamlider/individual_01/assets/54252072/de504ba6-1a5e-4b1f-86c8-d0c86c5b3aaf">

Con los tres archivos.parquet ya limpios, inicio el EDA , pero lo realizo con base en el requerimiento para cada función del MVP. Esto con el objeto de seleccionar solo los campos necesarios para cada función para optimizar recursos en cuanto al peso de los archivos y poder finalmente exportar solo el archivo con los campos necesarios para cada función. además de analizar graficamente la distribución de los campos en busca de relaciones para poder solucionar el problema para cada función. incluyo tambien el desarrollo de una función de prueba para testear el resultado y comprobar que las consultas se estan realizando de manera adecuada.

### Distribución de los campos.
<img width="869" alt="Captura de pantalla 2023-11-03 a la(s) 4 14 20 p m" src="https://github.com/teamlider/individual_01/assets/54252072/bcbb026b-cae8-4eb0-9936-f9d11be1003c">

### Relación entre los campos.
<img width="1019" alt="Captura de pantalla 2023-11-03 a la(s) 4 15 14 p m" src="https://github.com/teamlider/individual_01/assets/54252072/7230c70c-ff42-451c-807c-912f37198768">
<img width="1005" alt="Captura de pantalla 2023-11-03 a la(s) 4 14 57 p m" src="https://github.com/teamlider/individual_01/assets/54252072/b57aed74-3a4a-4045-93dc-a2dc026910c6">


### Relación entre los campos con el objeto de dar solución a las funciones de manera gráfica.
<img width="1026" alt="Captura de pantalla 2023-11-03 a la(s) 4 14 37 p m" src="https://github.com/teamlider/individual_01/assets/54252072/c39a2e4e-d76a-4412-9213-c30419e9a26b">

Finalizando el proceso en el EDA para cada función, realizo el testing de la función en ipynb. para posteriormente pasarla al main dentro de la API, con su correspondiente archivo.
<img width="1119" alt="Captura de pantalla 2023-11-03 a la(s) 4 27 18 p m" src="https://github.com/teamlider/individual_01/assets/54252072/2c15850a-6429-4704-9b33-b01a5a0bef76">
de esta manera pude optimizar al maximo los archivos y todas la funciones me corrieron sin problemas en el deploy. Para el EDA del modelo lo realice de la misma manera . pero en este caso tome una muestra de los datos pues ya no me quedaba suficiente capacidad en el render.


### Muestra para la función del modelo MC ,def recomendacion_juego( id de producto ):
<img width="403" alt="Captura de pantalla 2023-11-03 a la(s) 4 32 53 p m" src="https://github.com/teamlider/individual_01/assets/54252072/10b14e73-66d6-49be-8254-9064ed605eff">

Con cada archivo listo solo fue convertir las funciones del EDA a END POINTS de FASTAPI dentro del archivo main.py.
y con  cada archivo creo el dataframe con los campos correspondientes por función.
<img width="681" alt="Captura de pantalla 2023-11-03 a la(s) 4 41 33 p m" src="https://github.com/teamlider/individual_01/assets/54252072/68fd6e08-77ee-4677-9230-74994bae1f91">

### Finalmente realizo el deploy en render.
<img width="1419" alt="Captura de pantalla 2023-11-03 a la(s) 4 43 49 p m" src="https://github.com/teamlider/individual_01/assets/54252072/c2f13ddc-d16e-44c9-a904-32975ff63ccd">



  







