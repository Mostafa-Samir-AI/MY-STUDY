---
author: Mostafa Samir Ali
tags:
  - AI
  - "#data_pre_processing"
---

# pandas tutorial

## when dealing with data we need to know :-
-------------------------------------------- 
    (1) seperator 
    (2) if all letters are english
    (3) encoding of the data
 
 - how to check that :-
 ------------------------
  - manually: open the data on textEditor --> vscode / notepad++ ==> NOT microsoft_Word
  - by code : we can open data and see the previous by (open) method
        * code for reading a single line from the data 
        ```python

                with open(r'D:\Darsh\Engineer_DARSH\Amit_learning\stackoverflow_data\survey_results_public.csv') as f:
                        s = f.readline()

        ```
        * code for reading lines in my code 
        ```python

            lines = []
            with open(r"D:\Darsh\Engineer_DARSH\Amit_learning\stackoverflow_data\survey_results_public.csv") as f:
                for _ in range(2):
                        s = f.readline()
                        lines.append(s)
            lines

        ```

## importing data to my notebook
---------------------------------
 - importing data to use it in my code (dealing with csv)
 - using read_csv method in pandas
 
 - syntax:
 ---------
  - data = pandas.read_csv("_file location_" , sep = "seperator type" , encoding = "_encoding type_")
  
  ```python

        data = pd.read_csv(r"D:\Darsh\Engineer_DARSH\AI\Amit_learning\stackoverflow_data\survey_results_public.csv" , sep= "," , encoding="UTF-8")

  ```

## information about data:-
-----------------------------
 A- knowing the shape of the data:-
 -------------------------------
  - .shape attribute
  - returns shape of the data
  ```python
    
    data.shape
  ```
 B- checking for data shape and datatype:-
 ------------------------------------------
  - using .info() method 
  - giving us number of rows and columns + datatype for each column
  ```python
    
    data.info()
  ```

## displaying columns and rows:-
----------------------------------
 - we noticed that we cannot see the whole columns in the dataframe so , we need to display more coulumns
 - we can do that by adjusting options in pandas 
 
 ```python

    pd.set_option("display.max_columns" , _number of columns_)

 ```
 
- dataframe: 2D data structure , combination of rows and columns 

# Basic dataframe functionallity

 
## converting any datatype to dataframe 
----------------------------------------
  - by using DataFrame method in pandas

    '''
    df = pd.DataFrame(_data type_)
    '''

## accessing single column:-
-------------------------------
 - 2 ways
 *********
  - data.column_name
  - data['clolumn_name']
 
 - it return a series datatype NOT! a dataframe  
 - series: one-dimensional array

## accessing multi column:-
-----------------------------
 - passing the name of columns in a list 

 ```python

    data[["col1" , "col2"]]

 ```
 - do not forget to pass teh name of columns a list because pandas will think that U passed the 2 columns as a singel column
 - notice: we returned dataframe NOT! series , because it has 2d now 

## returning all columns names:-
-------------------------------------
 - .columns attribute 

 ```python

  data.columns
 ```

## accesing rows :-
----------------------
 - accesig rows can be Done by {loc} and {iloc} functions
 
 - loc : location       --> accepts string datatype
 - iloc: index location --> accepts intger datatype

 - for rows the index is the columns names 

 ```python

      data.loc[0] # returning the first row values 

 ```

 - loc  ==> loc[row_label , col_label]
 - iloc ==> iloc[row_index , col_index]

 * passing multi values --> list ==>iloc[[0,1]]
 * passing an interval --> : without list square brackets ==> iloc[0:5,1]

## counting values in the column:-
-----------------------------------
 - 2 methods

 A- count:-
 ---------- 
  - data.conut --> return the series and the count its length

 B- value_counts()
 ------------------
  - data.value_counts() --> return the count of each unique value 

## indexing:-
-----------------
 ### making any column an index to the data 
 ------------------------------------------
 - by using set_index() method

 ```python

    data.set_index(col1)
 
 ``` 
 - we note that changes are not made ???
 ------------------------------------------
  - python created an instance and changed that instance but did not change the original data
  - It give us an adventage to see the changes applied to the instance before we apply it on the data 

 - to make the changes parmenantly --> use (inplace = True) parameter 
 ```python

   data.set_index("col1" , inplace = True)

 ```
 
 ### reseting to index:-
 --------------------------
  - to reset the index we use reset_index(inplace = True) 
  ```python

      data.reset_index(inplace = True)

  ```
 ### applying index from the begin:-
 -------------------------------------
  - df = pd.read_csv(_file location_ , index = "col name")

 ### arranging the index in ascending and descending order:-
 -------------------------------------------------------------
  - in ascending order:
  ```python

    data.sort_index(ascending = True , inplace = True)

  ```

  - in descending order
  ```python

    data.sort_index(ascending = False , inplace = True)

  ```

