#Not python code. This was to verify that I have SQLite installed and configured properly.

CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Mohaddesa', 15);
INSERT INTO Ages (name, age) VALUES ('Eoghan', 19);
INSERT INTO Ages (name, age) VALUES ('Hailey', 30);
INSERT INTO Ages (name, age) VALUES ('Mindy', 35);
INSERT INTO Ages (name, age) VALUES ('Mailli', 27);

SELECT hex(name || age) AS X FROM Ages ORDER BY X