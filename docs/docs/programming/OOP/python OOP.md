---
author: Mostafa Samir Ali
tags:
  - python
  - OOP
---

# OOP with python
 - do not repeat Ur self 
 - each datatype is an instance of string or any other datatype class 
---
# Class creation
    
```python
class ClassName:
	pass
```
- this allow us to create an empty class


## creating attributes (manually):-
- these are attributes that are created manually in instance item1 (from class item)
- item1 is an instance of item class
- item1 is an object
- each one of those are attributes 
- they are assigned to instance of a class

```pyTHON
item1 = item()
item.name = "phone"
item.price = 1000
item.quantity = 5
item.total = item.price * item.quantity
```

---
# methods:-

 - **methods**: functions of a class
 - methods can be accessible through our class 
 - <u>methods are callable (they can be called)</u>
 - **any method that is created receive (instance/object) as first parameter**
 - if we want to use the method in the class we have to add (self)

 ```python
    class item:
        def calculate_total(self)
 ```
 - we are not allowed to create a method that does not accept any parameter --> except we put pass
---
# Creating attributes in class :-

 - we have a problem in manual attributes --> every time we make instance we initialize the attributes manually 
 - we need construct a instance/object of class and initialize the attributes manually
 - we use for this `__init__` method ==> (magic method)

 - (`__init__`): constructor
    - when creating a class --> python is gonna execute `__init__` method automatically
    - python will call the actions inside the `__init__` method 
 - EX:
```python
class item:
	def __init__(self):
		print("welcome to my class)

# initialize an instance of the class
item1 = item()

# execution of the code
item1() 
```
- output `welcome to my class`
---
## dynamic attribute assignment:-
- we can assign attributes dynamically with `__init__` 
- **its for instance attributes** 
- EX:
```python
class item:
	def __init__(self,fname):
		self.first_name = fname
```

> [!NOTE] ## Note
> - fname --> data passed to the `__init__` method 
> - first_name --> (name of instance attribute) attribute that will be created automatically when an instance of class is created

<br>

### Validating DataType values in instances attributes :-

 - that means I can define the DataType of attribute passed to the instance
 - EX:
 ```python
class item:
	def __init__(self, name:str , price:float , quantity = 0):
		self.item_name = name
		self.item_price = price
		self.item_quantity = quantity
	def calculate_total_price(self):
		return self.item_price * self.item_quantity
 ```

> [!NOTE] ## NOTE
>  - note : we did not assign a default DataType for quantity --why--> have a default value which automatically define the DataType

<br>

### Validate the received values
 - we need the value of price and quantity to be positive
 - we preform it by --> assert statement 
 - when adding a negative value --> assertion error

 ```python

    class item:
        def __init__(self, name:str , price:float , quantity = 0):
    
        # Run validations to received arguments , then adding an error message
            assert price >= 0, f"price {price} is not greater than or equal to 0 "
            assert quantity >=0, f"quantity {quantity} is not greater than or equal to 0 "
        
            self.item_name = name
            self.item_price = price
            self.item_quantity = quantity
        def calculate_total_price(self):
            return self.item_price * self.item_quantity

 ```

## purpose of ***self***
- **Instance Access**:
    
    - `self` allows each method to access attributes and other methods on the same object instance. This is essential for maintaining state within an object and for object-oriented programming to work properly.
    - Without `self`, methods would not be able to access or modify the instance's attributes.
- **Method Binding**:
    
    - When a method is called on an instance of a class, Python automatically passes the instance as the first argument to the method. By convention, this argument is named `self`. This automatic passing is what allows methods to operate on the instance data.
- **Convention and Readability**:
    
    - Using `self` is a convention in Python that enhances readability and makes it clear that a method belongs to an instance of a class. Other developers can quickly understand that `self.attribute` or `self.method()` refers to instance-specific data or behavior.


