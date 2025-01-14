from bs4 import BeautifulSoup

def read_html_with_beautiful_soup(file_path):
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Find all articles in the HTML
    articles = soup.find_all('a')

    for article in articles:
        parent = article.parent
        if parent.name == 'ul':
            parent = parent.parent
        
        print(parent)

# File path
html_file_path = 'data/0005205103/2008-08-14_AP-radioactif_pixtral.html'

read_html_with_beautiful_soup(html_file_path)
