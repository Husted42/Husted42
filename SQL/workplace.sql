-- https://www.edureka.co/blog/interview-questions/sql-query-interview-questions#retrievecolumns
DROP TABLE IF EXISTS employeeInfo;
CREATE TABLE employeeInfo(
	EmpID SERIAL, 
	EmpFname VARCHAR(32),
	EmpLname VARCHAR(32),
	Department VARCHAR(16),
	Project VARCHAR(2),
	Addres VARCHAR(32),
	DOB VARCHAR(16),
	Gender VARCHAR(1),
	PRIMARY KEY (EmpID)
);

INSERT INTO employeeInfo VALUES
(1, 'Sanjay', 'Mehra', 'HR', 'P1', 'Hyderabad(HYD)', '01/12/1976', 'M');
INSERT INTO employeeInfo VALUES
(2, 'Anaya', 'Mishra', 'Admin', 'P2', 'Delhi(DEL)', '02/05/1968', 'F');
INSERT INTO employeeInfo VALUES
(3, 'Rohan', 'Diwan', 'Account', 'P3', 'Mumbai(BOM)', '01/01/1992', 'M');
INSERT INTO employeeInfo VALUES
(4, 'Sonia', 'Kulkar', 'HR', 'P1', 'Hyderabad(HYD)', '02/05/1992', 'F');
INSERT INTO employeeInfo VALUES
(5, 'Ankit', 'Kapoor', 'Admin', 'P2', 'Delhi(DEL)', '03/07/1994', 'M');

DROP TABLE IF EXISTS EmployeePosition;
CREATE TABLE EmployeePosition(
	EmdID INT,
	EmpPosition VARCHAR(16),
	DateOfJoining VarChar(16),
	Salary NUMERIC,
 	PRIMARY KEY (EmdID, EmpPosition)
);

INSERT INTO EmployeePosition VALUES
(1, 'Manager', '01/05/2022', 500000);
INSERT INTO EmployeePosition VALUES
(2, 'Executive', '02/05/2022', 75000);
INSERT INTO EmployeePosition VALUES
(3, 'Manager', '01/05/2022', 90000);
INSERT INTO EmployeePosition VALUES
(2, 'Lead', '02/05/2022', 85000);
INSERT INTO EmployeePosition VALUES
(1, 'Executive', '01/05/2022', 300000);

-- Fetch the Fname in upper case and use the alias name as EmpName
SELECT UPPER(EmpFname) AS EmpName FROM employeeInfo;

-- Fetch the number of people working in HR
SELECT COUNT(Department) AS HRcount FROM employeeInfo
WHERE Department = 'HR' GROUP BY Department;

-- Write a query to get the current date
SELECT CURRENT_DATE;

-- Write a query to retive the first four charectors of Lname
SELECT LEFT(EmpLname, 4) FROM employeeInfo;

-- Write a query to fetch only the adress before barkets
SELECT SUBSTRING(Addres, 0, position('(' in Addres)) FROM employeeInfo;

--Write a query to fin all employess whose salry is between 50000 ad 100000
SELECT EmdID, Salary as totalSal FROM EmployeePosition
WHERE Salary > 50000 AND Salary < 100000;

-- Write a query to find all names that begins with S
SELECT EmpFname FROM employeeInfo
WHERE EmpFname LIKE 'S%';

-- Write a query to fetch top n records
SELECT * FROM employeeInfo
LIMIT 3;

-- Get first and last name
SELECT CONCAT(EmpFname, ' ' , EmpLname) AS name FROM employeeInfo;