from peewee_orm import Person

p = Person(name="Gustavo", age=46, account=90.21)
p.save()