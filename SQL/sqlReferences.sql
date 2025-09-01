ALTER TABLE hr_leave_types
ADD leave_code VARCHAR(30);

ALTER TABLE hr_leave_types
DROP COLUMN leave_code;

SELECT name, CONCAT(color, " ", request_unit) AS LeaveName 
FROM hr_leave_types

SELECT FIND_IN_SET('c', 's,q,c,v')
FROM hr_leaves;


SELECT FORMAT(salary, 2)
FROM hr_employee_salaries

DESCRIBE hr_employee_salaries;


