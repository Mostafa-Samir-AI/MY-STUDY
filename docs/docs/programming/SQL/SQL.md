---
author: Mostafa Samir Ali
tags:
  - "#SQL"
---

- commands must end with `;` 
- its not necessary to write the commands of the SQL capital letter 
- but it's a good practice where we can differ between commands and names assigned by user 

# list all databases
```sql
-- lsit all databases
\l
```
# create a DB 
- we use command `CREATE DATABASE`
```sql
CREATE DATABASE test ;
```

# Execute a file to create SQL DB
- we use the `\i` option and the path of the file
```sql
-- execute the file
\i D:/WORK/SQL;
```
# Connecting to database 
- we can get help from `help` command
```sql
-- connecting a sql database 
psql -h localhost -p 5432 -U postgres test
```

- `-h` : host , after that we write the host name
- `-p` : port
- `-U` : username 
## connecting to local database
- we use `\c`
```sql
# connecting to DB
\c test
```
- we can also switch between databases by the same option 

# SQL commands
## creating a table
- we need the column name and dtype for the table
<br><br>
**syntax**
- `command` + `name` + `{values}`
```sql
-- creating a table
CREATE TABLE person (
first_name VARCHAR(50) ,
last_name VARCHAR(50) ,
gender VARCHAR(7) ,
date_of_birth DATE
) ;

```

>[!NOTE] # note
> - we noticed that we can write SQL commands in many lines 
> - `;` determines the end of the command 
> - the semicolon `;` must <u>**not have Spaces from the command**</u>

## delete a table
```sql
-- delete a table
/*
* semicolon must not have space / seperated from the commad 
*/
DROP TABLE person;
```
## Specify constrains 
- constrains restrict the data inputs to be correct values 
- CONSTRAINS LIKE :-
	- NOT NULL
	- PRIMARY KEY
	- BIGSERIAL
```sql
-- create table with constrains
CREATE TABLE person (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(7) NOT NULL,
    email VARCHAR(150)
);

```

## Insert record in table
- we use the compound command 
- composed of 2 parts
	- `INSERT INTO` : specify the columns we are inserting into 
	- `VALUES` : actual values of the columns
<br><br>
**syntax**
- `INSERT INTO` + `table_name` + `(columns)` + `VALUES` + `(Values of columns)`;

```sql
-- inserting values in our columns 
INSERT INTO person (first_name, last_name, gender, email)
VALUES ('sasa', 'darwish', 'male', 'sasa@gmail.com');
```

## calling a query
- we call a query using `SELECT` + `col_name` + `FROM` + `table`
```sql
-- selecting a query
--- calling all the table
SELECT * FROM person;
```
- we can select from columns also
```sql
-- calling aquery in columns
SELECT email FROM person;
```

## sorting values
- we can apply sorting in many columns ascending and descending 
- we use `ORDER BY` option
### sort one column
```sql
-- sorting one column
--- sorting ascending 
SELECT * FROM person_data ORDER BY id ASC;

--- sorting descending
SELECT * FROM person_data ORDER BY id DESC;
```

### Sorting 2 columns
```sql
-- sorting 2 columns
SELECT * FROM person_data ORDER BY id ,email ASC;
```

## Remove Duplicates 
- we use `DISTINCT` keyword to remove duplicates
```sql
-- remove duplicates
SELECT DISTINCT * FROM person_data ORDER BY id ASC;
```
- in the previous query we :-
	- checked duplicates 
	- sort the data according to the column `id` Ascending order

## WHERE clause 
- where clause  allow us to filter the data based on conditions
<br><br>
**syntax**
	- `query` + `WHERE` + `condition`
```sql
-- selectin based on conditions 
SELECT * FROM person_data WHERE date_of_birth = '1998-01-10';
```

### logical operator
- we can do logical operators on the query to get a certain result
* logical operators
	* BETWEEN
	* AND
	* OR

```sql
-- finding a range of numbers
SELECT * FROM person_data WHERE date_of_birth BETWEEN '1996-01-01' AND '2000-12-30';
```

```sql
SELECT * FROM person_data WHERE date_of_birth = '1996-01-01' or date_of_birth = '2000-12-30';
```
### Comparison operator
- > bigger than
- >= bigger than or equal
- < less than
- <= less than or equal
- = equal to 

```sql
 select 1 = 1;
```
- out `t`

