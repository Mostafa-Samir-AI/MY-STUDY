---
author: Mostafa Samir Ali
tags:
  - DSA
  - python
---

# problem

## Question 1

Alice have some cards with numbers written on them. She arrange the cards in descending order , and lays them down in sequence on a table. she challanges Bob to pick out the card that containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card

we need to told Bob a general strategy to solve the problem

## Systematic strategy we apply for solving problems

1. State the problem clearly , identify the input and outputs format
2. Come up with some examples inputs and outputs , try to cover all edges
3. come up with the correct solution , state it in English language
4. implement the solution and test it using example inputs , fix bugs
5. analyze the algorithm complexity and identify inefficiencies , if any
6. apply the right technique to overcome the inefficiencies
7. repeat (3) and (6) steps

# step 1 : state the problem

##### A. Write the problem in your own words
we need to make a program to find the position if a given number in a list of numbers arranged in descending order , we also need to minimize number of times we access the list elements

> [!HINT] ## Pro Tip
>  if you do not understand the problem , discuss it with the interviewer to make sure you understand the question

##### B. define inputs and outputs

**Input**
1. `cards` : A list of numbers sorted in descending order `[13 , 11 , 10 , 7 , 4 , 3 , 1]`
2. `query`: A number , whose position in the array is to be determined `7`

**Output**
3. `output`: the index of the element
```python
# inputs
test = {'inputs' : {'cards' : [13,11,10,7,4,3,1] , 'query':7} , 
	    'output' : 3}
```

##### C. write the signature function 
- we define an empty function for now
- this is called signature function
```python
def locate_card(cards , query):
	pass
```


> [!NOTE] ## good practice
> name the function properly
> use descriptive variable names
> - interviewers will for this things  

# step 2 : Come up with some examples inputs & outputs . Try to cover all edges

- before we start implementing our function , it would be useful to come up with some examples inputs and outputs which can use later to test the problem
- we need to make many test cases to cover all edges that is a fault in the program

##### A. maintaining the logic of a function
```python
result = locate_card(**test["inputs"]) # un-packing the inputs
print(result)
```

##### B. write all possible queries that a function can handle
1. the number `query` occurs somewhere in the middle of the `cards` ***General Case***
2. `query` is the first element in the `cards`
3. `query` is the last element in the `cards`
4. the list `cards` contains just one element , which is the query
5. the list `cards` does not contain number `query`
6. the list `cards` is empty
7. the list `cards` contains repeating elements 
8. the number `query` occurs at more than one position in `cards`

>[!NOTE] ## Edge cases
> its likely that you do not think about all above cases when you read the problem for the first time 
> some of these are called edge cases , and they are extremely rare

- your problem should handle all of this **edge cases** if occurred because if this edge cases occurred , then it will be fault in your program or a hacker could use this fault to beak in your system

24:55

















