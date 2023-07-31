from peewee import *

db = SqliteDatabase("test.db")

class People(Model):
    name = CharField()

    class Meta:
        database =db