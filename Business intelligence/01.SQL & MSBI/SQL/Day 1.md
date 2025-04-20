---
author: Mostafa Samir Ali
tags:
  - SQL
---
# DB Life cycle
---
#### 1. Analysis
- reason: not to collide with the client
- the client talks business , while the developer talks coding , there is a gap between clients and developers
- so we need a *system analyst*
- a **_system analyst_** is someone have a strong background about the business and can translate the business view of the client to coding
- he determines the scope of the project in **Requirements Document** 
#### 2. DB design
- we need to convert the Requirements Document into **ERD** --> (Entity Relationship Diagram)
- the one responsible for that is **_DB designer_** 
- the DB designer reads the Requirements document and extracts the *Entities* and their relationships
- **Entity** : any important object that present in the scope of my project

> [!NOTE] Note
> - one Requirement Document can produce more than ERD
> - we need to revice each one of the ERD to check which one is the most fitting one to our app

#### 3. DB Mapping
- set of rules to convert the ERD to actual scheme and tables
- the one who does this work is **_DB designer_** 
- every ERD have only one Scheme , because the rules applied in DB mapping is fixed 
---
*  the previous steps are all done on schematic paper , no software is needed 
---
#### 4. DB Implementation
- its the part where we implement the scheme of the database (physical/shared database)
- we need a software to implement the scheme (SQL Sever , Oracle , mySQL , Access , .....)
- the software type is RDBMS (Relational Database management system)
- once you uploaded the RDBMS , your computer now is called =="DB server"==
- a server should have consistent databases (DBs that is not different on different servers)
- in order to work with these softwares we need to be proficient in SQL (Structured query language)
- the one who is doing this job is **_DB Developer_**

#### 5. Application GUI
- building the GUI 
- the one who do this work is **_Application Developer_** **(DB user)**
- whether it build web based software or an application
- the application will access the DB by **Application server**
- the application server will send queries to the database and return it to the application 
#### 6. End user (Client)
- access the application/URL that is connected to the DB


# before SQL and SQL server
- before SQL and SQL server , we used **file based system**
- File based system is to cheap and do not require a special software to operate
- type of file based systems
	1. Delimited files : file are written with delemiters
		```txt
		1,ahemd,22
		2,ali,25
		3,omaia,23
		```
	
	2. Fixed Width file : writing file with fixed size of bytes for each category
		```txt
		10 java 20 sd
		5 IS 13 python
		50 HR 8 SS
 	   ```

## Disadvantage of this ways
- difficulty in Search
- low performance
- inconsistency in files --> separated copies , each developer will modify on different will lead to different datasets in the same server *limited data sharing*
- no Relationship
- no DB integrity تكامل و ترابط الداتابيز
- DB redundancy --> duplication of the data
- long development time
- security & permissions aspects
- no Constrains | Rules--> rules for the values  have 
- no data Quality
- no Manual Backup & Restore
- different integration 

# modern DB
- after knowing the disadvantage of file based systems , the concept of **DB systems** emerged 
- modern database consists of tables and Relationships
## what are the characteristic of the modern DB
###### 1. one standard
- all data is stored in rows and columns , no more confusing about delimited or fixed width size
- also the data will have a unified shape , where the DBMS will refuse anything that is opposite to the DB structure 
###### 2. Metadata
- its allowed to have metadata in the DB
- metadata is essential in understanding the data we have in our DB
###### 3. datatype control
- each column will have a certain datatype 
- the control of the datatype for columns guarantees there is no wrong values will be inserted in our data
###### 4. Primary Key
- PK is integrated in relationships between data
- it guarantees data integrity 
- characters
	- unique
	- not NULL
###### 5. Centralized DB
- all the data will be gathered in one server 
- all developers will modify the same data --> guarantees data consistency 

# DB , DBS , DBMS
- **DB** : Collection of related data
- **DBMS** : software to facilitate the creation and manipulation of databases
- **DBS** : DBMS + DB + application


> [!HINT] Pro tip
> - one of the disadvantage of DBS is that we have different DB engines  like Oracle , mySQL , etc ...
> - so one of the solutions is to convert the DB into XML 
> - XML can run on different DB engines , its like (intermediate phase)

