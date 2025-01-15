import json
from collections import defaultdict

def classify_text(text: str) -> str:
    """
    Classify the text based on its mention or modification of articles.

    Args:
        texts (str): A text to classify.

    Returns:
        the detected action (mention, modification, substitution, abrogation, undefined), 
    """

    # Patterns for sactions
    mention_keywords = ["conformément", "comme le prévoit", "cité"]
    modification_keywords = ["modifié par", "mise à jour"]
    substitution_keywords = ["remplacé par", "remplacés respectivement par"]
    abrogation_keywords = ["abrogé", "abrogées"]

    # Classify action based on keywords
    if any(keyword in text.lower() for keyword in abrogation_keywords):
        action = "Abrogation"
    elif any(keyword in text.lower() for keyword in substitution_keywords):
        action = "Substitution totale"
    elif any(keyword in text.lower() for keyword in modification_keywords):
        action = "Modification partielle"
    elif any(keyword in text.lower() for keyword in mention_keywords):
        action = "Simple mention"
    else:
        action = "Indéfini"

    return action


def store_classifications(classifications_to_store:dict[str, dict], store_path:str): 
    """Store given classification in a json document"""

    with open(store_path, 'w', encoding='utf-8') as file:
        json.dump(classifications_to_store, file, ensure_ascii=False, indent=4)


def classify_parsing_output(parsing_output_path: str, store_path:str):
    """Read the parsing output document"""

    classifications_to_store:defaultdict[str, dict[str, dict[str, str]]] = defaultdict(dict)

    # open the source json
    with open(parsing_output_path) as f:
        data:dict[str, dict[str, str]] = json.load(f)

        # for each document and for each mentioned article, classify the text
        for document_name, mentions in data.items():
            for article_name, mention in mentions.items():
                action = classify_text(mention)

                classifications_to_store[document_name][article_name] = {
                    "mention" : mention,
                    "action": action,
                }

    store_classifications(classifications_to_store, store_path=store_path)

classify_parsing_output(
    parsing_output_path="../parsing/target_divs_by_target.json",
    store_path="./classification.json"
)