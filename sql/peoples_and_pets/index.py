from peewee import *

from models import Pet, Person

from datetime import date

# uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
# uncle_bob.save() # bob is now stored in the database
# grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1))
# grandma.save()
# herb = Person.create(name='Herb', birthday=date(1950, 5, 5))
# herb.save()

# p = Person()
# p.name = "coco"
# p.birthday=date(1960, 1, 15)
# p.save()

# uncle_bob = Person.get(Person.name=="Herb")

# bob_kitty = Pet.create(owner=uncle_bob, name='Gatito', animal_type='cat')

pets = Pet.select()

for p in pets:
    print(f"pet name => {p.name} /// onwe name => {p.owner.name}")