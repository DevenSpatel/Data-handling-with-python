TABLE-1 

create table courses(course\_id integer primary key autoincrement, **course**\_name varchar2(25) check(length(course\_name)<=25));



insert into courses(course\_name) values('BCA'),('BBA'),('BCOM'),('BSC'),('BTECH');



---------------------------------------------------------------------------------------------------------------------------



TABLE-2

create table semester(sem\_id integer primary key autoincrement, sem\_tag varchar2(15) check(length(sem\_tag)<=25));



insert into semester(sem\_tag) values('SEM-I'),('SEM-II'),('SEM-III'),('SEM-IV'),('SEM-V'),('SEM-VI');



---------------------------------------------------------------------------------------------------------------------------



TABLE-3

CREATE TABLE subjects(sub\_id integer primary key autoincrement, sub\_code varchar2(15) check(length(sub\_code)<=15), sub\_name varchar2(25) check(length(sub\_name)<=25), course\_id integer references courses(course\_id), sem\_id integer references semester(sem\_id));



-----------------------------------------------------------------------------------------------------------------------------



**Questions from practical 1:-**

1. **Display all subjects name start with c**

select \* from subjects where sub\_name like 'c%';

**2. Display all subjects name ends with ‘on’**

select \* from subjects where sub\_name like '%on';

**3. Display all subjects that contains ‘ic’.**

select \* from subjects where sub\_name like '%ic%';

**4. Display all subject details where subject name second character is o.**

select \* from subjects where sub\_name like '\_o%';

**5. Display all subject details where subject name second character is p and second last character is o.**

select \* from subjects where sub\_name like '\_p%%o\_';



