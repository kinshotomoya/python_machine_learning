import requests
import webbrowser
import time
from bs4 import BeautifulSoup
from selenium import webdriver  #seleniumは、ウェブブラウザを操作するソフトウェア。画面をスクロールなどの操作ができる


host_url = 'https://newspicks.com/'


def get_url_array(host_url):
    driver = webdriver.PhantomJS() # PhantomJSをドライバーとして扱うことによって、JSを考慮してウェブページを扱える
    driver.get(host_url)
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find_all("a", attrs={"classs": "user-selected-link"}) #NewsPicksでは、このクラス名が記事リンクになっている
    urls = [get_url(article) for article in articles]
    uniq_urls = list(set(urls))
    print(uniq_urls)
    return uniq_urls

def get_url(article):
    href = article.get('href')
    url = f"{host_url}{href}"
    return url

def display_url(urls):
    for url in urls:
        webbrowser.open(url)


urls = get_url_array(host_url)
display_url(urls)
