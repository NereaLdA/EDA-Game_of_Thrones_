#NOTA: RUN IN TERMINAL CON python Main.py

#PALETA COLORES
GOTcolors = [
    "#1C1C1C",  # Negro (Noche / Guardia de la Noche)
    "#8B0000",  # Rojo oscuro (Casa Baratheon)
    "#4682B4",  # Azul acero (Casa Stark, invierno)
    "#DAA520",  # Dorado (Casa Lannister)
    "#708090",  # Gris pizarra (Hierro / Casa Greyjoy)
    "#013220",  # Verde oscuro (Casa Tyrell / naturaleza)
    "#2F4F4F",  # Gris oscuro (batallas, oscuridad)
    "#A52A2A",   # Marrón rojizo (sangre, tierra)
    "#00CED1",  # Azul hielo más intenso (Caminantes Blancos / Invierno)
    "#CD853F",   # Marrón dorado (verano, desierto / Daenerys)
    "#4B0082",  # Índigo oscuro (Casa Targaryen, magia, fuego valyrio)
    "#C0C0C0",  # Plata (tramas de nobleza, armaduras, escarcha)
    "#5D3A00",  # Marrón oscuro (madera, castillos, la Guardia Real)
    "#191970",  # Azul medianoche (La larga noche, Caminantes Blancos)
    "#800000",  # Burdeos (sangre seca, poder, guerra)
    "#556B2F",   # Verde oliva oscuro (naturaleza salvaje, tierras del Norte)
]


#IMPORTS
from sklearn.datasets import load_iris
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8')
import warnings
warnings.filterwarnings("ignore")
from matplotlib.colors import LinearSegmentedColormap

#DATAFRAMES
df_battles = pd.read_csv('../data/battles.csv')
df_episodes = pd.read_csv('../data/episodes.csv')
df_epi_deaths = pd.read_csv('../data/episodios_y_muertes.csv')
df_muertes_epi1 = pd.read_csv('../data/muertes_x_episodio1.csv')
df_muertes_epi2 = pd.read_csv('../data/muertes_x_episodio2.csv')
df_viewers = pd.read_csv('../data/viewers.csv')

#LIMPIEZA DATAFRAMES
df_battles_clean = df_battles.drop(["year","battle_number","location","region","major_capture","battle_type","attacker_2","attacker_3","attacker_4","defender_2","defender_3","defender_4","note"], axis=1)
df_battles_clean.to_csv("../data_clean/df_battles_clean.csv", index=False)
df_episodes_clean = df_episodes.drop(["Ordered","Filming Duration","Original Air Date","Running Time (Minutes)","Directed by","Written by","Music by","Cinematography by","Editing by","Synopsis"], axis=1)
#cambiar nombre a columna
df_episodes_clean.rename(columns={"Rotten Tomatoes Rating (Percentage)": "Rotten Tomatoes Rating"}, inplace=True)
#cambiar valores escala (sobre 10, no %)
df_episodes_clean["Rotten Tomatoes Rating"] = df_episodes_clean["Rotten Tomatoes Rating"] / 10
df_episodes_clean.to_csv("../data_clean/df_episodes_clean.csv", index=False)
df_epi_deaths_clean = df_epi_deaths.drop(["Director","Writer","Original Air Date","IMDB Description"], axis=1)
df_epi_deaths_clean.to_csv("../data_clean/df_epi_deaths_clean.csv", index=False)
#CAMBIAR NOMBRES COLUMNAS POR 1º REGISTROS
# Reemplazar los nombres de las columnas desde la posición 2 en adelante con los valores de la primera fila
df_muertes_epi1.columns = list(df_muertes_epi1.columns[:2]) + list(df_muertes_epi1.iloc[0, 2:])
# Eliminar la primera fila (ya que la usamos como cabecera)
df_muertes_epi1 = df_muertes_epi1[1:]
# Reiniciar el índice
df_muertes_epi1 = df_muertes_epi1.reset_index(drop=True)
secundarios = ['Golden Company soldier','Golden Company horse', "King's Landing Citizen",
               'Unsullied','Undead Polar Bear', 'Greyjoy Soldier','Frey family member',
               "King's Landing Noble", 'Stark Soldier', 'The Masters Soldier','Meereen citizen',
               'Faith Militant Brother','Brotherhood Without Banners Member', 'Gladiator','Horse',
               'Stone Man', 'Unsullied Soldier', 'Second Sun Mercenary','Dorne Smuggler','Dorne Horse',
               'Dorne Soldier','Snake', 'Rat','Meereen slave','Sons of the Harpy agent','Unamed Dwarf',
               'Baelish soldier', 'Greyjoy soldier', "Night's Watch brother","Night's Watch mutineer",
               'Meereen slave master','Champion of Meereen',"Champion of Meereen's Horse",'Deer','Dragonstone citizen',
                'Unborn Stark child','Yunkai soldier','Horse breeder','White Walker','Astapor slaver',
                'Bolton soldier',"Baratheon of King's Landing soldier",'Baratheon of Dragonstone soldier',
                'Member of the Thirteen',"Baratheon of Storm's End guard",'Prisoner',"Night's Watch recruit",
                "Drogo's horse",'Stark staff member', 'Stableboy',"Olly's mum",'Wildling','Lannister soldier',
                'Tribesman','Stark soldier',"Clegane's horse",'Lady','Dothraki man','Direwolf','Stag']
