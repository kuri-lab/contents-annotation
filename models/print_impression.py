import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 100)
pd.options.display.max_colwidth = 100
import sqlite3

con = sqlite3.connect("models/impression.db")
cursor = con.cursor()

cursor.execute("SELECT * FROM impressioncontents")
results = cursor.fetchall()

df = pd.read_sql_query("SELECT * FROM impressioncontents", con)

print(df[:10])