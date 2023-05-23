drop table test02;

CREATE TABLE test02 (
  ID serial NOT NULL,
  var15 VARCHAR(15),
  number INT,
  PRIMARY KEY (ID)
);

INSERT INTO test02(var15, number) VALUES('A', 3);
INSERT INTO test02(var15, number) VALUES('B', 4);
INSERT INTO test02(var15, number) VALUES('C', 6);
INSERT INTO test02(var15, number) VALUES('D', 7);
INSERT INTO test02(var15, number) VALUES('E', 9);