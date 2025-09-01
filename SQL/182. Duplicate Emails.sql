Create table If Not Exists Person (id int, email varchar(255))

insert into Person (id, email) values ('1', 'a@b.com'), ('2', 'c@d.com'), ('3', 'a@b.com')

select email from Person group by email having count(email) > 1
