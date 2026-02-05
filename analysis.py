import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Análisis de Argentina
df = pd.read_csv('../data/spotify-streaming-top-50-argentina.csv')
df_artistas = df['artist'].value_counts()
top_artistas = df_artistas.head(10)

print("Top 10 artistas con más canciones en el top 50 de Spotify Argentina:")
print(top_artistas)

plt.figure(figsize=(10,6))
top_artistas.plot(kind='bar', color='skyblue')
plt.title('Top 10 artistas con más canciones en el top 50 de Spotify Argentina')
plt.xlabel('Artista')
plt.ylabel('Número de canciones en el top 50')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_artistas_argentina.png', dpi=300) 
plt.show()

# 2. Análisis de World
df_world = pd.read_csv('../data/spotify-streaming-top-50-world.csv')
df_worldartist = df_world['artist'].value_counts()
top_worldartistas = df_worldartist.head(10)

print("Top 10 artistas con más canciones en el top 50 de Spotify World:")
print(top_worldartistas)

plt.figure(figsize=(10,6))
top_worldartistas.plot(kind='bar', color='salmon')
plt.title('Top 10 artistas con más canciones en el top 50 de Spotify World')
plt.xlabel('Artista')
plt.ylabel('Número de canciones en el top 50')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_artistas_world.png', dpi=300) # Guardar gráfico
plt.show()

# 3. Comparación de Tops
common_artists = set(top_artistas.index).intersection(set(top_worldartistas.index))
print("Artistas comunes en ambos top 10:")
print(common_artists)

if common_artists:
    common_counts_arg = [top_artistas[artist] for artist in common_artists]
    common_counts_world = [top_worldartistas[artist] for artist in common_artists]
    
    x = np.arange(len(common_artists))
    width = 0.35
    
    plt.figure(figsize=(10,6))
    plt.bar(x - width/2, common_counts_arg, width, label='Argentina', color='skyblue')
    plt.bar(x + width/2, common_counts_world, width, label='World', color='salmon')
    
    plt.title('Artistas comunes en ambos top 10')
    plt.xlabel('Artista')
    plt.ylabel('Número de canciones en el top 50')
    plt.xticks(x, list(common_artists), rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig('artistas_comunes.png', dpi=300) # Guardar gráfico
    plt.show()
else:
    print("No hay artistas comunes en ambos top 10.")

# 4. Canciones más largas (World)
top10_longsong = df_world.drop_duplicates(subset=['song','artist'])
top10_longsong = top10_longsong.nlargest(10, 'duration_ms')[['artist', 'song', 'duration_ms']]

print("Top 10 canciones más largas en el top 50 de Spotify World:")
print(top10_longsong)

plt.figure(figsize=(10,6))
plt.barh(
    top10_longsong['song'].str.cat(top10_longsong['artist'], sep=' - '),
    top10_longsong['duration_ms'],
    color='lightgreen'
)
plt.title('Top 10 canciones más largas en el top 50 de Spotify World')
plt.xlabel('Duración (ms)')
plt.ylabel('Canción')
plt.tight_layout()
plt.savefig('canciones_mas_largas.png', dpi=300) # Guardar gráfico
plt.show()

# 5. Comparativa Drake vs Kendrick Lamar
drakepop = df_world[df_world['artist'].str.contains('Drake')]['popularity'].mean()
kendrickpop = df_world[df_world['artist'].str.contains('Kendrick Lamar')]['popularity'].mean()

print(f"Popularidad promedio de Drake: {drakepop}")
print(f"Popularidad promedio de Kendrick: {kendrickpop}")

plt.figure(figsize=(8,6))
artists = ['Drake', 'Kendrick Lamar']
popularity = [drakepop, kendrickpop]
plt.bar(artists, popularity, color=['blue', 'orange'])
plt.title('Popularidad promedio en el top 50 World')
plt.xlabel('Artista')
plt.ylabel('Popularidad promedio')
plt.tight_layout()
plt.savefig('popularidad_drake_kendrick.png', dpi=300) # Guardar gráfico
plt.show()