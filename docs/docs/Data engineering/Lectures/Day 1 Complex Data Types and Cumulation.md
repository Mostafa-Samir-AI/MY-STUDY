---
author: Mostafa Samir Ali
tags:
  - DataEngineering
date: 16-11-2024
---
# What is a dimension ? 
- a dimension is an attribute of an entity 
	- ex: entity *mostafa* --> have name , age , job
- some of the dimensions are *identifier dimension* like *ID* 

## flavors of attributes
1. Slowly changed
	- time dependent , can change through time
	- my favorite food , changes through time
	- cause alot of problems when we deal with it
2. Fixed
	- cannot be changed through time 
	- birthday 

# Knowing your consumer
- we need to know who will use the data we are working on 
- its hard for chatGPT or LLMs to figure

>[!NOTE] 
> - its important to know what is the usage of the data 
> - because if not you will make a alot of fatal mistakes 
#### Data analyst
- we need the to make the data easy to query 
- all columns must be string or int dtype
- building an OLAP cube 
#### Data engineer 
- other data engineer will use your data 
- in this case you will develop and work on **master data sets** 
- there are many pipelines to read and develop the data
- its allowed to use complex datatypes because the data engineer understand the workflow 
#### ML models
- depends on model and how its trained
#### Customers
- we should make charts , its not ok to give the customer row data

# Data modeling
- 3 types **dimensional data modeling** 
	- there is fact data modeling , Later
## OLTP
- online transaction processing 
- used by software engineers to speed up the program 
- the way it look to the data --> look to 1 entity
## OLAP
- online analytics processing 
- optimize for large volumes 
## Master data
- completeness entity definitions 

>[!TIP] 
> # mismatching needs = less business value
> - if we have an OLTP application based and we modelled the data as OLAP , then the application will be slow because pulling all these columns for the data while it needs only one is painful  
> - if vice versa , if we completely ignored the OLTB ; the joints (very expensive when doing manually) will cause us pian 

## OLTP and OLAP is a continuum 
- combining both OLTP and OLAP to produce master data 
### for layer of Dimensional data modeling 

![[Screenshot 2024-11-17 142030.png | center]]

# Cumulative table design 
- when building a master data , in any day a new user will show up 

## Core components
- 2 data frames (yesterday and today)
- full outer join the 2 data frames 
- coalesce (gather) values to keep everything around 
- hang onto all history

## Usage
- growth analytics at Facebook 
- analytical pattern usage 

## Diagram of cumulative data design 
- how it works

![[Pasted image 20241117200123.png | center]]

>[!NOTE]
> - if we starts today , then yesterday is NULL 

- cumulation matrix is calculation we preform to get insights of the data 
- cumulated output will be yesterday input (if we are starts today and continue tomorrow the same process)
## Cumulative data design 
<h3 color="green"> Pros </h3>
- we get historical analysis without grouping --> can preform massive queries on the data (table)
- easy transition analysis

<h3 color="red"> Cons </h3> 
- can only backfill sequentially 
- handling data can be a mess --> handling deleted users

## compactness vs usability tradeoff 
- when we design data tables we take in consider 2 metrics 
- compactness and usability 
#### the most usable table usually
- have no complex data types
- Easily can be manipulated with WHERE and GROUP BY 
- **OLAP Cubes**
#### the most compact table 
- it can't be read by humans (not human readable)
- too compressed as small as possible 
- need to be decoded every time it will be used 
- **online systems**
### the middle ground table
- we can use complex datatypes like structs ,arrays making the query tricker but  compacting more
- **Master data**

# Struct vs array vs map
## struct 
- struct : table inside in a table
- keys are defined 
- values of any type
## map
- keys are loosely defined 
- values have the same data type

## arrays 
- ordinal : ordered data 
- access randomly
- list of values of all data types , can be a list of structs or maps

# Temporal cardinality explosions of dimensions 
- 