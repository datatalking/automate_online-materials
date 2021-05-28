# SOURCE https://medium.com/@apoor/quickly-load-csvs-into-postgresql-using-python-and-pandas-9101c274a92f
# SOURCE https://towardsdatascience.com/python-and-postgresql-how-to-access-a-postgresql-database-like-a-data-scientist-b5a9c5a0ea43
# FILENAME pandas_to_postgres.py

import pandas as pd
from sqlalchemy import create_engine

# TODO run check if has a header, use header excel scrubber if blank
# TODO else figure out what can be in header, factor into james neuralnet
# This CSV doesn't have a header so pass
# column names as an argument
columns = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
    "class"
]

# TODO create a prompt for file name, also scan for file name and number 10 at a time
# Load in the data
df = pd.read_csv("iris.csv", names=columns)

# Instantiate sqlalchemy.create_engine object
engine = create_engine('postgresql://postgres:password@localhost:5432/iris')

# Save the data from dataframe to
# postgres table "iris_dataset"
df.to_sql(
    'iris_dataset',
    engine,
    index=False # Not copying over the index
)