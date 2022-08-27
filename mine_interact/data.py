from typing import (
    Optional,
    List,
)
from dataclasses import dataclass

__all__ = (
    'User',
)

@dataclass(frozen=True)
class User:
    id: Optional[int]
    pickaxe: Optional[int]
    backpack: Optional[str]
    money: Optional[int]
    field: Optional[str]
    exp: Optional[int]
    level: Optional[int]
    mine_count: Optional[int]
    guild: Optional[str]
    mystery_stone: Optional[int]
    skill: Optional[List]
