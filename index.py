import pandas as pd

df = pd.DataFrame(
    {
        'name': [
            'Braud, Mr. Owen Harris',
            'Allen, Mr. William Henry',
            'Bonnel, Miss. Elizabeth',
        ],
        'Age': [22, 35, 58],
        'Sex': ['Male', 'Male', 'Female']
    }
)
print(df)
print('Print age')
# When selecting a single column of a pandas DataFrame, the result is a pandas Series. To select the column,
# use the column label in between square brackets [].
# each column in a dataframe is a series
print(df['Age'])
print(df['Sex'])

# DO SOMETHING WITH A DATAFRAME OR SERIES

# Oldest
print(df['Age'].max())
# Methods are functions so use parenthesis
print(df.describe()) # Provides a quick overview of the numerical data in a dataframe. The textual data are not taken into account.

# REMEMBER
"""
Import the package, aka import pandas as pd
A table of data is stored as pandas DataFrame
Each column in a dataFrame is a series
you can do things by applying a method to a Dataframe or Series
"""
