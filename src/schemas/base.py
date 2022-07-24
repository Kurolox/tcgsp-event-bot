from os import getenv
from dotenv import load_dotenv
import peewee

load_dotenv()
db_path = getenv("EVENTBOT_DB_ENGINE")
print(f"Connecting to the following DB: {db_path}")
engine = peewee.PostgresqlDatabase(db_path)

class BaseModel(peewee.Model):
    class Meta:
        database = engine

# Get all of the defined models and create the tables if not existing already
engine.connect()

def create_tables():
    engine.create_tables(BaseModel.__subclasses__())
