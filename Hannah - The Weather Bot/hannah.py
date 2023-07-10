import discord
import os
import requests
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

load_dotenv()

Token = os.getenv('ttoken')
weather_key = os.getenv('weather_key')

#hannah = discord.Client()
hannah = commands.Bot(command_prefix='!', intents=intents)

@hannah.event
async def on_ready():
    print(f'Logged in as {hannah.user.name}')

@hannah.event
async def weather (ctx, location):
    url =f'http://dataservice.accuweather.com/currentconditions/v1/{location}'
    params= {'apikey': weather_key}
    responses = requests.get(url, params=params)
    weather_data = responses.json()

    if len(weather_data)>0 :
        temperature = weather_data[0]['Temperature']['Metric']['Value']
        temp_text = weather_data[0]['temp_text']

    messages =f"The temperature in {location} is {temperature} degree centrigate. Weather : {temp_text}."
    await ctx.send(messages)

    hannah.run(Token)


