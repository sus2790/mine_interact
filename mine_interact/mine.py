from typing import Union
import discord
from secrets import token_hex
from .data import User
from .error import ChannelNotFound, APIError

bot_id = 955828209860112395


class Mine:
    def __init__(
        self, client: Union[discord.Client, discord.Bot], channel_id: int
    ) -> None:
        self._client = client

        self._session = token_hex()[:15]
        self._channel = self._client.get_channel(channel_id)
        if self._channel is None:
            raise ChannelNotFound(f"Channel{channel_id} does not exist")

    def _check_message(self, m):
        return m.author.id == bot_id and m.channel == self._channel

    async def get_user_data(self, user: discord.User) -> User:

        await self._channel.send(f"MI.get_user_data {user.id} {self._session}")
        res = await self._client.wait_for("message", check=self._check_message)
        if not res.content.startswith("MI.user_data"):
            raise APIError(res.content)
        raw_data = res.content[13:]
        if raw_data == "none":
            return None
        data = raw_data.split("|")
        return User(
            id=int(data[0]),
            pickaxe=int(data[1]),
            backpack=data[2],
            money=int(data[3]),
            field=data[4],
            exp=int(data[5]),
            level=int(data[6]),
            mine_count=int(data[7]),
            guild=data[8],
            mystery_stone=int(data[9]),
            skill=[int(data[10]), int(data[11]), int(data[12])],
        )
