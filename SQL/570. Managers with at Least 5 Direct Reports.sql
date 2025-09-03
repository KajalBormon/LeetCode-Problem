Create table If Not Exists Employee (id int, name varchar(255), department varchar(255), managerId int)

Truncate table Employee

insert into Employee (id, name, department, managerId) values ('101', 'John', 'A', NULL)

insert into Employee (id, name, department, managerId) values ('102', 'Dan', 'A', '101')

insert into Employee (id, name, department, managerId) values ('103', 'James', 'A', '101')

insert into Employee (id, name, department, managerId) values ('104', 'Amy', 'A', '101')

insert into Employee (id, name, department, managerId) values ('105', 'Anne', 'A', '101')

insert into Employee (id, name, department, managerId) values ('106', 'Ron', 'B', '101')


-- Problem Solved 
SELECT e1.name
FROM Employee e1
JOIN Employee e2
  ON e1.id = e2.managerId
GROUP BY e1.id, e1.name
HAVING COUNT(e2.id) >= 5;

SELECT e1.name 
from Employee e1 
join Employee e2
    on e1.id = e2.managerId
group by e1.id, e1.name
HAVING count(e1.id) >= 5



