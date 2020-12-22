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

#from __future__ import unicode_literals

#from __future__ import unicode_literals



import logging

logging.basicConfig(level=logging.WARNING)

#from flask import request
#import os
#from flask import request

client = TelegramClient('anfghohn', int(os.environ.get("APP_ID" )), os.environ.get("API_HASH")).start(bot_token= os.environ.get("TG_BOT_TOKEN"))
#@client.on(events.NewMessage(pattern='/start
#@client.on(events.NewMessage(pattern='/start

    
    #await
    
    






# Handle all callback queries and check data inside the handler
@client.on(events.CallbackQuery)
async def handler(event):
    if not os.path.exists(sender.username):
        os.makedirs(sender.username)


    if os.path.exists(sender.username):
        print(event.data)
        vv = event.data
        cc= str(vv)
        x = cc.split("b")
        url = x[2]
        xx= x[1].split("'")[1]
        xxx= xx.split(" ")
        f= xxx[0]
        ydl_opts = {'format':f,'outtmpl':"/app/"+sender.username+"/"}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            Y=ydl.extract_info("https://zee5-player.vercel.app/player?id="+url, download=True)
            X = Y
            print(X)
            e = os.listdir("/app/"+sender.username+"/")
            filepath = "/"
            c = ""
            path = os.path.join("/app/"+sender.username+"/",c.join(e))
            await client.send_message(chat,"file  sending to Telegram")
            await client.send_file(chat,"/app/"+sender.username+"/"+c.join(e),force_document=True)
            path = os.path.join("/app/"+sender.username+"/",c.join(e))
            os.remove(path)
   # await event.answer("fff")
    #if event.data == b'yes':
        



    #chat = await event.get_media()
@client.on(events.NewMessage(pattern='(?i)/ls'))



async def handler(event):


    chat = await event.get_chat()
    link =event.text.split(" ")[1]
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        Y=ydl.extract_info("https://zee5-player.vercel.app/player?id="+link, download=False)
        X = Y
        
    #print (X["entries"][0]["formats"])
    #N = X["entries"][0]["formats"][-1]["url"]
        for x in range(len(X)):
            cc =  X["entries"][0]["formats"][x]["format"]
            await client.send_message(chat,"available_formats", buttons=[
        Button.inline(cc,cc+'b'+link+'b')
        
    ])


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
    
    
    #markup = client.build_reply_markup(Button.url("mx_Stream",SRC))
    await client.send_message(chat,SRC)   
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
    await client.send_message(chat,SRC)   
    #markup = client.build_reply_markup(Button.url("mx_Stream",SRC))
    
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
    #markup = client.build_reply_markup(Button.url("Zee5_Stream",SRC))
    await client.send_message(chat,SRC)   
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
