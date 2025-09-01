-- Find the second highest salary
SELECT(SELECT MAX(salary)
FROM hr_employee_salaries
WHERE salary < (SELECT MAX(salary) FROM hr_employee_salaries))

-- 1st -> desc order, 2nd ->  if tie both same ranking, 3rd -> 

SELECT salary, 
DENSE_RANK() OVER (ORDER BY salary DESC) AS `rank` 
FROM hr_employee_salaries 
ORDER BY salary DESC

INSERT INTO Employee (id, name, salary, managerId) VALUES
(1, 'Joe', 70000, 3),
(2, 'Henry', 80000, 4),
(3, 'Sam', 60000, NULL),
(4, 'Max', 90000, NULL);


