from bs4 import BeautifulSoup
import requests

KEYWORDS = ['Python', 'Windows', 'Facebook', 'Дизайн', 'Linux']


# Задание 1
url = 'https://habr.com/ru/all/'
headers = {
    'Accept': '*/*',
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
}
resp = requests.get(url, headers=headers)

soup = BeautifulSoup(resp.text, 'lxml')

articles = soup.find_all(class_="tm-articles-list__item")

for article in articles:
    pub_date = article.find('time').get('title')
    # print(pub_date)
    title = article.find(class_='tm-article-snippet__title-link')
    if title == None:
        article_title = article.find(class_="tm-megapost-snippet__title").text
    else:
        article_title = title.text
    first_url = 'https://habr.com'
    second_url = article.find(class_='tm-article-snippet__title-link')
    if second_url == None:
        mega_url = article.find(class_="tm-megapost-snippet__link")
        href = first_url + mega_url.get('href')
        # print(href)
    else:
        href = first_url + second_url.get('href')
    # for key in KEYWORDS:
    #     if key in article.text:
    #         print(f"< {pub_date} >-< {article_title} >-< {href} >")
    #         print('='*90)


# Задание 2
url = 'https://habr.com/ru/all/'
headers = {
    'Accept': '*/*',
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
}
resp = requests.get(url, headers=headers)

soup = BeautifulSoup(resp.text, 'html.parser')

articles = soup.find_all(class_="tm-articles-list__item")


for article in articles:
    pub_date = article.find('time').get('title')
    # print(pub_date)
    title = article.find(class_='tm-article-snippet__title-link')
    if title == None:
        article_title = article.find(class_="tm-megapost-snippet__title").text
    else:
        article_title = title.text
    # print(article_title)
    first = 'https://habr.com'
    second = article.find(class_='tm-article-snippet__title-link')
    if second == None:
        mega_second = article.find(class_="tm-megapost-snippet__link").get('href')
        link = first + mega_second
    else:
        link = first + second.get('href')
    # print(link)
    response = requests.get(link, headers=headers)
    art_soup = BeautifulSoup(response.text, 'html.parser')
    full_article = art_soup.find(class_="tm-article-presenter__content")
    for key in KEYWORDS:
        if full_article != None:
            if key in full_article.text:
                print(f"< {pub_date} >-< {article_title} >-< {link} >")
                print('='*90)
        else:
            if key in art_soup.find(class_="tm-layout__container").text:
                print(f"< {pub_date} >-< {article_title} >-< {link} >")
                print('=' * 90)