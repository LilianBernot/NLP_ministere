from bs4 import BeautifulSoup
import json
import os

def read_html_with_beautiful_soup(file_path):
    """Read an html document with beautiful soup"""
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Find all articles in the HTML
    articles = soup.find_all('a')
    
    clean_articles = []

    for article in articles:
        # Find the parent of the article
        parent = article.parent
        if parent.name == 'ul':
            parent = parent.parent
        
        # Delete divs with "VU"
        full_text = parent.get_text(strip=True)  # Strips leading and trailing spaces
        first_two_letters = full_text[:2]
        if first_two_letters != "VU":
            clean_articles.append(parent)

    return clean_articles

def store_htmls(htmls_to_store, store_path='target_divs.json'): 
    """Store given htmls in a json document"""

    # Get divs contents
    # We delete multiple spaces and special characters like \n
    div_contents = [' '.join(div.get_text(strip=True).strip().split()) for div in htmls_to_store]

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
                htmls_to_store += read_html_with_beautiful_soup(cur_path + file_name)


    store_htmls(htmls_to_store)

read_multiple_html()