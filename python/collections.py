### listas
### tuplas
### diccionarios

li = list() #es lo mismo# li = []
print(li)
li.append("hola")
li.append(1)
li.append(True) # booleans True, False y si algo no es nada (null) None
li.append(4.5)
print(li)

for i in li:
    print(type(i))

print(len(li))
li.pop()
print(len(li))
print(li)
li.reverse()
print(li)

li2 = [1, 2, 3, "hola", None]
print(li2)

#### tupla # no puede ser modificada
tup = (1, 2, 3, "hola", None, ) # es recomendable dejar un , al final siempre
for t in tup:
    print(t)

print(tup[0]) # me trae el primer valor 
print(tup[-1]) # me trae el ultimo valor

#### dict # que son dicionarios como los JSON
#import datetime 
from datetime import date # en realidad los import siempre deberian ir en el top del archivo
di = {
    "edad": 33,
    "nombre": "Cristo",
    "nacimiento": date(1,1,1)
}
di["madre"] = "Maria"
print(di)
for i in di:
    print(f"key: {i}, value: {di[i]}")

print(di["edad"])
print(di["nacimiento"])
print(di)
del di["edad"]
print(di)
print(di.keys())
nom = di.pop("nombre")
print(nom)
print(di)
print(di.get("name")) # trae None si la key no existe
#print(di["name"])


