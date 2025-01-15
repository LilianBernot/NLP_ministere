# Parsing   

This folder regroups research done for the project n°2. The goal is to parse the raw files to get the mentions of other articles.

## Run the code

To run the code : ```python parsing.py```.

The output file will be ```target_divs.json``` by default.

## Project description

The code first retrieves all the html elements in the ```<a>``` tags.
For each of those elements, we retrieve the parent element, to get the context around the mention.

The output of the code is a json file that will store data as a dictionary. The keys of the dictionary are the names of the html files that are being parsed. The corresponding values are dictionaries that have, as keys, the mentioned articles names, and as values, the context of the mention : 
```
{
    mentioning_article : { 
        mentioned_article : text, 
        ...
        },
    ...
}
```

## Potential improvement

We could store by article inside the arrêté instead of the arrêté itself. 

For now, we store the mentions by the file name (meaning the arrêté name), not the specified article inside the file. Let's imagine a file, named arrete_x. There, I have an article a.b that is referring to another article c.d. In my storage, I will have : ```"arrete_x": "context with article a.b inside"```. I might prefer having : ```"article a.b": "context with article c.d inside"```.

## Implementation choice

One big choice has been done while retrieving mentioned articles that are part of a list. Let's take the following example : ```data/0003013459/2020-04-20_AP-auto_initial_pixtral.html```.

In this example, we can see the citation of multiple articles all at once. Here, it is just a mention but in some others files we might have a different action, like modification or deletion. In that case, I thought about grouping the mentions all together, but I finally chose not to do anything special. Mentions will be stored the same way as the others and will appear multiple times in the output file : multiple keys (all the mentioned articles), will have the same value.

<h4 class="dsr-section_title">
    ARTICLE 1.6.1. REGLEMENTATION APPLICABLE
</h4>
<div class="dsr-alinea" data-number="1">
Sans préjudice de la réglementation en vigueur, sont notamment applicables à l'établissement les prescriptions qui le concernent des textes cités ci-dessus (liste non exhaustive) :
    <ul>
        <li>
            <a class="dsr-arrete_reference" data-authority="ministériel">
            arrêté
            ministériel
            du
            <time class="dsr-date" datetime="1997-01-23">
            23 janvier 1997
            </time>
            </a>
            relatif à la limitation des bruits émis dans l'environnement par les installations classées pour la protection de l'environnement ;
        </li>
        <li>
            <a class="dsr-arrete_reference" data-authority="ministériel">
            arrêté
            ministériel
            du
            <time class="dsr-date" datetime="1998-02-02">
            02 février 1998
            </time>
            modifié
            </a>
            relatif aux prélèvements et à la consommation d'eau ainsi qu'aux émissions de toute nature des installations classées pour la protection de l'environnement soumises à autorisation ;
        </li>
        ...
    </ul>
</div>

