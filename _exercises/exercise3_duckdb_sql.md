# Exercise 3 - DuckDB SQL repetition

In this exercise sheet, you will work with duckdb both in dbeaver and connect it with Python.

> [!NOTE]
> These exercises covers lecture 07-09.

## 0. Chess games

In lecture 08 we used duckdb CLI to read youtube data into the database and then used dbeaver to query the database. Now do similar but with [chessgames from lichess](https://www.kaggle.com/datasets/datasnaek/chess). 

&nbsp; a) Start with reading in this dataset into a duckdb database named chess.db 

For the following exercises, use dbeaver and duckdb to query the data

&nbsp; b) Find out the possible categories for winner column. 

&nbsp; c) Find out the possible categories for victory_status column. 

&nbsp; d) Check total number of games represented in the dataset.

&nbsp; e) Get statistics on the number draws, the number of white wins and number of black wins.

&nbsp; f) Check the top 10 most popular openings 

&nbsp; g) Which player has the highest ranking? 

## 1. How do Göteborg stad spend our tax money?

&nbsp; a) Connect Python to duckdb and save the data of two or more leverantörsfakturor (csv) in Göteborg stad into a duckdb database. 

&nbsp; b) Do an EDA of your choice using SQL.

&nbsp; c) Now try to join two or more files. 

&nbsp; d) See if you can connect to streamlit and make a simple dashboard.



