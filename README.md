# 🎧 Spotify Top 50 Insights Analysis

## Proyecto de Análisis de Datos de Streaming
Este proyecto realiza un análisis comparativo entre los charts de **Spotify Top 50 Argentina** y **Spotify Top 50 Global**. El objetivo es identificar tendencias de artistas, comparar la presencia de géneros locales versus globales y analizar atributos específicos como la duración de las canciones y la popularidad de artistas clave.

## 📊 Principales Análisis
1. **Liderazgo de Artistas:** Identificación de los artistas con mayor cantidad de tracks simultáneos en los tops.
2. **Intersección de Mercados:** Comparación de artistas que logran posicionarse tanto en el mercado argentino como en el global.
3. **Análisis de Duración:** Ranking de las canciones más extensas dentro del Top 50 World.
4. **Duelo de Popularidad (A/B Testing):** Análisis estadístico del promedio de popularidad entre artistas específicos (Ej: Drake vs Kendrick Lamar).

## 🛠️ Tecnologías Utilizadas
* **Python 3.10+**
* **Pandas:** Procesamiento y limpieza de datasets.
* **Matplotlib & NumPy:** Generación de visualizaciones estadísticas y manejo de arreglos.

## 📁 Estructura de Salida
El script genera automáticamente los siguientes reportes visuales en formato `.png`:
* `top_artistas_argentina.png`: El market share de artistas en Argentina.
* `top_artistas_world.png`: Líderes del chart global.
* `artistas_comunes.png`: Gráfico comparativo de artistas compartidos.
* `canciones_mas_largas.png`: Distribución de duración de tracks.
* `popularidad_drake_kendrick.png`: Comparativa directa de métricas de popularidad.

## 🚀 Cómo ejecutar
1. Asegúrate de tener los archivos CSV en la carpeta `../data/`.
2. Instala los requerimientos: `pip install pandas matplotlib numpy`.
3. Ejecuta el script: `python spotify_analysis.py`.

---
*Análisis desarrollado como parte de un enfoque en Ingeniería de Datos y Visualización.*