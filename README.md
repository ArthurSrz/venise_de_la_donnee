# La Venise de la donnée perdue

La Venise de la donnée (perdue) est un jeu interactif pour montrer à quel point des données non-ouvertes peuvent rendre la connaissance d'un territoire très (très). 

## Il était une fois...

Un honnête citoyen qui souhaite récupérer les données sur la localisation de panneaux dans le but de venir enrichier une cartographie collaborative. Comme la loi lui permet, il faut une demande à la collectivité, qui, au cours d'un échange courtois, lui propose de "sortir de chez soi et d'ouvrir les yeux"

<img width="544" alt="Screenshot 2023-09-29 at 03 26 08" src="https://github.com/ArthurSrz/venise_de_la_donnee/assets/55806298/49bb3154-c985-470d-87a9-cc58cc34fa70">

Malheureusement, l'honnête citoyen se trouve être aveugle et dépourvu de jambes 😢 (ceci relève plus de la fiction que de la réalité). 

![](https://media.giphy.com/media/fWfG9QbOMT1vddOVto/giphy.gif)

Comment peut-il contribuer à la cartographie ? 

## La génèse complexe du jeu "La Venise des données"

Désespéré, il fait une demande grâce à son ordinateur adapté au service juridique de la collectivité qui lui envoie la délibération au format .pdf sur les dits panneaux (ceci relève plus de la réalité que de la fiction, le fichier est [ici](https://github.com/ArthurSrz/venise_de_la_donnee/blob/main/donnees_cada.pdf)). 

Un fichier illisible, dans un standard non-ouvert. Comment notre citoyen aveugle et sans jambes peut-il faire pour contribuer à la carte collaborative ? 

Il se décide à créer le jeu de données à partir du .pdf. Pour cela il suit ce process lent et complexe. Mais après tout, on a du temps quand on est aveugle et sans jambes : 

* Grâce à [Tabula](https://tabula.technology/), il transforme le tableau dans le .pdf en fichier .csv
* Puis, il fait intervenir [Open interpreter](https://openinterpreter.com/) pour programmer rapidement un programme python qui va :
  - extraire les noms des rues dans le fichier
  - geocoder approximativement l'emplacement des rues
  - ajouter ces infos dans le fichier d'origina
* Il va positionner les points créés sur une carte grâce à la [librarie folium](https://python-visualization.github.io/folium/latest/)

Et c'est là qu'il a l'idée du jeu de la Venise de la donnée perdue. 

## Mode d'emploi du jeu 


