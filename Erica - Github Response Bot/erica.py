import discord
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
erica = commands.Bot(command_prefix='!', intents=intents)

@erica.event
async def on_ready():
    print(f'Logged in as {erica.user.name}')

@erica.command()
async def recent_commits(ctx, repo_owner, repo_name):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits'
    headers = {'Authorization': 'Bearer YOUR_GITHUB_TOKEN'}
    response = requests.get(url, headers=headers)
    commits = response.json()

    for commit in commits:
        message = f'{commit["commit"]["message"]} - {commit["commit"]["committer"]["name"]}'
        await ctx.send(message)

erica.run('your discord bot token, u need to keep ur token to urself do not ever reveal it online')
