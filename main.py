from bot import *
from config import config as config
import discord

def main():
    intents = intents=discord.Intents.default()
    intents.message_content = True
    intents.voice_states = True

    TOKEN = config['DISCORD']['TOKEN']

    Bot(TOKEN, intents)
