# What kind of data does pandas handle?
# import the package

import pandas as pd
import numpy as np

# SERIES
# Is a one dimensional array capable of holding any data. The axis labels are collectively referred to as the index.
# The basic method to create  series is to call.

# s = pd.Series(data, index=index) # Data can be anything: dict, ndarray, scalar value.
s = pd.Series(np.random.random(5), index=['a', 'b', 'c', 'd', 'e'])
print(s)

print(s.index)

print(pd.Series(np.random.random(5)))

# From dict
d = {
    'b': 1.0,
    'a': 0.0,
    'c': 2.0
}
print(pd.Series(d))
# if an index is passed, the values in data corresponding to the labels in the index will be pulled out.

print(pd.Series(d, index=['b', 'c', 'd', 'a'])) # NaN is the standard missing data marker used in pandas

# FROM A SCALAR VALUE

