# Detecting modification segments

References to other texts are inserted in the HTML document with ```<a>``` tags.

At the beginning of every document, we got "VU" stuff -> to delete.

For others : 
- get the higher-level tag to find context 
- get ```<lu>``` and then ```<div>``` containing it to get context
Quite often, just cited -> ```<a>``` within a normal text which is directly a ```<div>```

When applicable, got : 
    - context = applicables
    - list of articles 
    - article : named and little description behind


Substitutions : 
- data/0005205103/2023-10-16_AP-auto_modificatif_pixtral.html
- data/0005205103/2016-03-02_APC-auto_pixtral.html
- data/0005302750/2022-11-07_APC-auto_pixtral.html

In both cases, chapitre name is "ABROGATION DE DISPOSITIONS ANTERIEURES".


TODO : 
- [x] extract all mentioned articles with code 
- [x] create syntax to delete some like "VU" : 1525 -> 944 mentions
- better parsing and storing : 
    - [x] store by arrêté 
    - [x]clean the texts : space before and after dates
    - [x] store mentions by the mentionned article. Structure should be like 
    - [] store by article inside the arrêté : hard. Should investigate more on the structure of the html files.
    - [] storage : for the listed stuff, maybe group them under a same big "multiple mentions". Or, don't take all elements within the mention but only the parent + the current article. I prefer first solution
- [] category detection : implement that
- documentation : 
    - [x] add PDFs to the repo to explain subjects
    - [] write in readme : "For now, htmls are parsed in the following format : ```mentioning_article : { mentioned_article : text, ...}``` ..."
    - [] add in the readme : project in french because... -> still part to translate
    - [x] add in the readme : differentiate folders between project 1 and project 2


# Catégories potentielles

## Recherches sur le corpus 

Vocabulary : 
- applicable / application
- déterminée selon les indications de ...
- prévu à l'article/l'annexe ...
- conformément aux dispositions de ...
- selon la méthode définie en
- visés par ...
- définies conformément à ...
- respectent les prescriptions de
- complété

## Recherches personnelles
Modification partielle d’un article :
- Mots-clés indicateurs : "modifié", "complété", "amendé", "ajouté".
- Structure fréquente : "L'article X est modifié comme suit...".

Mention d’un article sans modification :
- Mots-clés indicateurs : "conformément à", "en application de", "prévu par".
- Structure fréquente : "Conformément à l'article X...".

Substitution complète d’un article :
- Mots-clés indicateurs : "remplacé", "abrogé", "substitué".
- Structure fréquente : "L'article X est remplacé par..." ou "L'article X est abrogé".

Création d’un nouvel article :
- Mots-clés indicateurs : "inséré", "ajouté", "créé".
- Structure fréquente : "Un article X bis est inséré...".

Référencement d’un article sans action :
- Mots-clés indicateurs : "comme indiqué dans", "mentionné dans".
- Structure fréquente : "L'article X précise que...".