# Standard Python Libraries
from dataclasses import dataclass


@dataclass
class User:
    user_id: str
    creation_date: str
    update_date: str
    first_name: str
    last_name: str
    email: str
    count_win: int
    count_lose: int
    current_game_id: str
    last_game_id: str
