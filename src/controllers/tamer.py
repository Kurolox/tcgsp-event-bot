from discord import User
from schemas.tamer import Tamer


def get(user: User) -> Tamer:
    """Recovers a Tamer instance belonging to a Discord user.
    If the user doesn't have a Tamer instance, one will be created before returning."""
    return Tamer.get_or_create(discord_id=user.id, name=user.name)[0]

def alter_currency(tamer: Tamer, movement: int):
    """Updates the amount of currency a Tamer has"""

    # Double check that the tamer won't go into negative values
    assert(movement >= 0 or tamer.currency > abs(movement)) 
    
    tamer.currency += movement
    tamer.save(only=[Tamer.currency])

def set_battle_status(tamer: Tamer, is_battling: bool):
    """Update the battle status of a given tamer"""
    tamer.in_battle = is_battling
    tamer.save(only=[Tamer.in_battle])


    