## LIMIT, OFFSET and FETCH 
- `LIMIT`: is used to return the max limit of rows 
- `OFFSET`: is used to made a start point where the shell can begin with 
- `FETCH`: its the same as `LIMIT` but it have long syntax

### LIMIT
```sql
-- using limit
SELECT * FROM person_data LIMIT 10;
```

### OFFSET
```sql
-- using OFFSET
SELECT * FROM person_data WHERE date_of_birth BETWEEN '1996-01-01' AND '2000-12-31' OFFSET 6 LIMIT 10;
```

### FETCH
- this one has a long syntax
- where we have to define the starting rows and the ending rows
```sql
-- using FETCH
SELECT * FROM person_data WHERE date_of_birth BETWEEN '1996-01-01' AND '2000-12-31' OFFSET 6  FETCH FIRST 5 ROW ONLY;
```

## IN keyword
- we use `IN` keyword to look for values that are in keywords
```sql
-- without in keyword
SELECT * FROM person_data WHERE gender = 'Male' OR gender = 'Female';

-- with in keyword
SELECT * FROM person_data WHERE gender IN ('Male' , 'Female');

```

## LIKE keyword
- `LIKE`: used for matching strings against patterns in the data
- we can use patterns to filter the data
* patterns 
	* `%`: used for serial of characters 
	* `_`: place for one character 

```sql
-- using like keyword and patterns to filter the data
SELECT * FROM email LIKE '________@%'; 
```

## HAVING keyword
- `HAVING`: allow us to make an extra filter on the query 
```sql
-- using HAVING keyword
 SELECT country , COUNT(*) FROM person GROUP BY country HAVING COUNT(*) > 5 ORDER BY COUNT(*) DESC ;
```

## Aggregate function
- aggregate functions are used to return information about a column
- Aggregate functions
	- MIN
	- MAX
	- AVR
	- SUM
### MIN
```sql
-- using min
select make, min(price) from car group by make;

-- without using min
select * from car group by price order by price asc limit 1 ;
```

### MAX
```sql
-- using max
select make, max(price) from car group by make;
```

### AVR
```sql
-- using average
SELECT AVR(price) FROM car
```

### SUM
```sql
-- using sum
SELECT make, sum(price) FROM car GROUP BY make;
```

## Arithmetic operations
- Arithmetic operations like (+,-,*,/,%) can be included in the SQL
- **Ex**: we will make discount 10% for the price
```sql
-- we need to select each column seperately 
SELECT make, model, price, price * .10 FROM car; -- we have a column of discount 

-- round it 
SELECT make, model, price, ROUND(price * .10, 2) FROM car;

-- new column for the final price
SELECT make, model, price, ROUND(price * .10, 2), ROUND(price - ROUND(price * .10, 2)) FROM car;
```

![[Screenshot 2024-12-01 110709.png | center]]

## Alias 
- an Alias is giving a short name to an entity
- **Ex**: using alias to make names for columns
```sql
-- alias for columns
 SELECT make , model , price as original_price, ROUND(price * .10, 2) as Discount, ROUND(price - (price * .10)) as After_discount FROM car;
```

![[Pasted image 20241201111223.png | center]]

## Handling NULLs
### coalesce Keyword
- `COALESCE` returns default value if the checked value equals `NULL` 
```sql
-- using COALESCE keyword
SELECT COALESCE(email, 'Email not provided') FROM person;
```

>[!NOTE] 
> - we must use single quote `''`  when passing a default value
> - using double quote `""` for passing a column name
> - when using coalesce take care of dtype
> 	- if COALESCE is used with string return string a as default value
> 	- if COALESCE is used with integers return an integer as default value

### NULLIF
- `NULLIF` takes 2 arguments
	- if the $1^{st} = 2^{nd}$ ----> *return NULL*
	- if the $1^{st} \not= 2^{nd}$ ----> return $1^{st}$ 
```sql
-- using nullif
SELECT NULLIF(10,0); -- out 10

SELECT NULLIF(1 , 1); -- null 
```

- **why do we use it** ?
	- because , when we divide by zero , the shell returns an error
	- we need to handle this error 
	- so we need something that return an acceptable value instead of error

