from typing import Optional
import asyncio
import discord
from secrets import token_hex
from .data import User
from .errors import NotFound, APIError, APITimeout

__all__ = (
    'Mine',
)

bot_id = 955828209860112395

class Mine:
    def __init__(
        self, client, channel_id: Optional[int]
    ) -> None:
        self._client = client
        self._session = token_hex()[:15]
        self._channel = self._client.get_channel(channel_id)
        if self._channel is None:
            raise NotFound('Unknown Channel')

    def _check_message(self, m):
        return m.author.id == bot_id and m.channel == self._channel
    
    async def get_user_data(self, user: discord.User) -> Optional[User]:
        minebot = self._client.get_guild(channel_id.guild).get_member(bot_id)
        if minebot.status != "offline":
            pass
        else:
            raise APIError("Mine Bot is offline")
        if user is None:
            raise NotFound('Unknown User')
        await self._channel.send(f'MI.get_user_data {user.id} {self._session}')
        try:
            res = await self._client.wait_for('message', check=self._check_message, timeout=15)  
        except asyncio.TimeoutError:
            raise APITimeout('Mine Bot did not respond')
        if not res.content.startswith('MI.user_data'):
          if not res.content:
            return APIError('Mine Bot returned invalid data')
          else:
            raise APIError(res.content)
        raw_data = res.content[13:]
        if raw_data == 'none':
            return None
        data = raw_data.split('|')
        return User(
            id = int(data[0]),
            pickaxe = int(data[1]),
            backpack = data[2],
            money = int(data[3]),
            field = data[4],
            exp = int(data[5]),
            level = int(data[6]),
            mine_count = int(data[7]),
            guild = data[8],
            mystery_stone = int(data[9]),
            skill = [int(data[10]), int(data[11]), int(data[12])],
        )