df_muertes_epi1_clean = df_muertes_epi1[~df_muertes_epi1['Name'].isin(secundarios)]
df_muertes_epi1_clean.to_csv("../data_clean/df_muertes_epi1_clean.csv", index=False)
df_muertes_epi2_clean = df_muertes_epi2.drop(["reason","allegiance"], axis=1)
df_muertes_epi2_clean.to_csv("../data_clean/df_muertes_epi2_clean.csv", index=False)
df_viewers_clean = df_viewers.drop(["Original air date [20]"], axis=1)
df_viewers_clean.to_csv("../data_clean/df_viewers_clean.csv", index=False)

#FUSIÓN DATAFRAMES
df_muertes_epi2_merge = pd.read_csv('../data/muertes_x_episodio2.csv')
df_muertes_epi2_merge_clean = df_muertes_epi2_merge.drop(["order","season","character_killed","killer","method","reason","location","importance","allegiance"], axis=1)
df_muertes_epi2_merge_clean.to_csv("../data_clean/df_muertes_epi2_merge_clean.csv", index=False)

df_viewers_merge = pd.read_csv('../data/viewers.csv')
df_viewers_merge_clean = df_viewers_merge.drop(["Unnamed: 0", "No.overall", "Title", "Directed by", "Written by", "Original air date [20]", "Season"],axis=1)
df_viewers_merge_clean.rename(columns={"No. inseason": "episode"}, inplace=True)
df_viewers_merge_clean.to_csv("../data_clean/df_viewers_merge_clean.csv")

df_muertes_y_viewers = df_muertes_epi2_merge_clean.merge(df_viewers_merge_clean, on='episode', how='left')


#HIPÓTESIS 1
#1
colors = ["#4682B4", "white", "#8B0000"]  
custom_cmap = LinearSegmentedColormap.from_list("got_cmap", colors, N=256)
corr = df_epi_deaths_clean.select_dtypes(include='number').corr()
plt.figure(figsize=(15, 15))
sns.heatmap(corr,
            vmin=-1,
            vmax=1,
            cmap=custom_cmap,
            square=True,
            linewidths=.1,
            annot=True);
plt.title("HEATMAP CORRELACIONES 1", fontsize=20)
plt.savefig("../img/Heatmap_correlaciones_1")

#2
df = df_epi_deaths.sort_values(by=["Season", "Number in Season"])
fig, ax1 = plt.subplots(figsize=(14, 6))
ax1.bar(df['Episode Number'], df['Notable Death Count'], color="#8B0000", alpha=0.6, label='Muertes')
ax1.set_xlabel('Número de episodio (total)')
ax1.set_ylabel('Muertes relevantes', color="#8B0000")
ax1.tick_params(axis='y', labelcolor="#8B0000")
ax2 = ax1.twinx()
ax2.plot(df['Episode Number'], df['US viewers (million)'], color="#4682B4", marker='o', label='Audiencia')
ax2.set_ylabel('Audiencia (millones)', color="#4682B4")
ax2.tick_params(axis='y', labelcolor="#4682B4")
plt.title('MUERTES RELEVANTES Y AUDIENCIA')
fig.tight_layout()
plt.savefig("../img/Muertes_relevantes_y_audiencia")

#3
df = df_epi_deaths.sort_values(by=["Season", "Number in Season"])
fig, ax1 = plt.subplots(figsize=(14, 6))
ax1.bar(df['Episode Number'], df['Notable Death Count'], color="#8B0000", alpha=0.6, label='Muertes')
ax1.set_xlabel('Número de episodio (total)')
ax1.set_ylabel('Muertes relevantes', color="#8B0000")
ax1.tick_params(axis='y', labelcolor="#8B0000")
ax2 = ax1.twinx()
ax2.plot(df['Episode Number'], df['Imdb Rating'], color="#4682B4", marker='o', label='Audiencia')
ax2.set_ylabel('Rating', color="#4682B4")
ax2.tick_params(axis='y', labelcolor="#4682B4")
plt.title('MUERTES RELEVANTES Y AUDIENCIA POR EPISODIO')
fig.tight_layout()
plt.savefig("../img/Muertes_relevantes_y_rating")

