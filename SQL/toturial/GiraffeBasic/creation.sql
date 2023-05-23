DROP TABLE student; 

CREATE TABLE student (
    student_id INT auto_increment,
    name VARCHAR(20) NOT NULL,
    major VARCHAR(20) DEFAULT 'undecided',
	PRIMARY KEY (student_id)
);

DESCRIBE student;
SELECT * FROM student;

/* delete stuf:
	tables:
		DROP TABLE student; 
	columns:
		ALTER TABLE student DROP COLUMN gpa;
    */

ALTER TABLE student add gpa DECIMAL(3, 2);
ALTER TABLE student DROP COLUMN gpa;

-- Insert data
INSERT INTO student(name, major) VALUES('Jack', 'Biology');
INSERT INTO student(name, major) VALUES('Kate', 'Sociology');
INSERT INTO student(name) VALUES('Claire');
INSERT INTO student(name, major) VALUES('Jack', 'Biology');
INSERT INTO student(name, major) VALUES('Mike', 'Computer Science');