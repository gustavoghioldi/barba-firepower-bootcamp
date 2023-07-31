-- SQLite
CREATE TABLE IF NOT EXISTS people (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, account REAL);

INSERT into people (name, age, account)  VALUES ("Gustavo", 46, 10023.23)
INSERT into people (name, age, account)  VALUES ("JUAN", 20, 1023.00)

INSERT into people (name, age, account)  VALUES ("pedro", 30, 23.00)
INSERT into people (name, age, account)  VALUES ("Omar", 50, 1000000.00)


SELECT name, age from people;
SELECT * from people;

SELECT * from people WHERE account>5000;
SELECT * from people WHERE account>5000 AND age=46;

UPDATE people set account=9999999 WHERE id=1;
SELECT * from people WHERE id=1;

UPDATE people set account=0;
SELECT * from people;

DELETE from people WHERE id=3

SELECT * from people;
INSERT into people (name, age, account)  VALUES ("pedro", 30, 23.00)