```sql
-- dividing by zero
SELECT 10 / 0 ; -- error 

-- using nullif
SELECT 10 / NULLIF(9, 0) ; -- any nuber will be ok

-- handle division by 0
SELECT 10 / NULLIF(0, 0) ; -- returns NULL

-- using COALESCE and NULLIF
SELECT COALESCE(10 / NULLIF(9, 0), 0) ;

```

## DATES
- we can detect date and time by function `DATE`
- we use `NOW()`
### Detecting both DATE and TIME
```sql
-- detecting date
SELECT NOW();
```

### Detecting DATE
- we cast the function `NOW()` to date
```sql
-- detecting date 
SELECT NOW()::DATE; 
```

### Detecting TIME
- we cast the function `NOW()` to time
```sql
-- detecting date 
SELECT NOW()::TIME; 
```

### Some useful dates functions 
#### Intervals
- we can add and subtract intervals from the date and time
- we use `INTERVAL` keyword

##### Adding interval
```sql
-- adding interval
SELECT NOW() + INTERVAL '10 YEARS';
```

##### Subtracting interval
```sql
-- subtracting interval
SELECT NOW() - INTERVAL '8 MONTHS'
```

##### Casting
- we can cast the value to date or time as we want
- we will use `::DATE` OR `::TIME` 
- we need to wrap the whole expression with ( )
###### DATE casting
```sql
-- cast to date
SELECT (NOW() + INTERVAL '7 YEARS')::DATE;
```
###### TIME casting
```sql
-- cast to time
SELECT (NOW() - INTERVAL '14 HOURS')::TIME;
```

### Extracting info from dates
- we can extract a specific values from date
- by using `EXTRACT ( )`

```sql

SELECT EXTRACT(YEAR FROM NOW()) as year;

SELECT EXTRACT(MONTH FROM NOW()) as month;

SELECT EXTRACT(DOW FROM NOW()) as day_of_week;
 
SELECT EXTRACT(DAY FROM NOW()) as month;

SELECT EXTRACT(CENTURY FROM NOW()) as month;

```

![[Screenshot 2024-12-01 210633.png | center]]

### AGE function
- we can calculate the age by subtracting the the date of birth from the current date
```sql
-- using age function
SELECT first_name , last_name , email , AGE(NOW() , date_of_birth) AS age FROM person;
```

## Primary Key
- **primary key** is unique for a record , It's used to distinguish any record in the data 
- cannot be repeated to other record 

### removing primary key
```sql
-- dropping primary key
ALTER TABLE person DROP CONSTRAIN person_pkey ;
```

### Assigning primary key
- assigning primary key takes many columns to construct the primary key
- in our case `id` column is enough 
```sql
-- assigning primary key
ALTER TABLE person ADD PRIMARY KEY (id);
```

## Constraints
- when we need to add constrains , we do
```sql
ALTER TABLE person ADD CONSTRAINT ....... ;
```
### unique constraints 
- **unique constraints** allow us to make each column have a set of unique values
- the same as **primary key** 
- unlike **primary key** that work with rows , **unique constraints** work with columns

```sql
-- adding a unique constrain
alter table person add constraint unique_email unique (email);
```

- adding unique constraint without name
- now we will let the shell decide the name
```sql
ALTER TABLE person ADD UNIQUE (email);
```

#### deleting a unique constraint
```sql
/*
 - when we set a unique constraint we set a name for the constraint 
 - in previous example we set the name to unique_email
 - now we will use this name to remove the constraint
*/

ALTER TABLE person DROP CONSTRAINT unique_email;
```

### check constraint
- the **check constraint** is a method to check if the data entered in a column is valid or not
```sql
-- check constraint 
ALTER TABLE person ADD CONSTRAINT gender_constraint CHECK (gender = 'Male' OR gender = 'Female');
```

## DELETE
- `DELETE`: a keyword is used for deleting elements 
- we can delete rows 
### DELETING all rows
```sql
-- deleting all rows
DELETE FROM person ;
```

- we need to be careful when we use delete because if we didn't specify the condition , the shell will delete the whole data in the table leaving only the table header

### DELETING a row
- we mostly delete by using primary key 
- but we can delete according to a value
```sql
-- deleting a row
DELETE FROM person WHERE id = 10;
```

### DELETING range of rows
#### DELETE according to a value of column
```sql
DELETE FROM person WHERE gender = 'Female';
```
- the previous query will delete all rows that contains gender is equal to *'Female'* 
#### DELETEING according to range of values
```sql
DELETE FROM person WHERE id BETWEEN 10 AND 20;
```

