import os
from os.path import join, dirname
from dotenv import load_dotenv
import urllib.request
import httplib2
import json
import pickle
import hashlib
# import sha3
from googleapiclient.discovery import build

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
api_key = os.environ.get('GOOGLE_API_KEY')
search_key = os.environ.get('GOOGLE_CUSTOM_SEARCH_KEY')

query = 'hoge'
service = build('customsearch', 'v1', developerKey=api_key)

page_limit = 10
start_index = 1
response_array = []
image_url_array = []

for page in range(page_limit):
    try:
        response_array.append(service.cse().list(
            q=query,
            cx=search_key,
            lr='lang_ja',
            start=start_index,
            searchType='image'
        ).execute())
        # pythonのget()は、dict {id: 1, id: 2}みたいなやつから、
        # keyを指定して、取得する。第二引数にdefault値を設定することができる
        start_index = response_array[page].get('queries').get('nextPage')[0].get('startIndex')
    except Exception as e:
        print(e)

for response_num in range(len(response_array)):
    for items in range(len(response_array[response_num]['items'])):
        image_url_array.append(items[response_num]['items']['link'])
