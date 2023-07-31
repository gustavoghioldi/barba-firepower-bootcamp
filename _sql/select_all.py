from peewee_orm import Person

people = Person.select()

for p in people:
    print(p)