SELECT * FROM student;

----- Update -----
UPDATE student 
SET major = 'Chemistry'
WHERE student_id = 5 ;

UPDATE student
set major = 'Biochemistry'
WHERE major = 'BIO' OR major = 'Chemistry';

UPDATE student
SET name = 'Tom', major = 'undecided'
WHERE student_id = 1;

UPDATE student
SET major = 'undecided';

----- Delete -----
DELETE FROM student
WHERE student_id = 5;

DELETE FROM student
WHERE name = 'Tom' AND major = 'undecided';

DELETE FROM student