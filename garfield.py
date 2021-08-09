import discord
import os 
from dotenv import load_dotenv
from garf_func import random_comic, comic_by_date, random_sunday_comic

from discord.ext import commands 
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has joined the chat!')

@bot.command()
async def randomgarf(ctx):
    url, year, month, day = random_comic(1978, 6, 19, sunday_only=False)
    await ctx.send(year + "-" + month + "-" + day)
    await ctx.send(url)

@bot.command()
async def randomgarfsunday(ctx):
    response = random_sunday_comic()
    await ctx.send(response)

@bot.command()
async def garfondate(ctx, arg):
    comic = comic_by_date(arg)
    await ctx.send(comic)

@client.event 
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

bot.run(TOKEN)
client.run(TOKEN)