#4
muertes_por_episodio = df_epi_deaths.groupby("Number in Season")["Notable Death Count"].sum()
muertes_por_episodio.plot(kind="bar", figsize=(12, 6), color=GOTcolors)
plt.xlabel("Número de Episodio")
plt.ylabel("Muertes Notables")
plt.title("MUERTES RELEVANTES POR Nº DE EPISODIO")
plt.tight_layout()
plt.savefig("../img/Muertes_relevantes_por_episodio")

#5
num_barras = len(df_muertes_epi1_clean['Season'].value_counts())
df_muertes_epi1_clean['Season'].value_counts().sort_index().plot(
    kind='bar', 
    title='MUERTES RELEVANTES POR TEMPORADA',
    color=GOTcolors[:num_barras])
plt.xticks(rotation=0)
plt.savefig("../img/Muertes_relevantes_por_temporada")

num_barras = len(df_muertes_epi1['Season'].value_counts())

df_muertes_epi1['Season'].value_counts().sort_index().plot(
    kind='bar', 
    title='MUERTES GENERALES POR TEMPORADA',
    color=GOTcolors[:num_barras])
plt.xticks(rotation=0)
plt.savefig("../img/Muertes_generales_por_temporada")

df_muertes_epi2_clean['episode'].value_counts().sort_index().plot(kind='bar', title='MUERTES POR EPISODIOS AGRUPADOS', color = GOTcolors)
plt.savefig("../img/Muertes_episodios_agrupados")

#6
top_5_episodios = df_muertes_y_viewers.groupby("episode")["U.S. viewers(millions)"].mean().nlargest(5).index
top_df = df_muertes_y_viewers[df_muertes_y_viewers["episode"].isin(top_5_episodios)]
metodos_top5 = top_df["method_cat"].value_counts().head(5)
plt.figure(figsize=(8,5))
metodos_top5.plot(kind="bar", color=GOTcolors)
plt.title("TOP 5 MÉTODOS Y EPISODIOS")
plt.xlabel("Método de muerte")
plt.ylabel("Frecuencia")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../img/Top5_metodos_episodios")

df_filtrado = df_muertes_y_viewers[~df_muertes_y_viewers["method_cat"].isin(["Unknown", "Other"])]
top_5_episodios = df_filtrado.groupby("episode")["U.S. viewers(millions)"].mean().nlargest(5).index
top_df = df_filtrado[df_filtrado["episode"].isin(top_5_episodios)]
metodos_top5 = top_df["method_cat"].value_counts().head(5)
plt.figure(figsize=(8,5))
metodos_top5.plot(kind="bar", color=GOTcolors)
plt.title("TOP 5 MÉTODOS Y EPISODIOS II")
plt.xlabel("Método de muerte")
plt.ylabel("Frecuencia")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../img/Top5_metodos_episodios_II")


#HIPÓTESIS 2
#1
plt.figure(figsize=(12, 6))
plt.plot(df_episodes_clean['No. of Episode (Overall)'], df_episodes_clean['Metacritic Ratings'], 
         color='#4682B4', alpha=0.6, label='Metacritic', linewidth=2)
plt.plot(df_episodes_clean['No. of Episode (Overall)'], df_episodes_clean['Rotten Tomatoes Rating'], 
         color='#8B0000', alpha=0.6, label='Rotten Tomatoes', linewidth=2)
plt.plot(df_episodes_clean['No. of Episode (Overall)'], df_episodes_clean['IMDb Rating'], 
         color='#DAA520', alpha=0.6, label='IMDb', linewidth=2)
plt.xlabel('Episodio')
plt.ylabel('Valoración (escala 0–10)')
plt.title('RATINGS EPISODIOS')
plt.legend()
plt.tight_layout()
plt.savefig("../img/RATINGS EPISODIOS")

#2
df_episodes_clean["Average Rating"] = df_episodes_clean[["IMDb Rating", "Metacritic Ratings", "Rotten Tomatoes Rating"]].mean(axis=1)
df_episodes_clean.to_csv("../data_clean/df_episodes_clean.csv", index=False)
plt.figure(figsize=(12, 6))
plt.plot(df_episodes_clean['No. of Episode (Overall)'], df_episodes_clean['Average Rating'], 
         color="#1C1C1C", alpha=1, label='Average Rating', linewidth=2)
plt.xlabel('Episodio')
plt.ylabel('puntuación 1-10')
plt.title('RATING MEDIO')
plt.legend()
plt.tight_layout()
plt.savefig("../img/Rating_medio")

