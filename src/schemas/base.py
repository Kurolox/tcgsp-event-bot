from os import getenv
from dotenv import load_dotenv
import peewee


load_dotenv()

engine = peewee.PostgresqlDatabase(getenv("EVENTBOT_DB_ENGINE"))

class BaseModel(peewee.Model):
    class Meta:
        database = engine

# Get all of the defined models and create the tables if not existing already
engine.connect()

def create_tables():
    engine.create_tables(BaseModel.__subclasses__())
