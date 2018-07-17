import pandas as pd
import numpy as np

df = pd.read_csv('./example.csv')

# get table
print(df)

# get ndarray
print(df.get_values())

# get value by column and index
print(df.get_value(2,2))

print(df.index)

print(df.columns)


