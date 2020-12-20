from telethon import TelegramClient, events, Button
import requests
from bs4 import BeautifulSoup as BS
from headers import headers
import urls
import pyrogram
import os
#import asyncio
from youtube_dl import YoutubeDL
#from flask import request
from pyrogram import (
    Client,
    Filters,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)



@client.on(events.NewMessage(pattern='(?i)https://www.zee5.com'))

async def handler(event):

    link =event.text.split('/')[-1]
    print(link)



    chat = await event.get_chat()
    url = f'''https://zee5-player.vercel.app/player?id={link}'''
#open and read page
    page = requests.get(url)
    v = page.text
#html = v.read()
#create BeautifulSoup parse-able "soup"
    soup = BS(page.text)
    video = soup.find("video")
#get the src attribute from the video tag
    SRC = video.find("source").get("src")
    markup = client.build_reply_markup(Button.url("mx_Stream",SRC))
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
    await client.send_message(chat, "Support @SerialCoIn & @urlicupload\n\n",file=video["poster"], buttons=markup)   
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

client.start()
client.run_until_disconnected()
