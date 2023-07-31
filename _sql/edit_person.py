from peewee_orm import Person

p = Person.get(Person.id == 1)
p.name = "Pedro"
p.age = 30
p.account = 0.0
p.save()
