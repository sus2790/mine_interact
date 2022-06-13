from typing import List

from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    id: int
    pickaxe: int
    backpack: str
    money: int
    field: str
    exp: int
    level: int
    mine_count: int
    guild: str
    mystery_stone: int
    skill: List
