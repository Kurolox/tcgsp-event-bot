from discord import User
from schemas.tamer import Tamer


def get(user: User) -> Tamer:
    """Recovers a Tamer instance belonging to a Discord user.
    If the user doesn't have a Tamer instance, one will be created before returning."""
    return Tamer.get_or_create(discord_id=user.id)[0]

    

