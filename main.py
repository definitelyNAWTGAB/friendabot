import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix='.',
                      intents=discord.Intents.all())  #sets the prefix to .

client.remove_command("help")  #removes the default help command

@client.command()  #load cogs
async def load(ctx, extension):

    client.load_extension(f'cogs.{extension}')


@client.command()  #unload cogs
async def unload(ctx, extension):

    client.unload_extension(f'cogs.{extension}')
    
@client.event  #notifies us that friend A is online
async def on_ready():

    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game('Greeting new friends!'))

    print("Friend A is here!")
    
for filename in os.listdir('./cogs'):

    if filename.endswith('.py'):

        client.load_extension(f'cogs.{filename[:-3]}')
        
FRIEND_A = os.environ['token']

client.run(FRIEND_A)
