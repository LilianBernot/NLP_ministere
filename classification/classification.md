# Détection de catégories

## Description du projet

Ce projet a pour but de réaliser un premier classificateur pour les textes obtenus grâce au projet de parsing.  

Il contient les fichiers suivants : 
- ```classification.py``` : qui contient l'algorithme de classification.
- ```classification_analysis.py``` : qui contient un algorithme pour analyses la classification.
- ```classification.json``` : l'output du code appliqué au corpus parsé.

La classification est faite en analysant si un texte contient ou non un mot de vocabulaire que l'on a défini comme classifiant. Exemple : si l'on voit le mot "conformément" dans un texte, on considère que l'article mentionné fait objet d'une simple mention. On n'est pas en train de l'amander ou de l'abroger mais simplement de le citer ou de montrer qu'on en applique un principe.

Le fichier créé par le classificateur prend à peu près la forme de celui du parsing, à ceci près que l'on ajoute pour chaque article mentionné, l'action classifiée au texte : 
```
{
    mentioning_article : { 
        mentioned_article : {
            "mention": text, 
            "action": detected action,
        }
        ...
        },
    ...
}
```

## Limites et évolutions du projet

On verra dans la partie d'analyses que les résultats sont relativement mauvais. On notera notamment le taux de 84% de mentions du corpus dont l'action n'est pas qualifiée. 

Il conviendrait pour faire avancer ce projet d'utiliser des outils de nlp pour pouvoir analyser plus précisément chacune des mentions et être plus robuste. Le projet s'arrêtera ici. Il avait pous but initial de jouer avec les résultats du parsing pour voir un peu de quoi il en retournait. On notera notamment que l'on a soulevé ici des erreurs dans le parsing telles que les mots qui sont "coupés", séparés en deux parties par un espace qui n'a pas lieu d'être.

## Run the project

To run the project, run : ```python classification.py```.

You can analyse the results with : ```python classification_analysis.py```. It will print a formatted ouput.


# Analyses de résultats

## Résultats d'occurence

Voici les résultats d'occurence des différentes actions après classification : 

```
{
   'Abrogation': 9,
   'Indéfini': 545,
   'Modification partielle': 17,
   'Simple mention': 74,
   'Substitution totale': 4,
   'Proportion actions indéfinies': 0.8397534668721109,
   'Total': 649
}
```

On notera ici la grande propotion d'actions indéfinies par notre système.

## Quelques réussites

Je mentionnerai ici quelques exemples de réussite du système, donnant des résultats attendus : 


```
INPUT
>>> "arrêté préfectoral du 2 mars 2016": "Suivant les conclusions de ce bilan, une mise à jour du programme de contrôle des émissions atmosphériques, prescrit notamment à l’article 8.2.1.1 « Auto surveillance des rejets atmosphériques » de l’ arrêté préfectoral du 2 mars 2016, pourra être proposée par l’exploitant.",

OUTPUT
>>> Text: arrêté préfectoral du 2 mars 2016
    Action: Modification partielle
```

```
INPUT
>>> "arrêté du 2 février 1998": "Conformément à l’article L.514-8 du code de l’environnement et à l’article 58 de l’ arrêté du 2 février 1998 l’inspection des installations classées se réserve également la possibilité de faire procéder, aux frais de l’exploitant, à des mesures de contrôle au niveau des points de rejets par un organisme extérieur sur les substances identifiées par l’exploitant comme sur d’autres substances non encore réglementées par un arrêté préfectoral ou ministériel applicable à l’établissement.",

OUTPUT
>>> Text: arrêté du 2 février 1998
    Action: Simple mention
```

## Manque de vocabulaire

On notera notamment que le vocabulaire défini ici l'a été grâce à une lecture non exhaustive des textes proposés. Le système serait alors très sensible à la façon dont les phrases sont tournées et au vocabulaire utilisé.

Dans l'exemple suivant on aimerait avoir un retour nous disant que la mention est simple, sans modification :

