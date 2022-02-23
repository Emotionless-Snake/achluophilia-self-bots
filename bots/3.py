token = input("Paste Your Token Here : ")
import discord
from termcolor import colored

from discord.ext import commands

client = commands.Bot(command_prefix=':', self_bot=True, help_command=None)

async def on_ready():
  await client.change_presence(status=discord.Status.online)
  print(colored("You Are Online :>\nUntil You Close The Program" , "green"))

client.run(token, bot=False)