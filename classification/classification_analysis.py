import json
from collections import defaultdict
from pprint import pprint

def analyse_classification(classification_path: str):
    """Read  documents"""

    number_of_mentions_by_action = defaultdict(int)

    # open the source json
    with open(classification_path) as f:
        data:dict[str, dict[str, dict[str, str]]] = json.load(f)

        for mentions in data.values():
            for mention in mentions.values():
                action = mention["action"]
                number_of_mentions_by_action[action] += 1
                number_of_mentions_by_action["Total"] += 1

    # Proportion of undefined results
    number_of_mentions_by_action["Proportion indéfinis"] = number_of_mentions_by_action["Indéfini"] / number_of_mentions_by_action["Total"]
    
    pprint(dict(number_of_mentions_by_action))

analyse_classification("./classification.json")