# flutter
## datatypes
- when using **num** ==> accept both integer and float --> its bigger than than int and float 
- be careful when using num , because it will use a lot of space and low performance 
- we used it if we do not know the data type coming from the backend
- string --> when defining a string datatype <u>S capital</u>
```dart 
# defining a string 
String name = "mostafa" ;
```
- **Const vs final**
	- const : constant value cannot change through the code
	- final : const value but will get it in the runtime (like waiting a value from the database while running)
- **var** datatype
	- var is undefined datatype , it takes type when we assign a value to it
```dart
# var datatype
var name = "mostafa" ; // type string
name = "samir" ; // ok

name = 23 ; // error
```

- note --> if we know the dtype , better to use the original datatype

-  **Dynamic**  datatype
	- can assign to all datatypes

# Collection data
 1. list 
 2. map 
 3. set 
## list
- **syntax**
	- `list` + `<dtype>` + `name` + = + `[ elements ] ` + ;
```dart 
// list
List <int> ages = [24 , 23 , 21 , 17] ;
```
- if we removed the data type --> list not array ==> `List name = [12 , "mostafa"]`
- List functions --> type the list name and . 
- it will open all function for the list 
### adding element
- by `add()`
### adding alot
- by `addAll([elements])`

## list functions
- length() --> `list.length`
- add
- addAll
- insert
- insertall
- remove --> function input --> elements
- removeAt --> function input --> use index

## MAP
- the same as dictionary in python
- we can define the type of the map
```dart
// Map
Map names = {1 : "mostafa" , 2 : "samir"} ;

// adding a new element
names[3] = "ali" ;
```

### Methods
- .keys --> list of all keys
- .values --> list of all values 
- .length
- .clear
- .remove

>[!NOTE]
> - API : intermediate between front and the database
> - it fetches information from DB

## Set
- set have {}
### methods
- union
- diff
- intersect

# arithmetic operation
- + 
- %
- -
- /
- *
# relational operation
- ==
- !=
- >
- >=
- <
- <=
# Logical operator
- &&
- ||
- ! 

# conditional statement 
## If statement
```dart
if (num >5) {
// statement 1
}
else {
// statement 2 
}
```

# Loops
## For loop 
```dart
// for loop
for(int i = 0 ; condition ; increment){
// statement 
}
```

## For in 
- the same as python
```dart
// for in loop
for (int i in list1){
 print(i)
}
```

# try and catch
- catch --> catches the error and print a message 