from bs4 import BeautifulSoup
from bs4.element import ResultSet
from bs4.element import Tag
import json
import os
import re


def clean_text(text : Tag) -> str:
    """Cleans the text of a beautiful soup object.

    Arguments :
        text : a BeautifulSoup object

    Returns : cleand text
    """
    parsed_text = ' '.join(text.get_text().strip().split()) # Remove multiple spaces
    fixed_text = re.sub(r"'\s+", "'", parsed_text)  # Remove space after apostrophe
    fixed_text = re.sub(r"\s+,", ",", fixed_text)  # Remove space before comma
    
    return fixed_text


def read_html_with_beautiful_soup(file_path:str) -> dict:
    """Read an html document with beautiful soup"""
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Find all articles in the HTML
    articles: ResultSet[Tag] = soup.find_all('a')
    
    # When we have lists of articles in the same div, we want to study them only once
    clean_articles = dict()

    for article in articles:
        article_name = clean_text(article)

        # Find the parent of the article
        parent = article.parent
        if parent:
            if parent.name == 'ul' and parent.parent:
                parent = parent.parent
    
            # Delete divs with "VU"
            full_text = clean_text(parent)
            
            first_two_letters = full_text[:2].lower()
            if first_two_letters != "vu":
                clean_articles[article_name] = full_text
                #/!\ WARNING : now, articles are duplicated because they have different keys

    return clean_articles

def store_htmls(htmls_to_store:dict[str, dict], store_path:str): 
    """Store given htmls in a json document"""

    with open(store_path, 'w', encoding='utf-8') as file:
        json.dump(htmls_to_store, file, ensure_ascii=False, indent=4)


def read_multiple_html(store_path: str):
    """Read all html documents"""
    
    path = "./data"
    dirs = os.listdir( path )

    htmls_to_store:dict[str, dict] = dict()

    for dir in dirs:
        file_names = os.listdir( path + "/" + dir )
        cur_path = path + "/" + dir + "/" 
        for file_name in file_names:
            if file_name[-5:] == ".html":
                htmls_to_store[file_name] = read_html_with_beautiful_soup(cur_path + file_name)

    store_htmls(htmls_to_store, store_path=store_path)

read_multiple_html(store_path='target_divs.json')