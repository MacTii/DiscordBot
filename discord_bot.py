import discord, os, requests
from dotenv import load_dotenv

# Load .env in same directory
load_dotenv()

# Initialize bot
client = discord.Client()

# Name to get country info
names = ["mateusz", "nathaniel", "kacper"]

def get_country_info(name):

    #name = "Mateusz"
    response = requests.get("https://api.nationalize.io?name=%s" % (name))

    country = response.json()["country"][0]["country_id"]
    #country_info = countries[0]["country_id"]
    return country

# Message that bot is running
@client.event
async def on_ready():
    print('Bot is running as {0.user}'.format(client))

# Bot event handler to messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Message content
    msg = message.content
    
    # Bot message
    if msg[0] == '$' and any(word in msg for word in names):
        await message.channel.send(get_country_info(msg[1:]))

# Bot run
client.run(os.getenv('TOKEN'))