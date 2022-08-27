# mine_interact
https://github.com/AWeirdScratcher/mi_interact 的代替品

## example
```py
import discord
from discord.ext import commands

from mine_interact import Mine

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")
    mine = Mine(bot, channel_id)
    user = bot.get_user(user_id)
    d = await mine.get_user_data(user)
    print(d.id)
    print(d.pickaxe)
    print(d.backpack)
    print(d.money)
    print(d.field)
    print(d.exp)
    print(d.level)
    print(d.mine_count)
    print(d.guild)
    print(d.mystery_stone)
    print(d.skill)


```
## install
```sh
pip install git+https://github.com/cutebear0123/mine_interact.git
```
