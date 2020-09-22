import httplib
import urllib
import time
import requests
import threading
import json

import random


# Define a function that will post on server every 15 Seconds

def thingspeak_post():
    threading.Timer(15,thingspeak_post).start()
    val=random.randint(1,30)
    URl='https://api.thingspeak.com/update?api_key=VVMPLOTIBDHL0DCX&field1=0'
    KEY='VVMPLOTIBDHL0DCX'
    HEADER='&field1={}&field2={}'.format(val,val)
    NEW_URL=URl+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)

def read_data_thingspeak():
    URL='https://api.thingspeak.com/channels/1153024/feeds.json?api_key=ICVRATPQT209S3XZ&results=2'
    KEY='ICVRATPQT209S3XZ'
    HEADER='&results=2'
    NEW_URL=URL+KEY+HEADER
    print(NEW_URL)

    get_data=requests.get(NEW_URL).json()
    #print(get_data)
    channel_id=get_data['channel']['id']

    field_1=get_data['feeds']
    #print(field_1)

    t=[]
    for x in field_1:
        print(x['field1'])
        t.append(x['field1'])

if __name__ == '__main__':
    #thingspeak_post()
    read_data_thingspeak()
