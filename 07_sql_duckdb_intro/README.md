# SQL with DuckDB

Watch this video on how to setup duckdb and dbeaver. 
[![setup duckdb and dbeaver and testing](https://github.com/kokchun/assets/blob/main/oop_advanced/dbeaver_setup.png?raw=true)](https://youtu.be/b9VMLSXKHwk)


## Setup

Follow [this link to install duckdb](https://duckdb.org/docs/installation/?version=stable&environment=cli&platform=macos&download_method=package_manager) on your computer.

Then we'll need the python client for connecting to duckdb through Python

```bash
uv pip install duckdb
```

Now [download and install dbeaver](https://dbeaver.io/download/), which is an IDE for viewing databases.

## DBeaver

First use the DuckDB CLI to create a new database file 

```bash
duckdb first_db.db
```

and then run a command so that it saves, lets say `desc` command to describe the database. Now there should be a database file called first_db.db saved in your file system. 

Inside of dbeaver
1. open new project, import from directory where your first_db.db file is 
2. establish a connection to your first_db.db file
3. create SQL script and start using SQL



## DuckDB cli

We start with using the cli so type

```bash
duckdb
```

You see that it is a transient in-memory database that starts, which is a temporary database that exists in memory only and has not been persisted to disk.

To create a database, just add a path to a database name, either existing or one that you want to create. 

```bash
duckdb <path_to_database.db>
```

Create a jokes table
```sql 
CREATE TABLE jokes (
    id INTEGER PRIMARY KEY,
    joke_text VARCHAR,
    rating INTEGER
);
```

Then insert some values
```sql
INSERT INTO jokes (id, joke_text, rating) VALUES
(1, 'Why don’t scientists trust atoms? Because they make up everything!', 8),
(2, 'Why did the scarecrow win an award? Because he was outstanding in his field!', 7),
(3, 'I told my wife she was drawing her eyebrows too high. She looked surprised.', 9),
(4, 'Why don’t skeletons fight each other? They don’t have the guts.', 6);
```

Also control that the table jokes have been populated by 

```sql 
SELECT * FROM jokes;
```

Now lets describe different database objects using

```sql
desc;
```

Here we can see that main is the default schema for DuckDB as we haven't specified any schemas when creating the table. 

```sql
-- both give same results here
desc jokes;
desc first_db.main.jokes;
```


That was funny, lets get some more jokes, but insert it by using an sql script. 

```sql
INSERT INTO jokes (id, joke_text, rating) VALUES
(5, 'Why don’t some couples go to the gym? Because some relationships don’t work out.', 8),
(6, 'I would avoid the sushi if I was you. It’s a little fishy.', 7),
(7, 'Want to hear a joke about construction? I’m still working on it.', 6),
(8, 'Why don’t programmers like nature? It has too many bugs.', 9),
(9, 'How does a penguin build its house? Igloos it together.', 1),
(10, 'A gothenburg person stands in queue for star wars. When someone cuts the line he says ge daj.', 2);
```

We'll use a meta command to read the sql script by

```sql
.read insert_values.sql
```

Lets remove all jokes that have less than 5 in ratings. 

```sql 
.read remove_bad_jokes.sql
```

## Meta commands
Some common meta commands

| Meta Command | Description                                 |
|--------------|---------------------------------------------|
| `.open`      | Opens a DuckDB database file.               |
| `.read`      | Executes SQL commands from a specified file.|
| `.schema`    | Shows the schema of tables in the database. |
| `.tables`    | Lists all tables in the connected database. |
| `.quit`      | Exits the DuckDB CLI.                       |
| `.help`      | Lists all available meta commands.          |


## Other videos :video_camera:

## Read more :eyeglasses:

From duckdb docs

- [Why duckdb](https://duckdb.org/why_duckdb)
- [Documentation](https://duckdb.org/docs/index)


Python client API

- [Data ingestion](https://duckdb.org/docs/api/python/data_ingestion)
- [Conversion between duckdb and python](https://duckdb.org/docs/api/python/conversion)
- [Python DB API](https://duckdb.org/docs/api/python/dbapi)
