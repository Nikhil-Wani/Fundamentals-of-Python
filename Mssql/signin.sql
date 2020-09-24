#sql

create database signin

USE signin 

create table signininfo
(
	first_name varchar(40),
	last_name varchar(40),
	Email_Id varchar(40),
	Pass varchar(40),
	phone_no varchar(40)
)

Select * from signininfo

insert into signininfo values('ankit','desai','desai@gmail.com','ad@123','8767006638')

delete from signininfo
where Name='Nikhil'    
