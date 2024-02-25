from database.models import BaseModel
from peewee import *
from playhouse.postgres_ext import *


class User(BaseModel):
    name = CharField()
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
    
db.create_tables([User])
