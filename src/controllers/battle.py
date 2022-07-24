
from discord import User

from schemas.battle import Battle
from controllers import tamer


def create(attacker: User, defender: User) -> Battle:
    """Creates a battle between two tamers"""
    tamer.