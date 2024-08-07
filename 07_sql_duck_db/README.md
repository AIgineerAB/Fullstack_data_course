# SQL with DuckDB

<!-- [![video](https://github.com/kokchun/assets/blob/025ae8622a25d5522d11b21108f52f1df9388ea2/data_warehouse/snowflake_free_trial.png?raw=true)](https://github.com/kokchun/assets/blob/025ae8622a25d5522d11b21108f52f1df9388ea2/data_warehouse/snowflake_free_trial.png?raw=true) -->

> [!IMPORTANT] > [LINK TO VIDEO &nbsp; :video_camera:](https://)

## Setup

Follow [this link to install duckdb](https://duckdb.org/docs/installation/?version=stable&environment=cli&platform=macos&download_method=package_manager) on your computer.

Then we'll need the python client for connecting to duckdb through Python

```bash
uv pip install duckdb
```

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



## Other videos :video_camera:

## Read more :eyeglasses:

From duckdb docs

- [Why duckdb](https://duckdb.org/why_duckdb)
- [Documentation](https://duckdb.org/docs/index)
- [Data importing](https://duckdb.org/docs/data/overview)
- [CSV import](https://duckdb.org/docs/data/csv/overview)
- [CSV autodetection](https://duckdb.org/docs/data/csv/auto_detection)

Python client API

- [Data ingestion](https://duckdb.org/docs/api/python/data_ingestion)
- [Conversion between duckdb and python](https://duckdb.org/docs/api/python/conversion)
- [Python DB API](https://duckdb.org/docs/api/python/dbapi)
