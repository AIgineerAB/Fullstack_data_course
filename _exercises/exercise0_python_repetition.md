# Exercise 0 - Python repetition

In this exercise sheet, you will get repetition of core Python and apply into exercises which are related to data processing.

> [!NOTE]
> These exercises covers lecture 01.

## 0. Hire IT employee data

In a company `Hire IT`, there are these employees.

| employeeID | name    | department | salary |
| ---------: | :------ | :--------- | ------ |
|          0 | Alice   | HR         | 31000  |
|          1 | Bob     | IT         | 41000  |
|          2 | Charlie | HR         | 28000  |

&nbsp; a) Create a list of dictionaries to represent this data, where each dictionary represents each row.

&nbsp; b) Extract the second record in this dataset.

&nbsp; c) Extract all rows from this dataset and print it in this format

```
Alice works in department HR and earns 31000.
Bob works in department IT and earns 41000.
Charlie works in department HR and earns 28000.
```

&nbsp; d) Find out the average salary in Hire IT.

&nbsp; e) Find out the average salary among the HR department in Hire IT.

&nbsp; f) Extract all records where the department is HR.

&nbsp; g) Find all unique departments in this list.

For the following exercises the data has now been updated with the age column

| employeeID | name    | department | salary | age |
| ---------: | :------ | :--------- | ------ | --- |
|          0 | Alice   | HR         | 31000  | 26  |
|          1 | Bob     | IT         | 41000  | 37  |
|          2 | Charlie | HR         | 28000  |     |

&nbsp; h) Add this age column into our list of dictionaries. `None` should be used for empty fields.

&nbsp; i) A new employee named David starts at the IT department, with salary 35000 and has the age 30. Create a function to add this record to the dataset.

## 1. Gotta catch em all

&nbsp; a) Define a Pokemon class with attributes for name, type, and level. Instantiate a pokemon named Pikachu and give it an electric type with level 10.

&nbsp; b) Implement `__str__()` method to display the Pokemon's details. Also implement a `__repr__()` method.

&nbsp; c) Create a subclass WaterPokemon that inherits from Pokemon and add a unique method splash. This method prints out the pokemons name and that it splashes some water.

&nbsp; d) Now instantiate two Squirtles and a Polywag. Squirtles and Polywags are of type WaterPokemon.

&nbsp; e) Loop through a tuple of all your instantiated pokemons and print them out.

Printing out details are just that fun. It's time for battle.

&nbsp; f) To implement battling we need to do the following:

- add an attribute hp (healthpoints) to Pokemon class.
- implement a (pseudo)private method take_damage that subtracts the damage on the healthpoints
- implement an attack method in the Pokemon class that takes in another Pokemon as an argument. It inflicts damage on other pokemon based on its own level times 2. Print out damage taken and life points left on the pokemon. When damage exceeds the life points, the pokemon is fainted. 

&nbsp; g) Instantiate two pokemons and let them battle until one has fainted and announce a winner. They take turns in fighting one attack at a time.

&nbsp; h) Feel free to implement more features.


## 2. Analyze a log file 

It is common to log from different softwares and systems so that you always can go back to find out what happened, e.g. for debugging purposes. Under the data directory, there is a short log from a data engineering tool called data build tool (dbt), which is used for data transformations with SQL and jinja templating language. 

There seem to have been some errors during runs. You are tasked to read this log using Python and parse it to find some useful information for debugging. Print them out in a nicely formatted way. 

&nbsp; a) Find specific error messages and codes to understand the nature of the issues encountered.

&nbsp; b) Identify timestamps when the errors happened. 

&nbsp; c) Find performance metrics.

&nbsp; d) Find application information.

&nbsp; e) Are there some other valuable information that can be extracted the log?


## 3. Theory questions

These study questions are good to get an overview of how snowflake works.

&nbsp; a) What is the difference between dictionary and lists?

&nbsp; b) What are postional arguments in functions?

&nbsp; c) What is the difference between using postional arguments and keyword arguments in functions?

&nbsp; d) What is the difference between a list and a tuple?

&nbsp; e) Explain the concept of Python's dynamic typing.

&nbsp; f) What is the purpose behind the `__repr__()` method in a class?

&nbsp; g) How does `__str__()` method differ from `__repr__()` method?

&nbsp; h) Why do you want to encapsulate objects? 

&nbsp; i) What are the pillars of OOP?

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology              | explanation |
| ------------------------ | ----------- |
| dictionary               |             |
| list                     |             |
| record                   |             |
| list comprehension       |             |
| append                   |             |
| field                    |             |
| row                      |             |
| column                   |             |
| dictionary comprehension |             |
| statement                |             |
| argument                 |             |
| boolean                  |             |
| class                    |             |
| conditional              |             |
| exception                |             |
| function                 |             |
| keyword arguments        |             |
| module                   |             |
| object                   |             |
| return statement         |             |
| tuple                    |             |
| type                     |             |
| self                     |             |
| instatiate               |             |
| iterating                |             |
| encapsulation            |             |
|                          |             |
|                          |             |
|                          |             |
