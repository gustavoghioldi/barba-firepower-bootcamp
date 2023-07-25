from peewee import *

db = SqliteDatabase('people_and_pets.db')

class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db

class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db

db.create_tables([Person, Pet])