## Class attributes :-
- class attributes are attributes that is shared between all instances of the class globally
- it belongs to the class itself BUT --> U can access it from the class itself 
- EX:
```python
class item:
	pay_rate = 0.8 --> class attribute 
		def __init__(self, ...)
```

### accessing the class attribute outside of the class 

```python
print(item.pay_rate)
```

### accessing class attributes from instances 
```python
print(item1.pay_rate)
print(item2.pay_rate)
print(item3.pay_rate)
```

> [!NOTE] ## Question
>   **why i can access the class attributes from instance level ???**
>  
>   * because the instance look for attribute in the instance level 
>     /if not found/
>   * it look for it in the class level 
> 

### accessing all attributes of class and instance :-

  - `__dict__` : take all attribute and convert it to dictionary
```python
class.__dict__ --> class attributes will appear here
object.__dict__ --> instance attributes only will appear here 
```

### design a function that access the class attribute 

  ```python
def apply_discount(self):
	self.price = self.price * item.pay_rate 
  ```
  - note: we add class name before the class attribute --> to allow instance to access the class attribute 
  - note --> the function below changes the instance attribute *imp*
 
## changing the class attribute :-
 
- there is a difference between `self.variable` and `class.variable`

#### self.variable
---
- variable can be changed in-directly through changing instance attribute
- EX:
```python
instance.variable = _new value_
items.pay_rate = 0.5
```
- instance variable can be changed without changing the class variable

> [!NOTE] # Note
> - instance.attribute = new value 
> - class.attribute = original value

#### class.variable
---
- variable **cannot** be changed in-directly through instaces attribute
- only change directly by class attribute
- it will change for the class and for all instances made from this modified class 
- when using the class attributes in Your code you either write before it class name or instance (self)
- Ex
```python
# changing the class attribute directly
item.pay_rate = 0.9
```

# list of created instances :-

 - we need to know how many instances are created from our class 
 - making a list of instances --useful--> processing data from instances like (processing instances attributes)
 - there is no build in function that do that so we will do it manually

### steps:-
  1. creating an empty list as a class attribute 
  2. put our executable code in the __init__ block
-  as U remember --> __init__ get executed every time we create an instance
  3. action to be executed --> `class.list_name.append(self)` ==> `item.all_.append(self)`

```python
class item:
    # class attribute
    pay_rate = 0.8
    all_ = []
    
    def __init__(self, name:str , price:float , quantity = 0):
    
    # Run validations to received arguments , then adding an error message
        assert price >= 0, f"price {price} is not greater than or equal to 0 "
        assert quantity >=0, f"quantity {quantity} is not greater than or equal to 0 "
    
    # assign to self object    
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
    
    # action to be executed   --> our point
        item.all_.append(self)
```
    
```python
# looping through instances
for instance in item.all_:
	print(instance.item_name)
```

## handling the representation of instances in all_ list :--
  - we see that the representation of the instances in list (all) is not friendly
  - we need to make it more friendly --> using `__repr__` method
```python  
# __repr__ method
def __repr__(self):
```
   returns --> list of string (item)

## to make it more friendly :-
```python
def __repr__(self):
	return f"item('{self.item_name}','{self.item_price}','{self.item_quantity}')"
  
``` 
- returns --> list of item instances 

# Class methods:-
 - Class Method: methods of class that ***do not take instances as first argument (`self`)***
- instead it takes ***class as first argument (`cls`)***
 
### making a class method:-
  1. using decorator `@classmethod`
  2. passing to the method --> class as first argument (`cls`)
    * note: we use `@classmethod` decorator ==> to change the functionality of the method
  - EX:
  * a class method to instantiate instances 
```python
@classmethod
def instantiate_from_csv(cls,csv_file):
	# openning the csv files
	with open(csv_file,'r') as f:
		
		# reading the csv file as dictionaries
		reader = csv.DictReader(f)
		
		# converting the dictionaries into lists
		items = list(reader)
```

### characters :-
  - class methods are only called by the class 
  - EX :
