from peewee import Model, CharField, IntegerField, FloatField, SqliteDatabase

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    age = IntegerField()
    account = FloatField()
    class Meta:
        database = db
         
db.create_tables([Person])