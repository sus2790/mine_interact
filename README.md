# WARNING
**永光 LmanTW**

**Removed Mine Bot's Interact feature**
it's read-only now
# Mine Interact
Mine Interact is a Python libary for Mine Bot Interact.

## Installing
**Python 3.8 or higher is required**

To install the library without full voice support, you can just run the following command:

```sh
# Linux/macOS
python3 -m pip install -U discord.py

# Windows
py -3 -m pip install -U discord.py
```

--------------
## Quick Example
```python
import discord
from discord.ext import commands
# Working for discord.py & pycord
from mine_interact import Mine

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=intents)
channel_id = 123456789 #change it to your channel id
user_id = 123456789 #change it too!

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
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

bot.run('token')
```
You can find more examples in the examples directory.

--------------
## Links
- [Mine Bot Support](https://discord.gg/rYkDwMRhWv)
- [Invite Mine Bot](https://discord.com/oauth2/authorize?client_id=955828209860112395&permissions=8&scope=bot)

You can ask **ANY** Mine Interact question in this server
