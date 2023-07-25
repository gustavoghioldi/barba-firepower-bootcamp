-- SQLite
SELECT * from pet JOIN person ON pet.owner_id=person.id
WHERE pet.animal_type='cat' AND person.name='Bob';