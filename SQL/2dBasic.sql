SELECT * FROM hr_employees
WHERE first_name LIKE 'A__';

SELECT * FROM hr_employees
WHERE email LIKE '[a]%';


SELECT * FROM hr_employees
WHERE email LIKE '[^AB]%';

SELECT * FROM hr_employees
WHERE email LIKE '[A-C]%';

SELECT * FROM hr_employees
WHERE first_name BETWEEN 'Alicia' AND 'Gerda'
ORDER BY first_name;


SELECT * FROM hr_employees
WHERE dob BETWEEN '1972-01-13' AND '1995-09-21';


SELECT hr_employees.first_name, users.email
FROM users 
INNER JOIN hr_employees 
ON hr_employees.user_id = users.id;

-- All Data fetch from the left table along with matching right table
SELECT hr_employees.id, hr_employees.first_name, users.email
FROM hr_employees 
LEFT JOIN users 
ON hr_employees.user_id = users.id; 


-- All Data fetch from the right table along with matching left table if no matching the field will fill up the `NULL` value
SELECT hr_employees.id, hr_employees.first_name, users.email, users.name
FROM hr_employees 
RIGHT JOIN users 
ON hr_employees.user_id = users.id; 


-- All Data fetch from the left table with right table full join is not supported mysql achieve this using left and right join both;
SELECT e.id, e.first_name, u.email, u.name
FROM hr_employees e
LEFT JOIN users u ON e.user_id = u.id

UNION

SELECT e.id, e.first_name, u.email, u.name
FROM hr_employees e
RIGHT JOIN users u ON e.user_id = u.id;

-- Self join for same table
SELECT a.name, b.email 
FROM users a, users b 
WHERE a.id = b.id 
AND a.name = b.name
ORDER BY a.name;


-- Union 
SELECT name FROM users   
UNION 
SELECT first_name from hr_employees 


SELECT name, count(*) as Total, email 
FROM users 
GROUP BY email  
ORDER BY id DESC;

SELECT h.employee_id, e.first_name, count(h.employee_id) as TotalAttendance
FROM hr_attendances h 
INNER JOIN hr_employees e
ON h.employee_id = e.id
GROUP BY employee_id
HAVING count(h.employee_id) > 2;

SELECT name 
FROM users 
WHERE EXISTS (SELECT first_name FROM hr_employees WHERE hr_employees.user_id = users.id);


SELECT first_name 
FROM hr_employees
WHERE salary > ANY (
    SELECT salary FROM hr_employees WHERE department_id = 2
);


SELECT first_name, salary,
CASE 
    WHEN salary > 20000 THEN 'The salary is greater than 20K'  
    WHEN salary > 30000 THEN 'The salary is greater than 30K'  
    ELSE 'The Salary less than 20K' 
END AS SalaryText
FROM hr_employees 
