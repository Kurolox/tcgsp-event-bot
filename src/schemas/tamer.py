from schemas.base import BaseModel
from peewee import *

INITIAL_CURRENCY_AMOUNT = 50

class Tamer(BaseModel):

    # Peewee doesn't seem to like non-incrementing primary keys, so the discord ID won't be used
    # as a primary key.
    discord_id = BigIntegerField(unique=True)
    currency = IntegerField(default=INITIAL_CURRENCY_AMOUNT)
    in_battle = BooleanField(default=False)
