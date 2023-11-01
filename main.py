import fastapi
import pandas as pd
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


# Primera función def (PlayTimeGenre)
#-------------------------------------

# Cargo los datos desde el archivo Parquet y creo el dataframe df_primera_función.
df_primera_funcion = pd.read_parquet('data_primera_funcion.parquet')


app = fastapi.FastAPI()

@app.get('/play_time_genre/{genero}')
def PlayTimeGenre(genero: str):
    df_expanded = df_primera_funcion.explode('genres')

    # Filtro las filas que contienen el género especificado
    df_filtered = df_expanded[df_expanded['genres'].apply(lambda genres: genero in genres)]

    if df_filtered.empty:
        return {f"No se encontraron datos para el género {genero}": None}

    # Encuentro el año con más horas jugadas para el género
    max_year = df_filtered.groupby('release_date')['playtime_forever'].sum().idxmax().year

    return {f"Año de lanzamiento con más horas jugadas para el género {genero}": max_year}


# Segunda Función (UserForGenre)
#----------------------------------

# Cargo los datos desde el archivo Parquet y creo el dataframe df_segunda_función.
df_segunda_funcion = pd.read_parquet('data_segunda_funcion.parquet')

@app.get('/user_for_genre/{genero}')
def UserForGenre(genero: str):
    # Explode (desglosa) la columna 'genres' para que cada género esté en una fila independiente
    df_desglosado = df_segunda_funcion.explode('genres')

    # Filtro las filas que contienen el género especificado
    df_filtrado = df_desglosado[df_desglosado['genres'] == genero]

    if df_filtrado.empty:
        return {f"No se encontraron datos para el género {genero}": None}

    # Encuentro el usuario que jugó más minutos para el género
    usuario_max_minutos = df_filtrado[df_filtrado['playtime_forever'] == df_filtrado['playtime_forever'].max()]

    # Agrupo los minutos jugados por año
    minutos_por_anio = df_filtrado.groupby(df_filtrado['release_date'].dt.year)['playtime_forever'].sum()

    resultado = {
        "Usuario con más horas jugadas para Género X": usuario_max_minutos['user_id'].values[0],
        "Horas jugadas": [{"Año": año, "Minutos": horas} for año, horas in minutos_por_anio.items()]
    }

    return resultado


# Tercera Función (UsersRecommend)
#----------------------------------

# Cargo los datos desde el archivo Parquet y creo el dataframe df_tercera_función.
df_tercera_funcion = pd.read_parquet('data_terceraCuarta_funcion.parquet')


# Definimos la ruta que acepta el año como parámetro
@app.get('/users_recommend/{year}')
def UsersRecommend(year: int):
    # Filtro los juegos recomendados y con comentarios positivos/neutrales para el año especificado
    filtered_df = df_tercera_funcion[(df_tercera_funcion['recommend'] == True) & (df_tercera_funcion['sentiment_analysis'] >= 0) & (df_tercera_funcion['posted_date'].dt.year == year)]
    
    # Agrupo por título, cuento las recomendaciones y ordeno en orden descendente
    recommended_by_title = filtered_df.groupby('title')['recommend'].sum().reset_index()
    recommended_by_title = recommended_by_title.sort_values(by='recommend', ascending=False)
    
    # Selecciono los 3 juegos más recomendados
    top3_games = recommended_by_title.head(3)
    
    # Creo una lista de diccionarios con el formato especificado
    result = [{"Puesto 1": top3_games.iloc[0]['title']},
              {"Puesto 2": top3_games.iloc[1]['title']},
              {"Puesto 3": top3_games.iloc[2]['title']}]
    
    return result


# Cuarta Función (UsersNotRecommend)
#--------------------------------------


# Cargo los datos desde el archivo Parquet y creo el dataframe df_tercera_función.
df_cuarta_funcion = pd.read_parquet('data_terceraCuarta_funcion.parquet')

@app.get('/users_not_recommend/{year}')
def UsersNotRecommend(year: int):
    # Filtro los juegos no recomendados y con comentarios negativos para el año especificado
    filtered_df = df_cuarta_funcion[(df_cuarta_funcion['recommend'] == False) & (df_cuarta_funcion['sentiment_analysis'] == 0) & (df_cuarta_funcion['posted_date'].dt.year == year)]
    
    # Agrupo por título, cuento las no recomendaciones y ordeno en orden descendente
    not_recommended_by_title = filtered_df.groupby('title')['recommend'].count().reset_index()
    not_recommended_by_title = not_recommended_by_title.sort_values(by='recommend', ascending=False)
    
    # Selecciono los 3 juegos menos recomendados
    bottom3_games = not_recommended_by_title.head(3)
    
    # Creo una lista de diccionarios con el formato especificado
    result = [{"Puesto 1": bottom3_games.iloc[0]['title']},
              {"Puesto 2": bottom3_games.iloc[1]['title']},
              {"Puesto 3": bottom3_games.iloc[2]['title']}]
    
    return result



# Quinta Función (UsersNotRecommend)
#--------------------------------------

# Cargo la  data desde el archivo Parquet
df_quinta_funcion = pd.read_parquet('datosquinta_funcion.parquet')


@app.get('/sentiment_analysis/{year}')
def sentiment_analysis(year: int):
    # Filtro el DataFrame por el año de lanzamiento
    filtrado_por_año = df_quinta_funcion[df_quinta_funcion['release_date'].dt.year == year]

    # Calculo el número de registros para cada categoría de análisis de sentimiento
    total_negativos = len(filtrado_por_año[filtrado_por_año['sentiment_analysis'] == 0])
    total_neutros = len(filtrado_por_año[filtrado_por_año['sentiment_analysis'] == 1])
    total_positivos = len(filtrado_por_año[filtrado_por_año['sentiment_analysis'] == 2])

    # Creo un diccionario con los resultados
    resultado = {'Negative': total_negativos, 'Neutral': total_neutros, 'Positive': total_positivos}

    return resultado


# Función Modelo MC recoemndación de juegos
#---------------------------------------------

# Cargo la data a un df.
# Cargo la  data desde el archivo Parquet
df_mcf = pd.read_parquet('data_mc.parquet')

# Paso 1: Preproceso los datos
df_mcf['genres_text'] = df_mcf['genres'].apply(lambda x: ' '.join(x))

# Paso 2: Creo una matriz TF-IDF
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(df_mcf['genres_text'])

# Paso 3: Calculo la similitud de coseno
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Paso 4: Defino la función de recomendación
def recomendacion_juego(item_id, cosine_sim=cosine_sim):
    # Encuentro el índice del juego en función de su item_id.
    idx = df_mcf[df_mcf['item_id'] == item_id].index[0]

    # Calculo la puntuación de similitud de coseno para todos los juegos con el juego dado.
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Ordeno los juegos según su puntuación de similitud.
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Obtengo los índices de los juegos más similares.
    sim_scores = sim_scores[1:6]

    # Obtengo los títulos de los juegos recomendados.
    game_indices = [i[0] for i in sim_scores]
    recommended_games = df_mcf['title'].iloc[game_indices]

    return recommended_games

# Modelo Pydantic para la entrada
class ItemId(BaseModel):
    item_id: float

# Endpoint para recibir solicitudes de recomendación
@app.get("/recomendar_juegos/")
async def get_recommendations(item_id: ItemId):
    recommendations = recomendacion_juego(item_id.item_id)
    return {"recomendaciones": recommendations.to_list()}





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