# DB users
- DB administrator
- system analyst
- DB designer  ✅
- DB Developer ✅
- Application Developer
- BI & Bigdata specialist (Data scientist)
- End user


# ERD
- entity relationship Diagram
- identifies information required by the business by displaying the relevant entities and the relationship between them
## basic Elements of ERD
- Entities 
- Attributes --> character of entities 
- Relationships --> correspond to primary and secondary keys in related tables (may have properties) 
* when we read the requirements document we find (nouns and verbs)
	* noun : name/attributes of the entity
	* verb : name of relationship
# Entity
- entity is the object that is the case of our study (gather and analyze information related to it)
## STRONG vs weak entity
- **Strong** : an entity set that has a primary key , don't have another entity to relay on
- **Weak** : an entity that do not have a sufficient attributes to make it's own primary key , <u>relay on another entity to exist</u> --> (Partial key)
* *Ex*: account (strong entity) have relationship with transactions (weak entity)
* since the  
# Attributes
## 1. Simple attribute
- an attribute is considered to be simple when
	- it cannot be divided
	- not included in runtime
	- cannot be repeated for the same person
- shape : one circle
- *ex* : customer first name ==> 1. cannot be repeated , 2. cannot include in runtime(do any calculations) , 3. cannot be divided 
## 2. Composite attribute
- the same as simple attributes , but <u>it can be divided</u>
- *ex* : customer full name ==> can be divided into first , sir and last name
- shape : 2 circles emerge from main circle

> [!NOTE] Note
> - composite attributes can be divided 
> - it's a must that when we combine all part , it will give meaning 
> - combining *first* + *last name* = *full name*

## 3. derived attributes
- an attribute that can be included in the runtime 
- also cannot be repeated 
- shape : dot circle
- *ex* : age or salary of employee
## 4. Multi value
- it's an attribute that can be repeated for the same person
- *ex* : employee have more than one phone number , more than one address
- shape (double circles)
## 5. Complex attribute
- multi value + composite
- shape : circles emerge from double main circle
- *ex* : address --> 1. can be more than one , 2. can be divided into sub addresses

# Relationships
- relationship is association between several entities 
- type --> degree
- **properties**
	- Degree
	- Cardinality
	- Participation

## Degree
- type of relationships are
	- Unary : between 2 instances of one entity
	- Binary : between instances of 2 entities
	- Ternary : among instances of 3 entities

### Unary
- its a relationship between an entity and itself 
- if 2 entities that are the same type
- *ex* : manager --> manage --> employee  // employee --> manage --> employee

![[what-is-the-degree-of-relation-in-dbms-unary-relationship-example-ae2955f9272e3c1b.jpg | center]]

### Binary
- relationship between 2 entities 
- are the most common

![[images 2.png| center]]
### Ternary
- relationship that combine more than 2 entities 
- it's rare to happen
- happens when an attribute force U to use this relationship

![[images 1 1.png| center]]

## Cardinality
- how many instances of entity one will be connected to the other entities
### types
1. one to one
2. one to many 
3. many to many

![[Relationship-Cardinality-Notations-768x925.webp | center]]

## Participation
- check if all rows of the entity participate in the relationship or not
### Types
1. total participation : if all rows participate in the relationship
	- keywords: must , one or more , obligatory 
2. partial participation : if some of the rows participate in the relationship 
	- weak Entities always have total participation
	- keywords : zero or more , may , some

![[Screenshot-(982).png | center]]

> [!HINT] Tip
> - if there is anything that is not clear in the requirement document you should ask the system analyst about it 
> - DO NOT ASSUME ANYTHING FROM YOUR PREPECTIVE

# keys
## candidate key
- it's a phase that be done before selecting primary key
- **candidate Key** : it's all keys that are candidate to become a primary key
- the candidate should follow the rules of primary key
- if there is no candidates then we use ....
## composite key
- composite key is a key we form combining various keys into one key to make a new primary key
- how we will combine it depends on the attributes we have
- if there is no , then we should make our unique primary key from scratch 
## Primary
- have underlying line on the name 

2:40:00 --> ERD design 

