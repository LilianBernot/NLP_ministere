import re

def classify_texts(texts):
    """
    Classify each text based on its mention or modification of articles.

    Args:
        texts (list of str): List of texts to classify.

    Returns:
        list of dict: Each dictionary contains the original text, 
                      the detected action (mention, modification, substitution, abrogation, undefined), 
                      and the referenced articles.
    """
    classifications = []

    # Patterns for article references and actions
    article_pattern = re.compile(r'article\s\d+(\.\d+)*', re.IGNORECASE)
    mention_keywords = ["conformément", "comme le prévoit", "cité"]
    modification_keywords = ["modifié par", "mise à jour"]
    substitution_keywords = ["remplacé par", "remplacés respectivement par"]
    abrogation_keywords = ["abrogé", "abrogées"]

    for index, text in enumerate(texts):
        # Extract referenced articles
        mentionned_articles = article_pattern.findall(text)

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

        # Append results
        classifications.append({
            "text_id": index,
            "action": action,
            "articles": mentionned_articles
        })

    return classifications

# Example texts
texts = [
    "L’exploitant utilise l’ensemble des résultats issus de son programme d’autosurveillance précis à l’article 8.2.1.1 de l’arrêté préfectoral du2 mars 2016...",
    "article 3.7 modifié par l’article 4 de l’arrêté préfectoral...",
    "Les articles 3.2.5 et 8.2.1 sont remplacés respectivement par les annexes 1 et 2...",
    "Les dispositions de l'article 7.3 sont abrogées et remplacées...",
]

# Classify the texts
results = classify_texts(texts)

# Print results
for result in results:
    print(f"Text: {result['text']}")
    print(f"Action: {result['action']}")
    print(f"Referenced Articles: {result['articles']}")
    print("-")
