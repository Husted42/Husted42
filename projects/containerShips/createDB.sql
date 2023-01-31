CREATE TABLE vessels (
  ship_id INT AUTO_INCREMENT,
  type VARCHAR(15),
  owned_since DATE,
  env_id INT,
  PRIMARY KEY (ship_id)
);

CREATE TABLE env_class (
	env_id INT PRIMARY KEY,
    env_name VARCHAR(10),
    emmision NUMERIC (2, 1)
);

ALTER TABLE vessels
ADD FOREIGN KEY(env_id)
REFERENCES env_class(env_id);

CREATE TABLE captains(
	emp_id int,
    fname VARCHAR(20),
    lname VARCHAR(30),
    PRIMARY KEY(emp_id)
);

CREATE TABLE routes(
	ship_id INT,
	departure_date DATE,
    emp_id INT,
    env_id INT ,
    goods_amount INT,
    lenght INT,
    PRIMARY KEY(ship_id, departure_date),
    FOREIGN KEY(ship_id) REFERENCES vessels(ship_id),
    FOREIGN KEY(emp_id) REFERENCES captains(emp_id)
);

-- add enviroment classes
INSERT INTO env_class VALUES(1, 'A', 3.0);
INSERT INTO env_class VALUES(2, 'B', 4.5);
INSERT INTO env_class VALUES(3, 'C', 6.0);
INSERT INTO env_class VALUES(4, 'D', 7.5);
INSERT INTO env_class VALUES(5, 'E', 9.0);

-- add vessels
INSERT INTO vessels(type, owned_since, env_id) VALUES('KFM Gold', '1991-02-20', 3);
INSERT INTO vessels(type, owned_since, env_id) VALUES('KFM Gold', '1991-02-20', 3);


SELECT * FROM vessels;
SELECT * FROM env_class;
SELECT * FROM captains;
SELECT * FROM routes;

DROP TABLE ships;
DROP TABLE env_class;
DROP TABLE captains;
DROP TABLE routes;