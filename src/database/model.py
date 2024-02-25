from peewee import *
from playhouse.postgres_ext import *
import os

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_TABLE = os.environ.get("DB_TABLE")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

db = PostgresqlDatabase(
    DB_TABLE,
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
)


class BaseModel(Model):
    class Meta:
        database = db


db.connect()
