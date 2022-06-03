"""borrowed from
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html"""

import pandas

df1 = pandas.DataFrame([['a', 'b'], ['c', 'd']])
df1.to_csv("output.csv")