## updating a row
- we use `UPDATE` keyword
<br><br>
**syntax**
- `UPDATE` + `TABLE_NAME` + `SET` + `Column = 'value'` + `WHERE` + `Condition`
- we use `SET` to set a value to cell in the data

>[!NOTE] # NOTE
> - if we didn't add a condition , the postgres will update all rows

```sql
-- updating a column values
UPDATE person SET email = 'NOT PROVIDED' where email IS NULL;

-- updating rows 
UPDATE person
first_name = 'sasa',
last_name = 'dada'
where id = 3;
```

## CONFLICTS
- we can manage conflicts not to return an error 
### IN CONFLICT DO NOTHING
- if we have a conflict in the DB like (Repeating primary key or violating a constraint)

![[Screenshot 2024-12-04 221024.png | center]]

- in the conflict ignore the query
```sql
-- in conflict do nothing
insert into person (id , first_name , last_name , email , gender , country)
values (999 , 'Erek' , 'Schaumann' , 'Not provided' , 'Male' , 'Mexico')
ON CONFLICT (id) DO NOTHING;
```
- out `insert 0 0`

![[Screenshot 2024-12-04 221113.png | center]]

### IN CONFLICT UPDATE
- if there is a conflict , we update values 
- in this case we assign new values to the existing record if there is a conflict in the primary key , etc ...
- we use `DO UPDATE` 
```sql
-- on conflict do update
insert into person (id, first_name, last_name, email, gender, country)
values (999 , 'sasa', 'Darwish', 'not provided', 'Male', 'EGYPT')
on conflict (id) do update set first_name = excluded.first_name, last_name= excluded.last_name, email = excluded.email, gender = excluded.gender, country = excluded.country;
```
![[Screenshot 2024-12-06 162604.png | center]]
## foreign keys , joins & relationships
- foreign keys are primary keys of a table transmitted to another one 
- foreign keys describe relationships between tables

### Foreign key
#### Adding foreign key to a table
- we will add the foreign key in the data while creation 
```sql
-- creating a foreign key
--- Ensure `pgcrypto` extension is enabled for generating UUIDs
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Create `car` table

CREATE TABLE IF NOT EXISTS car (
    car_uid UUID NOT NULL PRIMARY KEY DEFAULT gen_random_uuid(),
    make VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    price NUMERIC(19, 2) NOT NULL CHECK (price > 0)
);

-- Create `person` table

CREATE TABLE IF NOT EXISTS person (
    person_uid UUID NOT NULL PRIMARY KEY DEFAULT gen_random_uuid(),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(7) NOT NULL,
    email VARCHAR(100),
    date_of_birth DATE NOT NULL,
    country_of_birth VARCHAR(50) NOT NULL,
    car_uid UUID REFERENCES car(car_uid), -- foreign key
    
    -- constraint added
    UNIQUE(car_uid),
    UNIQUE(email)
);
```

>[!NOTE]
> - we created the column car before column person 
> - this allowed us to include foreign keys as usual 
> - if we reversed the SQL Shell will return an error , `table car does not exist` 

![[Screenshot 2024-12-09 175828.png | center]]

#### Assign foreign key to a column 
- we can add foreign key to another table 
- this operation is updating , so we will use `update` keyword
<br><br>
**syntax**
- `UPDATE` + `TABLE naem` + `SET` + `foreign key colunm  =  `  + `foreign key value` + `condition: WHERE` + `index: id = VALUE`
```sql
-- updating a foreign key
 update person set car_uid = '6357536f-f93a-4297-8978-c69dbbe3f40a' where person_uid = '8d096a1b-05a7-47b6-b4ab-6a948b8ff5fe';
```

![[Screenshot 2024-12-09 212952.png | center]]

#### Deleting foreign key
- now we will explain deleting foreign key
- if we want to delete any record that is a foreign key reference , it will return error
- because the record contains foreign key reference 
- car table have F.K reference in table person
- **what should we do ?**
	1. we can delete the record that have this foreign key (in table person)
	2. we can update the foreign key to null and delete the record in the other table (car)
- we choose the second option
<br><br>
**steps**
1. update foreign key to null 
```sql
-- updating foreign key to null
UPDATE person SET car_uid = NULL WHERE person_uid = '8d096a1b-05a7-47b6-b4ab-6a948b8ff5fe' ;
```