```python
item.instantiate_from_csv(_pass the csv file_)
```
## Creating an instance from a class method:-
 
  1. open csv file by python code and reading it as a dictionary
```python
with open(csv_file,'r') as f:
	reader = csv.DictReader(f) // DictReader: dictionary reader / f: file content / reader: variable 
```
  2. converting the dictionary to a list 
```python
items = list(reader)
```
  3. iterating through the list and creating instances of class by get method
```python
for item in items:
	items_1(name = item.get('name'))
	, price = float(item.get('price')) 
	, quantity = int(item.get('quantity'))    
```
 - calling the class method is by class level only --> item_class.int_from_csv( ) 

# Static methods:-
 - We generally use static methods to create utility functions.
 - EX :
 ```python
# static method to check if the person is adult 

@staticmethod 
def is_adult(age):
	if age > 18:
		return True
	else:
		return False

# another one 

@staticmethod
def isAdult(age):
 return age > 18
 ```

 - calling the static method 
 
 ```python
print(items_1.isAdult(22)) --out--> true 
 ```

## Class methods VS Static methods
------------------------------------------------

 - <u>Static method</u> is used to create utility for the class (function specified only for the class)
    - like creating a function and used in the class 
    - but prefere to make it as static method to be releated only for the class 
    * should do something releated to a class but not unique per instance 
    - static method is called from instance level 

<br> 

 - <u>Class method</u> is used for instantiate instances from some structured data that U own 

# Inheritance:-
 - problem: we have same item but different characters --> phone1 and phone2
 - Solution: we use inheritance 

<br>

 - we can create a child class that inherit from the parent class its attributes and methods
 -  we can create attributes that is releated to child class only // not useful for parent class 

<br>

 - we will need to repeat the constructor of the parent class  
 - EX : creating a child class
 
 ```python
class phone(items_class):

	# copying the constructor from parent class
	def __init__(self, name:str , price:int , quantity:int , broken_phones = 0):
		
	# Run validations to received arguments , then adding an error message
		assert price >= 0, f"price {price} is not greater than or equal to 0 "
		assert quantity >=0, f"quantity {quantity} is not greater than or equal to 0 "
		assert broken_phones >=0, f"broken_phones {broken_phones} is not greater than or equal to 0 "
	
	# assign to self object    
		self.item_name = name
		self.item_price = price
		self.item_quantity = quantity
		self.broken_phones = broken_phones
 ```

 - problem: duplication of constructor from parent class
 - Solution: use super() method 

 - EX:-
 ```python
class phone(items_class):

	# copying the constructor from parent class
	def __init__(self, name:str , price:int , quantity:int , broken_phones = 0):
		
		# using super() method
		super().__init__(name , price , quantity) # only attributes of the parent class
		
		# add phone specific attributes
	
	# Run validations to received arguments , then adding an error message
		assert broken_phones >=0, f"broken_phones {broken_phones} is not greater than or equal to 0 "

	# assign to self object    
		self.broken_phones = broken_phones
 ```
## we need list of instances for each class :-

- in all_ list
- we need to modify __repr__ method by which it accepts class name 

- we use {self.__class__.__name__} instead of (item)-->string 
  
  ```python
def __repr__(self):
	return f"{self.__class__.__name__}('{self.item_name}','{self.item_price}','{self.item_quantity}')"  
  ```
 
## code organization :-
 - working with multiple files --> making modules to work with
 - putting the classes in different modules and importing them in the main

 - importing modules in the main file
 
Here's the revised and logically fixed markdown for the explanation on encapsulation:

---
# public , private and protected
Here's a markdown table comparing public, private, and protected access modifiers in Python:


| Access Modifier | Syntax   | Description                                                                                 | Access Level                          |
| --------------- | -------- | ------------------------------------------------------------------------------------------- | ------------------------------------- |
| Public          | `name`   | Accessible from anywhere, both inside and outside the class.                                | No restrictions                       |
| Protected       | `_name`  | Intended to be accessed only within the class and its subclasses. Conventionally treated as | Within the class and subclasses       |
|                 |          | non-public, but still accessible from outside with a warning that it is a protected member. |                                       |
| Private         | `__name` | Accessible only within the class. Name is mangled to prevent access from outside.           | Within the class only (name mangling) |

