import os
from os.path import join, dirname
from dotenv import load_dotenv 
import requests
import math
import urllib
import http.client
import json


def get_headers(subscriptionKey):
    return {"Ocp-Apim-Subscription-Key" : subscriptionKey}


def get_params(searchTerm, required_image_num):
    return {
        "q": searchTerm,
        "license": "All",
        "imageType": "photo",
        "count": required_image_num,
        "mkt": "ja-JP"
    }


def get_images_url_array(search_url, headers, params):
    response = requests.get(search_url, headers=headers, params=params)
    search_results = response.json()
    print(search_results)
    return [image['thumbnailUrl'] for image in search_results['value']]


def down_load_images(thumbnail_url_array, file_name):
    index = 0
    for image_url in thumbnail_url_array:
        res = requests.get(image_url)
        if 'image' not in res.headers['content-type']:
            print('画像ではないので、保存しません')
        save_image(res.url, make_file_name(index, file_name))
        index += 1


# 画像を保存するメソッド
def save_image(url, file_name):
    # urlretrieveメソッドは、頻繁に使われる
    # 参考ドキュメント: https://momokogumi.com/urllib
    urllib.request.urlretrieve(url, "images/" + file_name)


# それぞれの画像のファイル名を作成するメソッド
def make_file_name(file_index, file_name):
    return file_name + "_" + str(file_index) + ".jpg"
    

def make_env():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)


if __name__ == '__main__':
    make_env()
    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
    subscriptionKey = os.environ.get('ACCESS_TOKEN_BING_KEY')
    searchTerm = 'ピカチュウ'
    # TODO: searchTermを英語に直すメソッドを作る
    file_name = "pikachu"
    required_image_num = 1
    headers = get_headers(subscriptionKey)
    params = get_params(searchTerm, required_image_num)
    thumbnail_url_array = get_images_url_array(search_url, headers, params)
    print(thumbnail_url_array[0])
    down_load_images(thumbnail_url_array, file_name)
