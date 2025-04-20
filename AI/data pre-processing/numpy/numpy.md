
# what is numpy?
- *numpy* is multi n D array  library
# why use array other than lists ?
| compare | list | numpy array |
| ---- | ---- | ---- |
| speed | slow | fast |
| use | - object datatype | - fixed type<br>- this means that it use *same datatype* for all elements in the array<br>- all int , all string , etc ... |
| storage | - more memory<br>- int type<br>*int type contains many information*<br>1. size (4 byte)<br>2. reference Count (8 byte)<br>3. object type (8 byte)<br>4. object value (8 byte) | - less binary stored in memory<br>- int32 (32 bit) |
| memory | value stored in memory blocks are scattered | - Contiguous memory<br>- all blocks are arranged together (next to each other) |
| CPU | slow in access data | - SIMD vector processing (Quicker)<br>-  effective cache utilization |
| operations | insertion , deletion , appending , concatenation | - a lot more in like (/,*,-,+) |
# Applications of numpy
1. mathematics (matlab Replacement)
2. plotting
3. Backend
4. machine learning


# uploading numpy
- by using `import` 
- we also use alias for numpy to use less typing 
```python
import numpy as np
```

# Basics of NumPy
- some default commands

## first array
- by using `np.array([])`
```python
# this is a numpy array

a = np.array([1,2,3])
```

## 2D array
- listing the no.dimensions
```python
# this is a 2D array

b = np.array([[1,2,3] , [4,5,6]])
print(b.ndim)
```
- output `2`
>	note we printed no.dimensions by `.ndim` attribute

## shape and dimensions of array
- shape and dimensions are attributes of any array
- we can see array shape by `.shape`
- while the D is by `.ndim`
```python
# shape and dimensions of an array

a = np.array([[1,2,2] , [4,5,6]])

# see the shape
print(a.shape)

# see the no.D
print(a.ndim)
```
- output  , *shape* : `(2,3)` , *D* : `2`

## Item size
- by using `itemsize` attribute
```python 
# item size for array --> calculated by byte

c = np.array(["mostafa" , "samir"])

# item size
c.itemsize
```
- output `28` --> using **"U7"** 

## specify datatype
- by using `dtype = 'type' parameter
```python
# dtype: to define the datatype

a = np.array([1,2,3] , dtype = 'i')
```

## Total size of array
- by using `nbyte` attribute
```python
# total size for array

a = np.array(["mostafa" , "samir"])

# nbyte attribute
a.nbyte
```
- output `56` byte --> because the usage of **"U7"**
## Copy of an array
- taking a copy of an array an modefing on it
- by `.copy()`
```python
a = np.array([1,2,5])

# taking copy of an array 
b = a.copy()

# modifing on the copy
b[0] = 100

# see changes on (a) and (b)
print(a , "\n" , b)
```
- output `[1,2,5]` array (a) , `[100,2,5]` array (b)

# playing with dimensions
## adding a new dimension
- if we have an array that has a shape of (n,) and we need to add a new dimension (sometimes its essential in machine learning algorithms) to be (n,1)
- we use `reshape` function
```python
# creating an array
randint = np.random.randint(0,3 , size = (3,))

# reshaping an array
arr = arr.rehsape(3,1)
```

## removing dimensions
- we can remove empty dimensions so the array could be (n,) instead of (n,1)
- we use `squeeze` function
```python
# removing a dimension
arr = np.squeeze(arr)
```
# Accessing rows and columns
- accessing elements in np array is the same as lists in python

## accessing specific element
- accessing work the same as lists
- *syntax* : `array[row,column]` 
```python
# accessing specific element in row and columns

a = np.array([[1,2,3,4,5,6,7] , [8,9,10,11,12,13,14]])

# accessing element row 1 , col 5
a[1,5]
```
- output `15`

## accessing element in reverse
```python
# accessing element in reverse 

a[1,-5]
```

## replacing element as in list
```python
a[2,3] = 10
```

# matrix 
- matrices in NumPy is the key fundemantal for AI
## Zeros Matrix
- matrix that is all zeros
- by `np.zeros([size])`
```python
# zeros matrix
zeros = np.zeros([2,3]) # passing the size
```

## Ones Matrix
- matrix of all ones
- by `np.ones([size])`
```python
ones = np.ones([2,6])
```

## Any Number Matrix
- matrix of any number
- by`np.full([size] , number)
```python
# matrix of nuber 50
fifty = np.full([1,4] , 50)
```

