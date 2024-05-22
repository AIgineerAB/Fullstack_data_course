from fastapi import FastAPI, Depends
import duckdb
import uvicorn

app = FastAPI()


class DuckDB:
    def __init__(self) -> None:
        self.conn = duckdb.connect(database=":memory:", read_only=False)
        self.conn.execute(
            "CREATE TABLE items (id INTEGER, name VARCHAR), values INTEGER"
        )
        self.conn.execute("INSERT INTO items VALUES (1, 'Item 1', 20), (2, 'Item 2', 25)")

    def execute_query(self, query):
        result = self.conn.execute(query)
        return result.fetchall()


# Dependency
def get_db():
    db = DuckDB()
    return db


@app.get("/items")
def read_items(db: DuckDB = Depends(get_db)):
    return db.execute_query("SELECT * FROM items")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
