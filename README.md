# ⚔👑**Análisis Juego de Tronos**👑⚔

![Texto alternativo](https://m.media-amazon.com/images/I/519IvvdDEUL._AC_UF894,1000_QL80_.jpg)

Juego de Tronos (o Game of Thrones en inglés) es una serie de televisión de fantasía medieval, basada en las novelas Canción de Hielo y Fuego de George R.R. Martin, que narra la lucha por el Trono de Hierro en Poniente, un continente ficticio. La trama se centra en las intrigas políticas, las alianzas cambiantes, las traiciones y las violentas batallas entre varias casas nobles por el control de los Siete Reinos. 

## 🗡Hipótesis🗡

El objetivo de este EDA es demostrar si existe relación entre el éxito de las temporadas y el número de muertes de personajes que se dan en las mismas. Se plantean las siguientes preguntas, a modo de guía para el desarrollo de este análisis:

❔¿Qué tendencia ha seguido la calidad de las temporadas?

❔¿Cuántos espectadores ha tenido la serie?¿Se ha mantenido dicho número?

❔¿Cuántas muertes ha habido en cada temporada?¿Y en cada episodio?

❔¿Qué tipo de muertes han tenido más audiencia?

❔¿Qué casa ha perdido más miembros relevantes?

❔¿Qué casa ha sido la que más ha matado?

## 💻Proceso💻

Para probar si esta hipótesis es correcta, se van a analizar datos de distintos datasets, disponibles en la carpeta [notebooks](https://github.com/NereaLdA/EDA-Game_of_Thrones_/tree/main/notebooks), a saber:

  1. **Batallas:** en este Dataframe encontramos una columna que indica el número de muertes relevantes por batalla. También se indican los atacantes y defensores, así como otros datos relacionados con las batallas. Podríamos relacionar datos con el capítulo, número de espectadores y rating de otros DataFrames
  2. **Episodes:** Aquí tenemos la lista completa de episodios, sus espectadores en EEUU y sus ratings según IMDb y ROtten Tomatoes
  3. **Episodios y muertes:** Aquí encontramos una relación entre episodios y muertes, así como sus ratings.
  4. **Muertes por episodio 1:** Aquí observamos una lista de personajes asesinados, así como por quién y cómo y dónde referenciados por episodio y temporada.
  5. **Muertes por episodio 2:** Además de la lista de episodios, también están reflejadas las muertes y su relevancia en la trama.
  6. **Viewers:** Aquí contamos con información extra sobre las visualizaciones de cada episodio en EEUU.

Por supuesto, en estos DataFrames hay mucha más información, aunque en una primera fase, la información más relevante para probar la hipótesis es la destacada anteriormente.
