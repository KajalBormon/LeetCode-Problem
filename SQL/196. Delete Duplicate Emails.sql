Create table If Not Exists Person (Id int, Email varchar(255))

Truncate table Person

insert into Person (id, email) values ('1', 'john@example.com')

insert into Person (id, email) values ('2', 'bob@example.com')

insert into Person (id, email) values ('3', 'john@example.com')


-- Problem Solved 
DELETE p1 FROM Person p1
JOIN Person p2
ON p1.Email = p2.Email AND p1.Id > p2.Id