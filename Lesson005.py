import numpy as nm
from pandas import Series, DataFrame
import matplotlib.pyplot as plt


# df = pd.read_csv('file/sales.csv')
# print(type(df))4
obj = Series([4, 7, -5, 3])
# print(obj)

sdata = {'cali': 100, 'Ohio': 200, 'Oregon': 300, 'Texas': 400}
obj3 = Series(sdata)
# print(obj3)

states = ['cali', 'Ohio', 'xx', 'Texas']
obj4 = Series(sdata, index = states)
print(obj4)