2. delete the record in car table
```sql
-- deleting record 
DELETE FROM car WHERE car_uid = '6357536f-f93a-4297-8978-c69dbbe3f40a' ;
```

![[Screenshot 2024-12-15 005152.png | center]]

### JOINS
#### Inner joins 
- equivalent to intersection 
- it takes 2 tables (A , B) then find the intersection $(A\ \bigcap B)$  and then produce the result C (the intersection)
- we will use `join` keyword  
```sql
-- preforing a join
select * from person join car on person.car_uid = car.car_uid;
```

![[Screenshot 2024-12-09 220049.png | center]]

>[!NOTE] 
> - we can specify the columns we want to get information from it
> 
> ![[Screenshot 2024-12-09 220520.png | center]]

#### Left joins 
- getting all data that are in the first table + the intersection
```sql
-- left join
select * from person left join car on car.car_uid = person.car_uid;
```

![[Screenshot 2024-12-10 013133.png | center]]

## SEQUENCE
- `BIGSERIAL` :  is a datatype that increment integer any inserted record
	- if the `id` column is a `BIGSERIAL` it will increment to the last record
- we can use it to manage the primary key instead of inserting the `id` in every row we want to create , we will use the `BIGINT` dtype to manage this for us
### See the sequence in the dataset
- the sequence is created by default as a constrain in the data when we created a primary key
- it will be named `TableName_PrimaryKeyName_seq` 
<br><br>
- we can see the sequence with command `select`
```sql
-- select the sequence 
select * from persons_id_seq;
```
- out
![[Screenshot 2024-12-20 201518.png | center]]
- `last_value`: last value used in the sequence 
- `log_cnt`: no. provoking this function
- `is_called`: the sequence was called 
<br><br>
- we can add values by the `insert` command without specifying the `primaryKey`
- the sequence will handle it
- **we need to check the last value of the sequence**
	- if the value equals to the last value in the data --> we can insert
	- if not , we need to alter the sequence to meet the requirements

```sql
-- checking the last value of the sequence 
select * from persons_id_seq;
```
#### good news
- the sequence last value is equal to the last value in the data
- now we can approach ahead
```sql
-- inserting a new column
 insert into persons (first_name, last_name, email, gender, country) values ('Nichol', 'Livick', 'nlivick0@w3.org', 'Female', 'Tanzania');
```

#### BAD news
- the sequence last value is not equal to the data last value
- we need to alter the sequence values

```sql
-- altering the values of a sequence
ALTER sequence person_id_seq RESTART WITH 1001; 
```

- now we can insert the values

# Extensions
- extensions are features/function that add extra functionality to the DB 
- see list of all extensions
```sql
-- see all available extensions
SELECT * FROM pg_available_extensions;
```

# UUID
- `UUID` stands for universally unique identifiers , its globally unique 
- made by complex calculations

- we need to install the extension for `UUID`
- first we need to look for available extensions
- we type command `select * from pg_available_extensions;`

```sql
-- listing all available extensions
select * from pg_available_extensions;
```

- then we find the extension we need, then install it
## installing extension
```sql
-- create an extension
create extension if not exists "uuid-ossp";
```

- now we need to identify the function we want
- we type `\df` will list all functions in the PSQL 
```sql
-- list all functions we have in PSQL
\df
```

## using UUID function
- we can use UUID function that will create a unique UUID 
```sql
-- create a unique UUID
select uuid_generate_v4();
```

## Creation of UUID
- we can create UUID by using SQL 
- instead of `BIGSERIAL` we use `UUID`

```sql
-- creating UUID

CREATE TABLE IF NOT EXISTS person (

    person_uid UUID NOT NULL PRIMARY KEY DEFAULT gen_random_uuid(),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(7) NOT NULL,
    email VARCHAR(100),
    date_of_birth DATE NOT NULL,
    country_of_birth VARCHAR(50) NOT NULL,
    
    -- constraint added
    UNIQUE(car_uid),
    UNIQUE(email)
);
```

# Export to CSV
- we can save any data in SQL as CSV file
- we need to type `\copy` + `query` + `location`

```sql
-- export to csv
\copy (select * from person) TO 'D:/WORK/programming/SQL/results.csv'
```

![[Screenshot 2024-12-20 215621.png | center]]