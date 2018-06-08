from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from datetime import datetime, timedelta


SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('client_id.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))

# 以下の.list()の箇所で、取得するイベントのフィルタリングできる
events_result = service.events().list(calendarId='primary', timeMin="2018-06-03T10:00:00-07:00").execute()
events = events_result.get('items', [])

if not events:
    print('No upcoming events found.')
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    print(start, event['summary'])
