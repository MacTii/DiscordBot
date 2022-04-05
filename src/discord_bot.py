import discord, os, requests
from dotenv import load_dotenv
from names_dataset import NameDataset

# Load .env in same directory
load_dotenv()

# Initialize bot
client = discord.Client()

# Database of names
nd = NameDataset()

def get_country_info(name):
    response = requests.get("https://api.nationalize.io?name=%s" % (name))

    if not response.json()["country"]:
        return None

    country = response.json()["country"][0]["country_id"]

    flag = ":flag_%s:" % (country.lower())
    return flag

# Message that bot is running
@client.event
async def on_ready():
    print('Bot is running as {0.user}'.format(client))

# Bot event handler to messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Message content case sensitive
    msg = message.content.casefold()
    
    # Bot message
    if msg[0] == '$' and nd.search(msg[1:]):
        info = get_country_info(msg[1:])
        if info is not None:
            await message.channel.send(info)

# Bot run
client.run(os.getenv('TOKEN'))