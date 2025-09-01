-- Active: 1733116492302@@127.0.0.1@3306@employ_zen
SELECT * FROM countries WHERE name LIKE '%A';

SELECT * FROM countries WHERE name NOT IN ('American Samoa', 'Dhaka');

SELECT * FROM countries WHERE name IN ('American Samoa', 'Dhaka');

SELECT * FROM countries ORDER BY code;

SELECT * FROM countries ORDER BY code, name;

SELECT first_name, last_name, email, gender, salary FROM hr_employees WHERE blood_group = 'A' OR (first_name LIKE '%a%'); 

SELECT * FROM hr_employees 
WHERE NOT blood_group <> 'A' 
OR first_name NOT LIKE 'a%';

SELECT * FROM hr_employee_salaries 
WHERE salary NOT BETWEEN 15000 AND 70000;


SELECT * FROM hr_employees 
WHERE salary IS NOT NULL;


SELECT * FROM hr_employees
WHERE emergency_contact_relation = 'Parent'
LIMIT 5;

SELECT MAX(salary) as MaxSalary  FROM hr_employee_salaries GROUP BY employee_id;

SELECT COUNT(*) FROM hr_employees