#4
plt.figure(figsize=(12, 6))
plt.plot(df_episodes_clean['No. of Episode (Overall)'], df_episodes_clean['U.S. Viewers (Millions)'], 
         color="#8B0000", alpha=1, label='U.S. Viewers', linewidth=2)
plt.xlabel('Episodio')
plt.ylabel('Espectadores (millones)')
plt.title('AUDIENCIA')
plt.legend()
plt.tight_layout()
plt.savefig("../img/Audiencia")


#HIPÓTESIS 3
#1
df_muertes_epi1_clean['Killer'] \
    .value_counts() \
    .head(10) \
    .plot(kind='barh',
          color=GOTcolors,
          title='TOP 10 ASESINOS (RELEVANTES)')
plt.xlabel('Número de muertes')
plt.ylabel('Asesinos')
plt.tight_layout()
plt.savefig("../img/Top10_asesinos_relevantes")

df_muertes_epi1_clean['Method'] \
    .value_counts() \
    .head(10) \
    .plot(kind='barh',
          color=GOTcolors,
          title='MÉTODO ASESINATO (RELEVANTES)')
plt.xlabel('Veces usado')
plt.ylabel('Método')
plt.tight_layout()
heatmap_data = df_muertes_epi1_clean.pivot_table(index='Killer', columns='Method', aggfunc='size', fill_value=0)
plt.savefig("../img/Metodo_asesinato_relevantes")

df_muertes_epi1['Killer'] \
    .value_counts() \
    .head(10) \
    .plot(kind='barh',
          color=GOTcolors,
          title='TOP 10 ASESINOS(GENERAL)')
plt.xlabel('Número de muertes')
plt.ylabel('Asesinos')
plt.tight_layout()
plt.savefig("../img/Top10_asesinos_general")

df_muertes_epi1['Method'] \
    .value_counts() \
    .head(10) \
    .plot(kind='barh',
          color=GOTcolors,
          title='MÉTODO ASESINATO (GENERAL)')
plt.xlabel('Veces usado')
plt.ylabel('Método')
plt.tight_layout()
plt.savefig("../img/Metodo_asesinato_general")

#2
df_muertes_epi1['Killers House'] \
    .value_counts() \
    .head(10) \
    .plot(kind='barh',
          color=GOTcolors,
          title='MUERTES POR CASA DEL ASESINO')
plt.xlabel('Número de muertes')
plt.tight_layout()
plt.savefig("../img/Muertes_casa_asesino")


#HIPÓTESIS 4
#1
df_batallas_outcome = df_battles_clean.dropna(subset=["attacker_outcome"])
conteo_resultados = df_batallas_outcome["attacker_outcome"].value_counts()
conteo_resultados.plot(kind="bar", color=["#8B0000","#4682B4"])
plt.title("¿GANA MÁS EL ATACANTE O EL DEFENSOR?")
plt.xticks(rotation=0)
plt.ylabel("Número de batallas")
plt.xlabel("Resultado para el atacante")
plt.savefig("../img/ganador")

#2
df_batallas_ejer = df_battles_clean.dropna(subset=["attacker_size", "defender_size", "attacker_outcome"])

condicion_attacker = df_batallas_ejer["attacker_size"] > df_batallas_ejer["defender_size"]
condicion_defender = df_batallas_ejer["attacker_size"] < df_batallas_ejer["defender_size"]
condicion_empate = df_batallas_ejer["attacker_size"] == df_batallas_ejer["defender_size"]

df_batallas_ejer["mayor_ejercito"] = "empate"
df_batallas_ejer.loc[condicion_attacker, "mayor_ejercito"] = "attacker"
df_batallas_ejer.loc[condicion_defender, "mayor_ejercito"] = "defender"

df_batallas_ejer["ganador"] = df_batallas_ejer["attacker_outcome"].map({
    "win": "attacker",
    "loss": "defender"})

coinciden = df_batallas_ejer["mayor_ejercito"] == df_batallas_ejer["ganador"]
conteo = coinciden.value_counts().rename({
    True: "Ganó el mayor ejército",
    False: "Perdió el mayor ejército"})

plt.figure(figsize=(6,5))
sns.barplot(x=conteo.index, y=conteo.values, palette=["#013220", "#8B0000"])
plt.title("¿GANA EL EJÉRCITO MÁS GRANDE?")
plt.ylabel("Número de batallas")
plt.xlabel("")
plt.savefig("../img/tamanio_gana")

#3
data = df_battles["attacker_king"].value_counts()
my_circle=plt.Circle( (0,0),
                     0.7, 
                     color="white")
plt.figure(figsize=(8,8))
plt.pie(data.values,
        labels=data.index,
        colors=("#DAA520","#4682B4","#708090","#8B0000"),
        autopct='%1.2f%%')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.title("REY ATACANTE")
plt.savefig("../img/rey_atacante")


