import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import asyncio
import utils
import sqlite3
import os

load_dotenv()

# setup database
con = sqlite3.connect("fliphistory.db")
cur = con.cursor()

token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename="discord.log", encoding="utf-7", mode="w")

intents = discord.Intents.default()

intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="f!", intents=intents) 


# check if running
@bot.event
async def on_ready():
    print("ready to flip")


# Return last 5 flips and average from the server
@bot.command(description='Returns last 5 flips, total number of flips, and flip percentage from server')
async def local_history(ctx):
    server_id = ctx.guild.id

    # execute sqlite3 query and stores raw data to cur_history
    cur_history = cur.execute(
        "SELECT result, date_time, username FROM flips WHERE server_id = ? ORDER BY flip_id DESC;",
        (server_id,),
    )

    # format and send message using data
    history = cur_history.fetchall()
    if not history:
        print(f"local_history requested by {ctx.message.author}\nlocal_history empty")
        await ctx.send("no history")
    output = utils.return_five(history, False)
    print(f"local_history requested by {ctx.message.author}\nlocal_history returned")
    await ctx.send(output)


# Return last 5 flips and average from global
@bot.command(description='Returns last 5 flips, total number of flips, and flip percentage from all servers')
async def global_history(ctx):
    server_id = ctx.guild.id

    # execute sqlite3 query and stores raw data to cur_history
    cur_history = cur.execute(
            "SELECT result, date_time, username FROM flips ORDER BY flip_id DESC;",
    )

    # format and send message using data
    history = cur_history.fetchall()
    if not history:
        print(f"global_history requested by {ctx.message.author}\nglobal_history empty")
        await ctx.send("no history")
    output = utils.return_five(history, True)
    print(f"global_history requrested by {ctx.message.author}\nglobal_history returned")
    await ctx.send(output)


# flip coin, return result, add to databese
@bot.command(description='flips coin')
async def flip(ctx):
    server_id = ctx.guild.id
    username = ctx.author.name
    await ctx.send("*flipping...*")
    await asyncio.sleep(1.15)
    coin = utils.flip()
    await ctx.send(f"It's {coin.result}")
    cur.execute(
        "INSERT INTO flips (result, date_time, server_id, username) VALUES (?, ?, ?, ?);",(coin.result, coin.timestamp, server_id, username),
    )
    con.commit()
    print(f"server_id:{server_id}\nresult:{coin.result}\ntimestamp:{coin.timestamp}")


bot.run(token, log_handler=handler, log_level=logging.DEBUG)
