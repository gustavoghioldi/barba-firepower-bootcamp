from peewee_orm import Person


try:
    p = Person.get_by_id(1)
    p.delete_instance()
except Exception as e:
    print(e)
    print("La persona con id 1 no existe")