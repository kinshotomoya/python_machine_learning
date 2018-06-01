import os
from os.path import join, dirname
from dotenv import load_dotenv 
import requests
import math
import urllib
import http.client
import json

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
subscriptionKey = os.environ.get('ACCESS_TOKEN_BING_KEY')
searchTerm = '欅坂46'
required_image_num = 100
make_directory()


def make_directory():
    # 取得した画像を保存するディレクトリを作成する    

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
    return [image['thumbnailUrl'] for image in search_results['value']]


def down_load_images(thumbnail_url_array):
    for image_url in thumbnail_url_array:
        res = requests.get(image_url)
        if 'image' not in res.headers['content-type']:
            print('画像ではないので、保存しません')
        print(res.content)




headers = get_headers(subscriptionKey)
params = get_params(searchTerm, required_image_num)
thumbnail_url_array = get_images_url_array(search_url, headers, params)
print(thumbnail_url_array[0])
down_load_images(thumbnail_url_array)
