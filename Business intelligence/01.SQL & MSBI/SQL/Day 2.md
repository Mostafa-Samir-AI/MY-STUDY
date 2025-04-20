# DB mapping
- set of rules we apply on the ERD we get the schematic tables
- every entity is converted into table and the attributes are converted to columns
- the relationship between the 2 entities is converted to **foreign key constrain** 
- the **foreign key** is a primary key in another table
- unlike the primary key **foreign key** can be replicated and have NULL values
* in tables of the schematic , the only cardinality we have is (1-M) one to many <u>parent to child (parent have many children)</u>
* Primary key --> parent
* foreign key --> child

>[!NOTE] Note
> - you cannot delete a parent that have child or more 

---
# terminologies
- Table : collection of records
- Attributes : characters of an Entity
- ROW : specific character of the Entity
- DataBase : A collection of tables
---

* each column in the database must have a domain 
* **Domian** : range of values to work on
* the Domain is clearly represented in Data sheet , where it ensures the Quality and dtype of the column data 
* also columns have constrains and rules / it guarantees values inserted in the data column 

# Mapping Rules
- based on experienced developers who worked on many databases , they put some rules we (DOGSHIT) can work on while learning how to map DB 

![[Screenshot 2024-11-01 204108.png | center]]

## Step 1 : Mapping of regular Entity types
- regular entity means strong entity
- Create table for each Entity type <u>if there is no 1-1 total participation relationship in the data</u>
- choose one of the attributes to be the primary key 
### simple attribute

![[Screenshot 2024-11-01 204649.png | center]]

### Composite attribute
- in some cases we have composite attributes 
- we degenerates the composite attribute and keep the components to be the new attributes 
- we need to inform the developers working on the same database that the composite attribute is deleted , we do that through the **constrain file** 

![[Screenshot 2024-11-01 204919.png | center]] 

### Multi value attribute 
- multi value means that , the value is repeated for the same record 
- so , we make a new column which have a **composite primary key** and the multi-value attribute  

![[Screenshot 2024-11-01 205324.png | center]] 

>[!NOTE]  
> - the entity is not always a table 
> - because the entity could contain a multi-value attribute which make a new table

### Driven attribute
- we do not include the driven attribute in the tables 
- since it can be calculated by equation , it will be included in the constrains file
* in some cases , we need to include the driven attribute 
	* when it requires alot of computation
	* have alot of relationships to other tables

![[Screenshot 2024-11-01 213017.png | center]]

- for the moment , we will no include the driven attribute till we know what microsoft do to handle the driven attributes
## Step 2 : Mapping weak Entity
- in the mapping of weak entity , we do the same we did for the strong entity
- But , in the weak entity <u>we don't have a primary key</u> 
- we have **partial key** 
- **partial key is the primary key of the weak entity** 
* weak entities have different types of key in their tables
* its called "**Composite key**" 
* **Composite key** : foreign key + partial key

## Step 3 : Mapping of Binary 1:1 Relationship types
- binary relationship have 6 phases 
##### 1. binary 1:1 total participation in both sides 
- it converts to 1 table
- then we choose any of the primary keys to be the main primary key 
##### 2. binary 1:1 total and partial participation 
- it converts to 2 tables
- primary key of the partial is put in the total participation table
##### 3. binary 1:1 partial in both
- it converts to 2 tables
- where it have 2 partial keys and any one of them can be the primary key 

## Step 4 : Mapping of Binary 1:N Relationship 