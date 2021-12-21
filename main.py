from discord import channel
from escpos.printer import Network  
import discord

channel_id = ""

printer_ip = ""

token = ""

client= discord.Client()

printer = Network(printer_ip)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name="printing your messages"
        )
    )

@client.event
async def on_message(message):
    if (message.channel.id == channel_id):
        wiadomosc = message.content.replace("\n", " ")
        if len(wiadomosc) > 128:
            print("Message detected (Shortened to 128 characters.) : " + wiadomosc[:128] + "    (" "time : " + str(message.created_at)[:-7] + ")")
            printer.text("@" + message.author.name + "#" + message.author.discriminator + "   " + str(message.created_at)[:-7] +" : \n")
            printer.text(wiadomosc[:128] + "\n")
        else: 
            print("Message detected : " + wiadomosc + "    (" "Time: " + str(message.created_at)[:-7] + ")")
            printer.text("@" + message.author.name + "#" + message.author.discriminator + "   " + str(message.created_at)[:-7] +" : \n")
            printer.text(wiadomosc + "\n")

client.run(token)