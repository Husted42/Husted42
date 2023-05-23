SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
SELECT @@session.sql_mode;

-- Find the numbers of employees with supervisors
SELECT COUNT(super_id)
FROM employee;

-- Find the number of female employees born after 1970
SELECT COUNT(emp_id)
FROM employee
WHERE sex = 'F' AND birth_day > '1971-01-01';

-- Find the average of all the male employee's salaries
SELECT AVG(salary)
FROM employee
WHERE sex = 'M';

-- Find the sum of all the employee's salaries
SELECT COUNT(salary)
FROM employee;

-- Find out how many males and females there are
SELECT COUNT(sex), sex
FROM employee
GROUP BY sex;

-- Find the total sales of each salesmen
SELECT SUM(total_sales), emp_id
FROM works_with
GROUP BY emp_id;

-- Find the total spending of each client
SELECT SUM(total_sales), client_id
FROM works_with
GROUP BY client_id;