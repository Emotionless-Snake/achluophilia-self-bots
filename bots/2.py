token = input("Paste Your Token Here : ")
import discord
from discord.ext import commands
from termcolor import colored




client = commands.Bot(command_prefix="-!-" , self_bot=True,help_command=None)

@client.event
async def on_ready():
 print(colored("Portable Clock Self-bot is Ready!" , "green"))
 print(colored("Use This Command On Any Discord Text-Channel :\n-!-clock\nTo See The Live Clock" , "blue" , "on_white"))
 print(colored("Close The Program To Stop This Bot!" , "yellow" , "on_red"))

@client.command(name="clock")
async def say_clock(ctx):
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    await ctx.send("The Time is : " + current_time)

client.run(token , bot=False)

 