### Detailed Description

#### Public
- **Syntax**: `name`
- **Description**: Public members are accessible from anywhere, both inside and outside the class. They have no restrictions.
- **Example**:
  ```python
  class MyClass:
      def __init__(self, name):
          self.name = name

  obj = MyClass("PublicName")
  print(obj.name)  # Accessible from outside the class
  ```

#### Protected
- **Syntax**: `_name`
- **Description**: Protected members are intended to be accessed only within the class and its subclasses. By convention, a single underscore prefix indicates that the member is protected. While it can still be accessed from outside the class, it suggests that it should not be.
- **Example**:
  ```python
  class MyClass:
      def __init__(self, name):
          self._name = name

  obj = MyClass("ProtectedName")
  print(obj._name)  # Accessible but not recommended
  ```

#### Private
- **Syntax**: `__name`
- **Description**: Private members are accessible only within the class. The double underscore prefix triggers name mangling, making it difficult to access from outside the class.
- **Example**:
  ```python
  class MyClass:
      def __init__(self, name):
          self.__name = name

      def get_name(self):
          return self.__name

  obj = MyClass("PrivateName")
  print(obj.get_name())  # Accessible through a public method

  # Accessing directly will result in an error
  try:
      print(obj.__name)  # Raises AttributeError
  except AttributeError as e:
      print(e)

  # Name mangling allows access, but it's not recommended
  print(obj._MyClass__name)  # Accessible through name mangling
  ```
  
This table and the examples illustrate the differences in access levels and intended use for public, protected, and private members in Python.
# Encapsulation

Encapsulation is a mechanism that restricts access to certain components, preventing the modification of variables directly. Instead, access and modifications are controlled through methods. This ensures that variables, once initialized, remain constant (read-only).

### Example: Creating a Read-Only Property

```python
class Item:
    def __init__(self, name):
        self._name = name

    @property
    def read_only_name(self):
        return self._name

# Testing the property decorator
item = Item("AAA")
print(item.read_only_name)  # Output: "AAA"

# Trying to change the value
try:
    item.read_only_name = "BBB"
except AttributeError as e:
    print(e)  # Output: "can't set attribute"
```

### Changing Class Attributes to be Encapsulated

Creating encapsulated attributes requires careful handling. If you make a property decorator directly for an attribute, initializing it within the class can be tricky because decorators execute first.

```python
class ItemClass:
    import csv

    # Class attribute
    pay_rate = 0.8
    all_ = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations on received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"

        # Assign to self object
        self._name = name
        self._price = price
        self._quantity = quantity

        # Add instance to the class attribute
        ItemClass.all_.append(self)

    @property
    def name(self):
        return self._name

# Testing encapsulation
item = ItemClass("Sample", 10, 2)
print(item.name)  # Output: "Sample"
try:
    item.name = "NewName"
except AttributeError as e:
    print(e)  # Output: "can't set attribute"
```

### Private Attributes

To further restrict access, you can use private attributes by adding double underscores `__` before the variable name. Private attributes cannot be accessed directly from outside the class.

```python
class Item:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

# Testing private attributes
item = Item("PrivateItem")
print(item.name)  # Output: "PrivateItem"
try:
    item.name = "NewName"
except AttributeError as e:
    print(e)  # Output: "can't set attribute"
```

### Private Attributes vs. Encapsulation

- **Private Attributes**: Cannot be accessed directly from outside the class.
- **Encapsulation**: Allows access through getter methods, but prevents modification.

### Setting a New Value for a Private Attribute

To allow controlled modification of a private attribute, use the `@property` decorator along with a setter method.

