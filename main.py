from discord import channel
from escpos.printer import Network  
import discord

#Wpisz ID kanałów
channel_id =  
#Wpisz IP drukarki
printer_ip = ""
#Wpisz Token bota
token = ""

client= discord.Client()

printer = Network(printer_ip)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name="drukowanie twych wiadomości"
        )
    )

@client.event
async def on_message(message):
    if (message.channel.id == channel_id):
        time = str(message.created_at)
        print("wykryto wiadomość : " + message.content + "(" "Godzina : " + time + ")")
        printer.text("@" + message.author.name + "#" + message.author.discriminator + print(time[:-7]) +" : \n")
        printer.text(message.content + "\n")
        printer.cut()


client.run(token)