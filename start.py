from telethon import TelegramClient, events, Button
    #import requests
from bs4 import BeautifulSoup as BS

import asyncio

import subprocess

import requests

#from headers import headers

#import urls

import os
import subprocess

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
#@client.on(events.NewMessage(pattern
#@client.on(events.NewMessage(pattern='/start
@client.on(events.NewMessage(pattern='(?i)/start'))
async def handler(event):
    chat = await client.get_chat()
    os.makedirs(sender.username)
    await client.send_message(chat,"hai"+sender.username)




    
    
    #await
    
    






# Handle all callback queries and check data inside the handler
@client.on(events.CallbackQuery)
async def handler(event):
    if not os.path.exists(event.sender.username):
        os.makedirs(event.sender.username)
    if os.path.exists(event.sender.username):
        vv = event.data
        cc= str(vv)
        x = cc.split("b")
    #print(x)
        url = x[1]
        urlz = url.split("'")[1]#urlssssssssss
        print(urlz)
        f = x[2]
        fz= f.split(" ")[0] #format
        print(fz)
        ydl_opts = {'outtmpl':"/app/"+event.sender.username+"/",'format':fz,'proxy':'SOCKS5://49.12.0.103:36895'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            Y=ydl.extract_info("https://zee5-player.vercel.app/player?id="+urlz, download=True)
            print(Y)
            chat = await event.get_chat()
            list = os.listdir("/app/"+event.sender.username+"/")
            await client.send_message(chat,list)
    
    
    
    
    
    #print(f)
   # format= xxx.split(" ")
   # if os.path.exists(event.sender.username):

   # await event.answer("fff")
    #if event.data == b'yes':
        



    #chat = await event.get_media()
@client.on(events.NewMessage(pattern='(?i)/ls'))



async def handler(event):


    chat = await event.get_chat()
    link =event.text.split(" ")[1]
    ydl_opts = {'proxy':'SOCKS5://49.12.0.103:36895'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        Y=ydl.extract_info("https://zee5-player.vercel.app/player?id="+link, download=False)
    X = Y
    for x in range(len(X)):
        #Op=x
        #print (Op)
        
        #print(Op)
        ytdlf= X["entries"][0]["formats"][x]["format"]
        await client.send_message(chat, 'https://www.zee5.com', buttons=
    Button.inline(ytdlf,link+"b"+ytdlf))
        
    #c = subprocess.getoutput("youtube-dl"+" -F "+link)
    #await client.send_message(chat,c)


    #str1.join(s)



    #print(c)



    #await client.send_message(chat,c.join(e))
@client.on(events.NewMessage(pattern='(?i)/lss'))

async def handler(event):

    chat = await event.get_chat()

    link =event.text.split(" ")[1]
    print (link)
    subprocess.call (link)
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
