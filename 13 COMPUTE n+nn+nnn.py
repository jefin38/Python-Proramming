i =int(input("Enter a number:"))
num= (i+ ((i*10)+i) + ((i*100)+(i*10)+i))
print(num)



import pandas as pd ufo = pd.read_csv('http://bit.ly/uforeports')

print(ufo.isnull().tail()) print(ufo.notnull().tail())

print(ufo.isnull().sum())

print(ufo.shape)

# if 'all' values are missing in a row, then drop that row (none are dropped in this case)

print(ufo.dropna(how='all').shape)

20

print(ufo.dropna(subset=['City', 'Shape Reported'], how='any').shape)

print(ufo['Shape Reported'].value_counts().head())

# fill in missing values with a specified value

print(ufo['Shape Reported'].fillna(value='VARIOUS', inplace=True)) # confirm that the missing values were filled in

print(ufo['Shape Reported'].value_counts().head()) drinks = pd.read_csv('http://bit.ly/drinksbycountry') print(drinks.head())

# every DataFrame has an index (sometimes called the "row labels")

print(drinks.index) # index and columns both default to integers if you don't define them

print(pd.read_table('http://bit.ly/movieusers', header=None, sep='|').head())

# identification: index remains with each row when filtering the DataFrame

print(drinks[drinks.continent=='South America'])

#selection: select a portion of the DataFrame using the index

print(drinks.loc[23, 'beer_servings'])