## filters:-
----------------
 - using filter to pick a specific data 
 -how to do that
 ```python

    filt = data["col_name"] == value # a filter that will return bool values
    data[filt] # the filter will be applied to the dataframe and raturn values of true 

 ```

## filter for multi values 
---------------------------
 - we can specify a list of values , the use it to apply a filter 

 ```python
    # list of countries to apply filter on
    list_of_conutries = ["Egypt" , "USA" , "UAE"]

    # filter using isin() method
    filt = data["Country"].isin(list_of_conutries)

    # applying the filter on the data 
    data[filt]

 ```

## assigning conditions with filters :-
----------------------------------------
 - we can assign conditions on the filter ensuring all condtion is going to happen
 - we use | , & operators --> make sure not to use and + or keywords in filters 
 - make sure also to use () for each condition 

 ```python

    filt = (data["Country"] == "Egypt") & (data["Contry"] == "UAE")  
    data[filt]

 ```

## filter strings:-
--------------------
 - we can filter string values inside a column by .str method

 ```python

  filt = data['LanguageHaveWorkedWith'].str.contains("Python" , na = False)
  data[filt]

 ```

## modifying columns :-
-----------------------
 
 * assigning the value of columns *
 =================================
  - create list of names and assign it to data.columns 
  ```python

    data.columns = ["col1" , "col2" , ...]

  ```
 
 * changing name of columns using list comprehension *
 ======================================================
  - assign data.columns to a list comprehension from
  ```python

    data.columns = [x.lower() for x in data.columns]

  ```
 * replaceing/modifing values of columns :-
 ===========================================
  - from str method and use replace 
  ```python

    data.columns = data.columns.str.replace("_" , "") # code to replace _ to empty string 

  ```
 * renaming columns *
 =====================
  - rename() method and use attribute columns where U pass a dictionary
  - dictionary: old value --> key , new value --> value 
  ```python

    data.rename(columns{"old_name":"new_name"})

  ```

## Updating data in rows
- we use `loc[]` and `iloc[]` to locate and change the value 
### changing multi values
- changing 2 cells in the data 
- we locate the row and the list of columns then assign the new value
- *syntax* : `data.loc[row , column] = new value`
```python
# code to change multi values in the dataframe
data.loc[2 , ["first" , "last"]] = ["mostafa" , "samir"]
```
### Changing a single value
- locating the value with `loc` or `iloc` then assign the new value
```python
# code to change a sigle value using iloc
data.iloc[2,2] = "mostafa_samir@gimal.com"
```

> changing the values without using the `loc` or `at` will cause an error 


# Applying function on the dataframe
- **we gonna talk about 4 functions** 
1. apply
2. applymap
3. map
4. replace 
## Apply
- useful in calling a function on our values
- **work on** : series , Dataframes
### apply on series  
- *Syntax* : `data.column_name.apply(func)` , we pass the function without ( ) 
- Ex: 
```python
# function that calculate the length of each element in the email column
data.email_address.apply(len)
```
- another example
```python
# design a function that return uppercase
def update_email(x):
    return x.upper()

# apply the function on the series email
data.email_address.apply(update_email) # without ()  because we do not want to execute the function when passing in the apply func
```

### apply on all series in the DataFrame
- *syntax* : `data.apply(func)`
- Ex
```python
# len function in this case will return the length of each series
data.apply(len)
```
>"note that **lambda** function work only on series not DataFrames "

### apply on entire DataFrame
- using the apply method in the DataFrame , we need to use a function that is okey to use on all objects in each series in the DataFrame
- *syntax* : `data.apply(func)`
- Ex
```python
# apply on the whole dataframe
data.apply(pd.Series.min) # return the min value in the series object 
```

## Applymap 
- **work on** : entire *DataFrame* <u>ONLY</u> 
- useful whan applying a function on every value in the dataframe 
- *syntax* : `data.applymap(func)`
- Ex
```python
# using apply map
data.applymap(len) # measuring the length of each element
```
> we need to use a function that can fit all data types in the dataframe

## Map
- **work on** : Series <u>ONLY</u>
- used when applying change on each value in the series
- *syntax* : `data['column'].map(func)`
- Ex
```python
# using the map function
data['first'].map(len)
```

## Replace 
- used to replace old values with new values
- **work on** : series 
- *syntax* : `data['column'].replace({"old_value" : "new_value"})`
- Ex
```python
# using the replcae method
data['last'] = dtf['last'].replace({"samir" : "Darsh"})
```

# Add and remove columns DataFrame

## Adding columns
- we can concatenate columns by the + sign
```python
# concatenating 2 columns into 1 column
data['first'] + " " + data['last']
```
> <mark style="background: #FF5582A6;">Note</mark> we cannot use (.) assign in this case 

