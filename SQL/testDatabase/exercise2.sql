DROP TABLE IF EXISTS teaches;
DROP TABLE IF EXISTS attends;
DROP TABLE IF EXISTS likes;
CREATE TABLE teaches (lecturer VARCHAR(50), course VARCHAR(50));
CREATE TABLE attends (student VARCHAR(50), course VARCHAR(50));
CREATE TABLE likes (student VARCHAR(50), lecturer VARCHAR(50));

COPY teaches FROM 'C:/C/github/code/SQL/testDatabase/csv/teaches.csv' DELIMITER ',';
COPY attends FROM 'C:/C/github/code/SQL/testDatabase/csv/attends.csv' DELIMITER ',';
COPY likes FROM 'C:/C/github/code/SQL/testDatabase/csv/likes.csv' DELIMITER ',';

SELECT course, student FROM teaches NATURAL JOIN attends;

-- SELECT * FROM teaches NATURAL JOIN attends NATURAL JOIN likes;
