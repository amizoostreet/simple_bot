import discord
from discord.ext import commands
import os
from config import *


class MyBot(commands.Bot):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    async def on_ready(self):
        # Slash Command Sync
        synced =await bot.tree.sync()
        print(f"Synced: {len(synced)}")
        print(f"Bot Online: {bot.user} , {bot.user.id}")



    # Cog Load
    async def setup_hook(self):
        for filename in os.listdir('cogs'):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")
                print(f"Cog Loaded: {filename[:-3]}")
            else:
                print(f'Failed to load cog {filename}')
                    

            
bot = MyBot(command_prefix=prefix,intents=discord.Intents.all())


# Bot Run
bot.run(token)