- we noticed that we concatenated 2 columns but did not change the data frame
- in order to make change to the dataframe *we need to assign it to a new column*
```python
# making a new column called "full_name"
data['full_name'] = data['first'] + " " + data['last']
```

## Deleting columns
- in order to delete a column we will use `drop()` method
- *syntax* : `data.drop(columns = {"col_name"} , inplcae = True)`
```python
# using drop method to delete column
data.drop(columns = {'first' , 'last'} , inplcae = True)
```

## splitting a column into new columns 
- use the `split( )` method in the `str` module
```python
# using str.split method
data["fill_name"].str.split(" ")
```
- *out* : list that contain `n_ELEMENT` separated by space 
### unpacking of values
- we now have a list of outputs , how we can assign it to a new column
- if we directly assign the new values to columns without unpacking the pandas will call an error
- because when not unpacking the pandas assign 1 value (list) to 2 values (2 columns)
```python
# assign to new columns without unpacking 
dtf["first"] , df["last"] =  dtf['full_name'].str.split(" ")
```
- *out* : `too many values to unpack (expected 2)`
- **another mistake** : when we unpack and assign the new values in the new columns without putting them into list
```python
# wrong unpacking
dtf["first"] , df["last"] =  dtf['full_name'].str.split(" " , expand = True)
```
- now the columns will take the index values of the list
#### The right Unpacking is
```python
# the right unpacking
dtf[['first' , 'last']] = dtf['full_name'].str.split(" " , expand=True)
```

# Adding and removing rows in DataFrame
## appending rows 

- adding rows to the dataframe using `append( )` method
```python
# adding rows to the dataframe using append()
data.append({"first" : "sasa"} , ignore_index = True)
```
> <mark style="background: #D2B3FFA6;">note</mark> : new version of pandas removed `append()` method

### using another way to insert row inside the our dataframe
- using `loc` and `len(data)`
```python
data.loc[len(data)] = ["mostafa" , "samir" , "ali"]
```

- using `loc` and adding the new index and columns
```python
data.loc[4,:] = ["mostafa" , "samir" , "ali"] 
```

## Concatenating 2 dataframes
- we know that the `append()` method is removed in teh new version of pandas ,So we use another methods to insert and concatenate rows
- using `concat()` method
- *syntax* : `result = pd.concat(_data_frames_)`
```python
# concatenating 2 dataframes

# First DataFrame
df1 = pd.DataFrame({'id': ['A01', 'A02', 'A03', 'A04'],'Name': ['ABC', 'PQR', 'DEF', 'GHI']})
 
# Second DataFrame
df2 = pd.DataFrame({'id': ['B05', 'B06', 'B07', 'B08'],'Name': ['XYZ', 'TUV', 'MNO', 'JKL']})

# put the dataframes in list datatype and store it in a variable
frames = [df1, df2]

# converting the list into one dataframe by .concat()
result = pd.concat(frames)
display(result)
```

## Removing rows 
- we can use the same as we dropped the columns but instead we use `index = ` 
- dropping by index
```python
# code to drop row by index
data.drop(index = 4)
```

- making a filter and dropping rows by index in the filter

```python

# making a condition (filter) , then dropping this filter out of the data
filt = data["last"] == "ali"

''' getting the index of the filtered data ==> data[filt].index'''

# applying the filt to the data and dropping the filtered data
data.drop(index = data[filt].index)
``` 

# Sorting DataFrame
- sorting values by using `sort_values(by = )` method
- *syntax* : `data.sort_values(by = "col name")`
```python
# sorting values according to a column
data.sort_values(by = "last" , inplace = True)
```

## sorting by ascending order
- we use `ascending  = True` 
```python
# sorting in ascending order
data.sort_values(by = "last" , ascending = True ,inplace = True)
```

## sorting by descending order
- we use `ascending  = False 
```python
# sorting in ascending order
data.sort_values(by = "last" , ascending = False ,inplace = True)
```

## Sorting multi columns
- sorting in columns 1 and if the values in column 1 are the same , sort according to column 2
- we will pass the values in *list*
```python
# sorting on multi column
data.sort_values(by = ["first", "last"] , inplcae = True)
```

## Sorting multi columns in different ways
- imagine if we want to sort the first column in ascending and the second column in descending 
- we can do it if we pass 2 *bool values* in a list for *ascending* parameter
```python
# sort the first in descending and teh second in ascending
data.sort_values(by = ["first" , "last"] , ascending = [False , True] , inplace = True)
```

## returning the default index
- we want to reset the index to its default 
- we use `sort_index()`
```python
# return index to default
data.sort_index(inplace = True)
```

# Grouping 
- organizing data into groups according to categories of a specific column


# file handling in pandas





