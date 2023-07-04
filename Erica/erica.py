import discord
from discord.ext import commands
import requests

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

erica.run('MTEyNTg3NTE3MjE4MDc3MDkzOA.GtC2yF.LtaGDjbxPS-aCRqkBWDv_BTTpoJkTA4e5kEBoA')
