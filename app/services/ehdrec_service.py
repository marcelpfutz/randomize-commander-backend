import requests
from bs4 import BeautifulSoup

def get_edh_data(commander):
    link = 'https://edhrec.com/commanders/' + commander
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'}
    request_data = requests.get(link, headers=headers)

    data = BeautifulSoup(request_data.text, 'html.parser')
    all = data.find(class_='NavigationPanel_tags__M9VjI')

    results = []
    for item in all:
        label = item.find(class_='NavigationPanel_label__xMLz1').get_text()
        href = item['href']
        results.append((label, href))

    return results