import requests
import json
import datetime
import io
from bs4 import BeautifulSoup

url = 'https://novayagazeta.ru/stories'
path = "articles.json"

def get_html_page(url):
    return requests.get(url)


def find_articles(html_page):

    soup = BeautifulSoup(html_page, 'html.parser')
    soup = soup.find_all('h2')
    headers = [header.get_text() for header in soup]
    articles = [{"title": header} for header in headers]
    return articles


def publish_report(path, articles):
    report = {"url": url,
              "creationDate": datetime.datetime.now().strftime("%Y-%m-%d"),
              "articles": articles}


    with io.open(path, 'w', encoding='utf8') as json_file:
        json.dump(report, json_file, ensure_ascii=False)
        return path


html_page = get_html_page(url)
articles = find_articles(html_page.text)
publish_report(path, articles)
