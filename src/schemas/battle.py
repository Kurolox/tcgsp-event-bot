from datetime import datetime
from schemas.base import BaseModel
from peewee import *
from schemas.tamer import Tamer

class Battle(BaseModel):

    attacker = ForeignKeyField(Tamer)
    defender = ForeignKeyField(Tamer)
    wager = IntegerField()
    timestamp = DateTimeField(default=datetime.now())
    winner = ForeignKeyField(Tamer, null=True)
    cancelled = BooleanField(default=False)

