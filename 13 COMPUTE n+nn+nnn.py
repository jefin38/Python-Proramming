i =int(input("Enter a number:"))
num= (i+ ((i*10)+i) + ((i*100)+(i*10)+i))
print(num)




import pandas as pd

import numpy as np

#create a DataFrame from a dictionary (keys become column names, values become #data) optionally specify the order of columns and define the index df= pd.DataFrame(('id': [100, 101, 102], 'color': ['red', 'blue', 'red']], columns=['id', 'color'], index=['a', 'b', 'c'])

print("DataFrame from a dictionary: ")

print(df)

print()

#create a DataFrame from a list of lists (each inner list becomes a row)

29

print("DataFrame from a list of lists: ")

print(pd.DataFrame([[100, 'red'], [101, 'blue'], [102, 'red']], columns=['id', 'color']))

print()

#create a NumPy array (with shape 4 by 2) and fill it with random numbers between0&1 arr np.random.rand(4, 2)

print("Numpy array: ") print(arr)

print()

print("DataFrame from the above defined NumPy array: ")

print(pd.DataFrame(arr, columns=['one', 'two'])) print()

print("DataFrame of student IDs (100 through 109) and test scores (random integers

between 60 and 100: ") print(pd.DataFrame(('student':np.arange(100, 110, 1), 'test':np.random.randint(60, 101,

10))))

print()

#'set_index' can be chained with the DataFrame constructor to select an index print(pd.DataFrame(('student':np.arange(100, 110, 1), 'test':np.random.randint(60, 101,10))).set_index('student')) print()

#create a new Series using the Series constructor s=pd.Series(['round', 'square'], index=['c', 'b'], name='shape")

print(s)

print()

#concatenate the DataFrame and the Series (use axis=1 to concatenate columns)

print(pd.concat([df, s], axis=1))