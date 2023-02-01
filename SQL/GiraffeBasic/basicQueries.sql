SELECT * FROM student;

SELECT name, major
FROM student
ORDER BY name ASC
LIMIT 3;

SELECT student.name, student.major
FROM student
ORDER BY student_id ASC;

SELECT student.student_id, student.name, student.major
FROM student
ORDER BY major DESC, student_id;

SELECT *
FROM student
where major = 'Biology' OR major = 'Sociology';

-- <, >, <=, >=, =, <>, AND, OR
SELECT *
FROM student
where major <> 'Biology';

SELECT *
FROM student
where student_id <= 3 AND name IN('Claire', 'Kate', 'MIke');