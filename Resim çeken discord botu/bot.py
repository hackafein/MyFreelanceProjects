import discord
from bs4 import BeautifulSoup
import requests
import urllib.request
from discord.ext import commands
from discord.utils import get
import datetime
import urllib3
import cv2
client = discord.Client()
site="https://furkanceran.herokuapp.com/test"
source="https://furkanceran.herokuapp.com"
@client.event
async def on_message(message):
    print(message.content) 
    if message.content.find("!komutlar") != -1:
        await message.channel.send("""
        ---=Komut Listemiz=---
        !resimleri getir
        !son resim
        !hakkında
        """)




    if message.content.find("!resimleri getir") != -1 :
        await message.channel.send("Resimler Getiriliyor...")
        page = urllib.request.urlopen(site)
        soup = BeautifulSoup(page)
        images = []
        a=0
        for img in soup.findAll('img'):
            try:
                a+=1
                resim=img.get('src')
                try:
                    resim=resim[2:]
                    
                    
                    contex="Resim "+str(a)
                    e = discord.Embed(title="Örnek Başlık", description="Örnek Açıklama")
                    e.set_image(url=source+resim)
                    await message.channel.send(contex, embed=e)
                except:
                    print(resim," Okunamadı")
            except:
                continue

         







client.run("NzIxODcxNTEwNDczNTM5NjM4.XudWyA.fPBsxYvEDPB40lf5DCUGSG2eakM")
