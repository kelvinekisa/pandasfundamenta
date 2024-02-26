import pandas as pd
import numpy as np
# OBJECT CREATION

# creating a series by passing a list of values.

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# creating a dataframe
dates = pd.date_range("20230101", periods=6)

# print(dates)

# creating a dataframe by passing a dictionary of objects.
df2 = pd.DataFrame(
    {
        "A": 1.0,
        'B': pd.Timestamp('20130102'),
        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
        'D': np.array([3] * 4, dtype='int32'),
        'E': pd.Categorical(['test', 'train', 'test', 'train']),
        'F': 'Foo',
    }
)
# print(df2)

# print(df2.dtypes)
print('Viewing data')
print(df2.head())
print('Tail')
print(df2.tail())

# display dataframe index
print('dataframe index')
print(df2.index)
print('dataFrame column')
print(df2.columns)

# Return a Numpy representation of the underlying data with DataFrame.to_numpy() without index or column labels
print('Dataframe to Numpy') # Array
print(df2.to_numpy())

print(df2.dtypes)

# describe() shows a quick statistic summary of your data
print(df2.describe())

# Transposing your data

print('Transposing your data')
print(df2.T)

# dataframe sort index. Sorts by an axis
print(df2.sort_index(axis=1, ascending=True))

# dataframe sort by values
print(df2.sort_values(by='B'))

# Selection
# GetItem([])
# Passing a single label selects a columns and yields a series
print(df2['A'])

# Passing a slice selects a matching rows
print(df2[0:3])

# selection by label
# selecting a row matching a label
# print(df2.loc[dates[0]])

# selecting all rows with a select column labels

print('Selecting all rows(:) with a select column label')
print(df2.loc[:, ['A', 'B']])

# for label slicing all labels are included:
print(df2.loc['20130102': '20130104', ['A', 'B']])


# selection by position: using dataFrame.iloc(), Dataframe.iat()
print('Selection by position')
# seect via the position of the passed integers
print(df2.iloc[3])

# Integer slices acts similar to numpy/python
print(df2.iloc[3:5, 0:2])