```python
class Item:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value

# Testing the setter method
item = Item("ShortName")
print(item.name)  # Output: "ShortName"

item.name = "NewName"
print(item.name)  # Output: "NewName"

try:
    item.name = "ThisNameIsWayTooLong"
except Exception as e:
    print(e)  # Output: "The name is too long"
```

### Summary

- **Encapsulation** ensures read-only access by using the `@property` decorator.
- **Private Attributes** are further restricted and cannot be accessed directly from outside the class.
- Setters allow controlled modification of attributes, ensuring that any changes adhere to specific conditions.

The `@property` decorator in Python is used to manage the access and modification of class attributes in an encapsulated manner. Here are the primary reasons for using `@property` when dealing with encapsulated variables:

# @property
### 1. **Read-Only Access**

Using the `@property` decorator allows you to create read-only attributes. This means that once an attribute is set, it cannot be modified directly. This is useful for attributes that should not be changed after initialization.

```python
class Item:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

item = Item("ReadOnlyItem")
print(item.name)  # Output: "ReadOnlyItem"
item.name = "NewName"  # Raises AttributeError: can't set attribute
```

### 2. **Controlled Modification**

By using a property with a setter method (`@property` combined with `@<property_name>.setter`), you can control how and when an attribute is modified. This allows you to enforce rules and validation checks before setting a new value.

```python
class Item:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise ValueError("The name is too long")
        self._name = value

item = Item("ValidName")
item.name = "ShortName"  # Works fine
item.name = "ThisNameIsWayTooLong"  # Raises ValueError: The name is too long
```

### 3. **Data Encapsulation**

Encapsulation ensures that the internal representation of an object is hidden from the outside. By using `@property`, you can provide a public interface to interact with the private attributes, ensuring that the internal state is not exposed directly.

```python
class Item:
    def __init__(self, name):
        self.__name = name  # Private attribute

    @property
    def name(self):
        return self.__name

item = Item("EncapsulatedName")
print(item.name)  # Output: "EncapsulatedName"
print(item.__name)  # Raises AttributeError: 'Item' object has no attribute '__name'
```

### 4. **Improved Code Maintainability**

Using properties allows you to change the implementation details of how attributes are accessed and modified without changing the external interface of the class. This improves the maintainability and flexibility of the code.

```python
class Item:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        # Additional logic can be added here later without changing the interface
        return self.__name

    @name.setter
    def name(self, value):
        # Additional validation can be added here later without changing the interface
        self.__name = value
```

### Summary

The `@property` decorator is a powerful feature in Python that helps implement encapsulation by providing a controlled way to access and modify class attributes. It ensures read-only access, allows for controlled modification with validation, hides internal state, and improves code maintainability.
# principles of OOP:-

 (A) Encapsulation
 (B) Abstraction
 (C) Inheritance
 (D) Polymorphism


(A) Encapsulation:-
-------------------------
 - a mechanism to restrict the direct access to some of attributes in a program
 - i cannot change teh variable from instance level ,but i can change it from the class it self 

(B) Abstruction:-
------------------
 - shows necessary attributes and hide un-necessary from user 
 - one method calls multiple methods --> hidding the multiple un-necessary methods from the instance
 
 - this could be achevied by converting the inner methods to **private methods**

 ```python

        class mail:
    def __init__(self , from_:str , to:str , address:str):
        
        self.from_who = from_
        self.to = to
        self.address = address
        
    def __connection_http(self):
        pass
    def __routing(self):
        pass
    
    def send_mail(self , send = False):
        if send:
            self.__routing()
            self.__connection_http()
            print("email is sent")

 ```

(C) Inheritance:-
----------------
 - mechanism reuse the code across our classes 
 * parent class --> have ==> child classes

(D) Polymorphism:-
--------------------
 - use of single type of entiy for representing many different types with different scenarios 
 - Polymorphism: many forms 
 
 - len() functions --> knows how to handle different type of scenarios 
  * can work with string , integers
 






