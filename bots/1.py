token = input("Paste Your Token Here : ")
import discord
from discord.ext import commands
from termcolor import colored

client = commands.Bot(command_prefix="-!-" , self_bot=True,help_command=None)

@client.event
async def on_ready():
 print(colored("Spammer Self-bot is Ready!" , "green"))
 print(colored("Use This Command On Any Discord Text-Channel :\n-!-spam (amount of spam) (message to spam)\nTo Spam" , "blue" , "on_white"))
 print(colored("Close The Program To Stop This Bot!" , "yellow" , "on_red"))

@client.command(name='spam')
async def spam(ctx, amount:int, *, message):
    for i in range(amount): 
        await ctx.send(message) 


client.run(token , bot=False)