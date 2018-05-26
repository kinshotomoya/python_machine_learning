# Google検索・スクレイピング
import requests
import webbrowser
from bs4 import BeautifulSoup
from googlesearch import search

def google_search(word, limit):
    print(word)
    target_web_urls = search(word, lang='ja', stop=limit)
    for web_url in target_web_urls:
        print(web_url)
        try:
            get_image(web_url)
        except:
            print('そのURlからは画像は取得できません')

def get_image(web_url):
    response = requests.get(web_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all("img")
    i = 0
    for image in images:
        i += 1
        if i > 11:
            break
        image_url = image.get('src')
        webbrowser.open(image_url)

google_search(' 画像' + ' -naver -twitter', 10)
