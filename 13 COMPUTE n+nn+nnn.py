i =int(input("Enter a number:"))
num= (i+ ((i*10)+i) + ((i*100)+(i*10)+i))
print(num)




import pandas as pd

#change display options in pandas

#read a dataset of alcohol consumption into a DataFrame drinks = pd.read_csv('http://bit.ly/drinksbycountry') print("Shape: ", drinks.shape)

print()

# check the current setting for the 'max_rows' option pd.get_option('display.max_rows') print(drinks)

print()

#overwrite the current setting so that all rows will be displayed pd.set_option('display.max_rows',2)

print(drinks)

print()

#reset the 'max_rows' option to its default pd.reset_option('display.max_rows')

print(drinks)

print()

#add two meaningless columns to the drinks DataFrame

drinks['x'] = drinks.wine_servings * 1000

drinks['y'] = drinks.total_litres_of_pure_alcohol * 1000 print(drinks.head())

print()

# use a Python format string to specify a comma as the thousands separator

pd.set_option('display.float_format', '(:,}'.format)

print(drinks.head())

print()

#read the training dataset from Kaggle's Titanic competition into a DataFrame train = pd.read_csv('http://bit.ly/kaggletrain')

# an ellipsis is displayed in the 'Name' cell of row 1 because of the 'max_colwidth' option pd.get_option('display.max_colwidth')

print(train.head())

print()

#overwrite the current setting so that more characters will be displayed pd.set_option('display.max_colwidth', 1000)

print(train.head())

print()