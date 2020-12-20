from telethon import TelegramClient, events, Button
    #import requests
from bs4 import BeautifulSoup as BS

import asyncio

import subprocess

import requests

#from headers import headers

#import urls

import os

#import cryptg

import youtube_dl #import YoutubeDL

#from future import unicode_literals

#from future import unicode_literals



import logging

logging.basicConfig(level=logging.WARNING)

#from flask import request
#import os
#from flask import request

client = TelegramClient('anfghohn', int(os.environ.get("APP_ID" )), os.environ.get("API_HASH")).start(bot_token= os.environ.get("TG_BOT_TOKEN"))
#@client.on(events.NewMessage(pattern='/start





    
    
    #await
    
    






@client.on(events.NewMessage(pattern='(?i)sm'))



async def handler(event):



    link =event.text.split(" ")[1]



    print(link)



    chat = await event.get_chat()



    await client.send_file(chat,link,force_document=True)

@client.on(events.NewMessage(pattern='(?i)/ls'))



async def handler(event):



    link =event.text.split(" ")[1]



    e = os.listdir(link)



    chat = await event.get_chat()



    c = "|"



    #str1.join(s)



    #print(c)



    await client.send_message(chat,c.join(e))

@client.on(events.NewMessage(pattern='(?i)https://www.zee5.com'))

async def handler(event):

    link =event.text.split('/')[-1]
    print(link)
    chat = await event.get_chat()
    urlq= f'''https://zee5-player.vercel.app/player?id={link}'''
    page = requests.get(urlq)
    v = page.text
    soup = BS(page.text)
    video = soup.find("video")
    SRC = video.find("source").get("src")
    
    
    markup = client.build_reply_markup(Button.url("Zee5_Stream",SRC))
    await client.send_message(chat, "Support @SerialCoIn & @urlicupload\n\n",file=video["poster"], buttons=markup)   
    #print (SRC)
@client.on(events.NewMessage(pattern='(?i)https://www.mxplayer.in/show/'))

async def handler(event):

    link =event.text.split('/')[-1]
    link1 =event.text.split('-')[-1]
    
    print(link1)



    chat = await event.get_chat()
    url = f'''https://mx.tpro.ga/player?id={link1}&type=episode'''
#open and read page
    page = requests.get(url)
    v = page.text
    print(v)
#html = v.read()
#create BeautifulSoup parse-able "soup"
    soup = BS(page.text)
    video = soup.find("video")
#get the src attribute from the video tag
    SRC = video.find("source").get("src")
    markup = client.build_reply_markup(Button.url("mx_Stream",SRC))
    
    #print (SRC)
@client.on(events.NewMessage(pattern='(?i)https://www.mxplayer.in/movie/'))

async def handler(event):

    link =event.text.split('/')[-1]
    link1 =event.text.split('-')[-1]
    
    print(link1)



    chat = await event.get_chat()
    url = f'''https://mx.tpro.ga/player?id={link1}&type=movie'''
#open and read page
    page = requests.get(url)
    v = page.text
#html = v.read()
#create BeautifulSoup parse-able "soup"
    soup = BS(page.text)
    video = soup.find("video")
#get the src attribute from the video tag
    SRC = video.find("source").get("src")
    markup = client.build_reply_markup(Button.url("Zee5_Stream",SRC))
    await client.send_message(chat, "Support @SerialCoIn & @urlicupload\n\n",file=video["poster"], buttons=markup)   
    #print (SRC)
    #print (SRC)



    



    
   # await client.send_file(chat,r1["image_url"],caption = r1["title"])

    

    

            #rgx = w

   # await client.send_message(chat, g1)

   #await client.send_message(chat,"445")






    #path = os.path.join()

    #os.remove(path)







client.start()

client.run_until_disconnected()
