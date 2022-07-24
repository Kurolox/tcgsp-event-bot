from datetime import datetime
from schemas.base import BaseModel
from peewee import *
from schemas.tamer import Tamer

class Transaction(BaseModel):

    tamer = ForeignKeyField(Tamer)
    movement = IntegerField()
    balance = IntegerField()
    timestamp = DateTimeField(default=datetime.now())
    reason = TextField()


