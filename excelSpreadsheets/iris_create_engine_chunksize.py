# SOURCE https://medium.com/@apoor/quickly-load-csvs-into-postgresql-using-python-and-pandas-9101c274a92f
# FILENAME iris_create_engine_chunksize.py

import pandas as pd
from sqlalchemy import create_engine
import psycopg2



# This CSV has no header so pass
# columns names as an argument
columns = [
  "sepal_length",
  "sepal_width",
  "petal_length",
  "petal_width",
  "class"
]

# Instantiate sqlalchemy.create_engine object
engine = create_engine('postgresql://postgres:password@localhost:5432/iris')

# Create an iterable that will read "chunksize = 1000" rows
# one at a tiem from the CSV file

for df in pd.read_csv("iris.csv",names=columns,chunksize=1000):
    df.to_sql(
        'iris_dataset',
        engine,
        index=False,
        if_exists='append' # if the table already exists, append this data
    )
