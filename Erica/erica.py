import discord
import requests

erica = discord.Client()

async def login():
    print(f'Logged in as {bot.user.name}')
async def recent_commits(ctx, repo_owner, repo_name):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits'
    headers = {'authorization':'bearer UR_GITHUB_TOKEN'}
    responses = requests.get(url, headers=headers)
    commits =responses.json()
