i =int(input("Enter a number:"))
num= (i+ ((i*10)+i) + ((i*100)+(i*10)+i))
print(num)





import pandas as pd ufo = pd.read_csv('http://bit.ly/uforeports') print("Dataframe: ")

print(ufo.head(3))

print()

print("Selecting multiple rows and columns from a pandas DataFrame using 'loc": ")

print()

#loc method is used to select rows and columns by label print("First row, all columns: ")

print(ufo.loc[0,:])

print()

print("First 3 rows, all columns: ")

print(ufo.loc[[0, 1, 2), :))

print()

#rows 0 through 2 (inclusive), all columns

print(ufo.loc[0:2, :)

print() #this implies "all columns", but explicitly stating "all columns" is better

print(ufo.loc(0:21)

print()

print("First 3 rows, only one column 'City': ")

print(ufo.loc[0:2, 'City'])

print()

print("First 3 rows, two columns 'City' and 'State': ")

print(ufo.loc[0:2, ['City', 'State']])

print() print("Accomplish the same thing using double brackets: ")

#using 'loc' is preferred since it's more explicit print(ufo['City', 'State']].head(3))

print() print("First 3 rows, columns 'City' through 'State":")

print(ufa.loc[0:2, 'City':'State'])

print()

print("Accomplish the same thing using 'head' and 'drop": ")

print(ufo.head(3).drop("Time", axis-1))

print()

print("Rows in which the 'City' is 'Oakland', column 'State":")

print(ufo.loc[ufo.City='Oakland', 'State'])

print()

print("Accomplish the same thing using 'chained indexing":")

#using 'loc' is preferred since chained indexing can cause problems

print(ufo[ufo.City=="Oakland'] State)

print()

print("Selecting multiple rows and columns from a pandas DataFrame using "iloc": ")

print()

print("Rows in positions 0 and 1, columns in positions 0 and 3: ")

print(ufo.iloc[[0, 1], [0, 3]])

print()

print("Rows in positions 0 through 2 (exclusive), columns in positions 0 through 4

(exclusive): ")

print(ufo.iloc[0:2, 0:41)

print()

print("Rows in positions 0 through 2 (exclusive), all columns: ")

print(ufo.iloc[0:2, :)

print()