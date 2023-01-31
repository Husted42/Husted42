-- Find all employees
SELECT * 
FROM employee;

-- Find all clients
SELECT *
FROM client;

-- Find all employees ordered by salary
SELECT * 
FROM employee
ORDER BY salary DESC;

-- Find all employees ordered by sex then name
SELECT *
FROM employee
ORDER BY sex DESC, first_name ASC, last_name ASC;

-- Find the first five emplotees in the table
SELECT * 
from employee
LIMIT 5;

-- Find the first and last name of all employees
SELECT first_name, last_name
from employee;

-- Find the forename and surnames of all employees
select first_name AS forename, last_name AS surname
FROM employee;

-- Find out all the different branch_id
SELECT DISTINCT branch_id
FROM employee;