```
INPUT
>>> "arrêté ministériel du 2 février 1998": "Pour les substances identifiées à l’article 3.3 présentées une des 10 classes de danger pour la santé au sens du règlement CLP (règlement (CE) n°1272/2008 modifié), ou celles visées à l’article 27.7 b) ou c) de l’ arrêté ministériel du 2 février 1998 . L’exploitant tient à disposition de l’inspection un bilan établi de la substance considérée en vertu du 6ième point de l’article 4.1. Ce bilan identifie les émissions dans l’environnement (eau, air, déchets) de la substance, il compare la quantité émise calculée avec des mesures à l’émission. L’exploitant informe sans délai l’inspection des installations classées lorsque toute incertitude est susceptible d’engendrer un dépassement de seuil réglementaire ou qu’une émission est susceptible d’avoir un impact sanitaire.",

OUTPUT
>>> Text: arrêté ministériel du 2 février 1998
    Action: Indéfini
```


## Robustess

On constate notamment que le parsing n'a, pour certains textes, pas été parfait. On note notamment des mots qui ont des espaces qui ne devraient pas avoir : regarder le mot "remplac és" dans l'exemple suivant. Ces mots vont difficilement être détectés par notre système et dans ce cas précis, pas détecté du tout. L'action associée sera donnée comme indéfinie.

```
INPUT
>>> "arrêté préfectoral n° 5103/2016/03 du 2 mars 2016": "Les articles 3.2.5 et 8.2.1 de l’ arrêté préfectoral n° 5103/2016/03 du 2 mars 2016 sont remplac és respectivement par les annexes 1 et 2 du présent arrêté",

OUTPUT
>>> Text: arrêté préfectoral n° 5103/2016/03 du 2 mars 2016
    Action: Indéfini
```

# Catégorisation

## Catégories de mention d'articles
1. Simple mention :  
   Le texte fait uniquement référence à un article sans en altérer le contenu.  
   Exemple :  
   - "L’exploitant utilise l’ensemble des résultats issus de son programme d’autosurveillance précis à l’article 8.2.1.1 de l’arrêté préfectoral du2 mars 2016..."
   - "Conformément à l’article L.514-8 du code de l’environnement et à l’article 58 de l’arrêté du2 février 1998..."

2. Modification partielle :  
   Le texte indique explicitement que l’article est modifié, généralement en précisant la nature de la modification (par un autre article ou arrêté).  
   Exemple :  
   - "article 3.7 « Valeurs limites d’émissions dans l’air » de l’arrêté préfectoral n° 09/IC/01 du6 janvier 2009, modifié par l’article 4 de l’arrêté préfectoral n° 8378/2016/04..."
   - "Les dispositions de l'article 7.3 de l'arrêté préfectoral n° 5103/19/38 du08 août 2019 sont abrogées et remplacées par celles du présent arrêté."

3. Substitution totale :  
   Le texte remplace intégralement un ou plusieurs articles par de nouvelles dispositions.  
   Exemple :  
   - "Les articles 3.2.5 et 8.2.1 de l’arrêté préfectoral n° 5103/2016/03 du2 mars 2016 sont remplacés respectivement par les annexes 1 et 2 du présent arrêté."

4. Abrogation :  
   Le texte supprime explicitement les dispositions d’un article.  
   Exemple :  
   - "Les dispositions de l'article 7.3 de l'arrêté préfectoral n° 5103/19/38 du08 août 2019 sont abrogées..."


## Règles d’identification
1. Simple mention :  
    - "Conformément à l’article..."
    - "Comme le prévoit l’article..."
    - "Cité à l’article..."  

2. Modification partielle :  
    - "modifié par l’article..."  
    - "modification de l’article..."  
    - "mise à jour de l’article..."  

3. Substitution totale :  
    - "remplacé par..."  
    - "remplacés respectivement par..."  
    - "intégralement remplacé par..."  

4. Abrogation :  
    - "abrogé..."  
    - "abrogées et remplacées par..."  