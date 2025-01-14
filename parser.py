from bs4 import BeautifulSoup
import json
import os
import re

def read_html_with_beautiful_soup(file_path):
    """Read an html document with beautiful soup"""
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Find all articles in the HTML
    articles = soup.find_all('a')
    
    # When we have lists of articles in the same div, we want to study them only once
    clean_articles = set()

    for article in articles:
        # Find the parent of the article
        parent = article.parent
        if parent.name == 'ul':
            parent = parent.parent
        
        # Delete divs with "VU"
        full_text:str = parent.get_text(strip=True)  # Strips leading and trailing spaces
        first_two_letters = full_text[:2].lower()
        if first_two_letters != "vu":
            clean_articles.add(parent)

    return clean_articles

def store_htmls(htmls_to_store, store_path='target_divs.json'): 
    """Store given htmls in a json document"""

    def clean_text(text):
        parsed_text = ' '.join(text.get_text().strip().split()) # Remove multiple spaces
        fixed_text = re.sub(r"'\s+", "'", parsed_text)  # Remove space after apostrophe
        fixed_text = re.sub(r"\s+,", ",", fixed_text)  # Remove space before comma
        
        return fixed_text

    div_contents = [clean_text(div) for div in htmls_to_store]

    # Write the contents to a json file
    with open(store_path, 'w', encoding='utf-8') as file:
        json.dump(div_contents, file, ensure_ascii=False, indent=4)


def read_multiple_html():
    """Read all html documents"""
    
    path = "./data"
    dirs = os.listdir( path )

    htmls_to_store = []

    for dir in dirs:
        file_names = os.listdir( path + "/" + dir )
        cur_path = path + "/" + dir + "/" 
        for file_name in file_names:
            if file_name[-5:] == ".html":
                htmls_to_store += list(read_html_with_beautiful_soup(cur_path + file_name))


    store_htmls(htmls_to_store)

read_multiple_html()