## Using the shape of an array to form a new one
- by `a.shape` attribute
```python
# using a.shape
any_ = np.full(a.shape , 4)

# also we can use a method called full alike
any_2 = np.full_alike(a , 4) # same result
```

## Matrix of random variables 
- matrix of random variables in numpy range (0 , 1) 
- by `np.random.rand(size_without_())`
```python
# array of random variabels
rdm = np.random.rand(4,2)
```

## Matrix of random integers
- random integers forming a matrix
- by `np.random.randint(start , end , size = (size of the matrix))`
```python
# creating a random integer matrix
randint = np.random.randint(0,15 , size = (3,3))
```
- output : a matrix of random integers of size (3,3)

## Identity Matrix
- identity matrix is a matrix that its diagonal is composed by one
- by `np.identity(size)`
- note that the size is passed in one parameter , because the identity matrix is always square
```python
# identity matrix

ide = np.identity(5)
```
- output identity matrix of 5X5 size

## Repeating Matrix
- repeating matrix element many times
- by `np.repeat(array , _no.repeats_)`
```python
# repeating an array
a = np.array([1,2,3])

r1 = np.repeat(a , 3)

print(r1)
```
- output `[1,1,1,2,2,2,3,3,3]`

# Mathematics 
## Addition
```python
# prefom addition 
a + 2
```
## Subtraction
```python
# subtraction
a - 2
```
## Division
```python
# division
a / 2
```
## Multiply
```python
# multiply
a * 2
```

## Power
```python
# power
a **2 
```

# linear Algebra 

- using linear algebra operations

## Matrix Multiplication
- multiplying a matrix with another matrix
- by `np.matmul()`
```python
# multiplying 2 matrices

np.matuml(m1 , m2)
```

## Determent of matrix
- finding the determent of a matrix
- by `np.linalg.det()`
```python
# finding determent of a matrix
np.linalg.det(m1)
```

# Statistics 
- finding min and max of an array or a matrix

## min 
- by `np.min()`
```python
# finding min of a martix
np.min(m1 , axis = 0) # in each column
```

## max 
- by `np.max()`
```python
# finding min of a martix
np.max(m1 , axis = 1) # in each row
```

# Re-Organize array
- re-organizig the array by reshaping it
- by `.reshape([size])`
> the size must be valid 
> if not valid it will cause an error

```python
# reshaping an array
arr.reshape([2,2])
```

# Stacking 
- stacking the array in both vertical and horzontal
### Vstack
- vertical stacking
- by `np.vstack(v1 , v2)`
> np.columns in v1 == no.columns v2
```python
# vstack 2 arrays
np.vstack(v1 , v2)
```

### Hstack
- vertical stacking
- by `np.hstack(h1 , h2)`
> np.rows in h1 == no.rows h2
```python
# hstack 2 arrays
np.hstack(h1 , h2)
```

# load data in numpy
- loading txt data
- by `np.getformattxt(location , delimeter = 'seperator')`
```python
# calling data in my notebook
data = np.getformattxt("location" , delimeter = 'seperator')
```

# Boolean masking and advanced indexing
- finding a value inside the matrix or the array by boolean filter
steps :-
1. apply a boolean condition
2. index according to this condition
```python
# making a new matrix from random variabels
test = np.random.randint(100 , size = [6,10])

# apply a boolean mask and filter with it
test[test > 67]
```
- output `all values that are bigger tahn 67`
## using `np.any`
```python
# using np.any()
np.any(test > 67
```
## using `np.all`
```python
# using np.all()
np.all(test > 67)
```
## indexing using list
```python
# indexing with a list in numpy
test2 = np.array([1,2,3,4,5,6,7,8,9])
test2[[0,1,2,8]]
```

## indexing using axis
```python
# using indexing with axis

np.any(test > 67 , axis = 0)
```



# resources
- https://www.w3schools.com/python/numpy/default.asp
- freecodecamp numpy video 




































