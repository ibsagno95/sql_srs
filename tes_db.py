import duckdb
con = duckdb.connect(database="data/sql_exercises.duckdb",read_only=False)

test= con.execute("SELECT * FROM memory_state").df()

print(test)
