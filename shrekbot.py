#!/usr/bin/python3

import os
import discord
import random
import re

from dotenv import load_dotenv

def get_shrek_quote():
    quotes = []
    with open("shrekscript.txt", 'r') as scriptfile:
        quote_regex = re.compile("^\w*")
        for line in scriptfile:
            if re.match(quote_regex, line):
                quotes.append(line.strip())

    return random.choice(quotes)



def main():
    load_dotenv()

    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')

    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    # Event/function that runs when connection is ready prints guilds and a confirmation message
    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
        for guild in client.guilds:
            print(guild)

    # Message response event
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        shrek_1_songs = [
            "Self - Stay Home",
            "Smash Mouth - I'm a believer",
            "Leslie Carter - Like Wow!",
            "Dana Glover - Is It you (I have Loved)",
            "Baha Men - Best Years of Our Lives",
            "Halfcocked - Bad Reputation",
            "Jason Wade - You belong to me",
            "Smash Mouth - All Star",
            "Rufus Wainwright - Hallelujah",
            "The Proclaimers - I'm on my way",
            "Eddie Murphy - I'm a Believer (reprise",
            "John Powell - True Love's First Kiss"
        ]

        if message.content == "heyshrek":
            response = "Yes Donkey?"
            await message.channel.send(response)

        if message.content == "heyshrek play":
            song_choice = random.choice(shrek_1_songs)
            await message.channel.send("-play " + song_choice)

        if message.content == "test":
            channel = client.get_channel(786165783020437506)
            shrek_quote = get_shrek_quote()
            await channel.send("G'day mate howyagoin. Here's a shrek quote:\n> {}".format(shrek_quote))


    @client.event
    async def on_voice_state_update(member, before, after):
        if before.channel==None and after.channel!=None:
            print(member.name + " has entered the channel")
            channel = client.get_channel(753900124962553859)
            shrek_quote = get_shrek_quote()
            await channel.send("G'day {} howyagoin. Here's a shrek quote:\n > {}".format(member.name, shrek_quote))

    client.run(TOKEN)

if __name__=="__main__":
    main()
