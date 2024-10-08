i =int(input("Enter a number:"))
num= (i+ ((i*10)+i) + ((i*100)+(i*10)+i))
print(num)




import pandas as pd print("Creating dummy variables in pandas: ")

print()

#read the training dataset from Kaggle's Titanic competition train = pd.read_csv('http://bit.ly/kaggletrain')

print("Dataframe: ")

print(train.head())

print()

#use 'get_dummies' to create one column for every possible value print(pd.get_dummies (train.Sex).head())

print()

#drop the first dummy variable ('female') using the 'iloc' method print(pd.get_dummies (train.Sex).iloc[:, 1:].head())

print()

#add a prefix to identify the source of the dummy variables print(pd.get_dummies (train.Sex, prefix='Sex').iloc[:, 1:].head())

print()

# use 'get_dummies' with a feature that has 3 possible values

print(pd.get_dummies (train.Embarked, prefix='Embarked').head(10))

print()

#drop the first dummy variable ('C')

print(pd.get_dummies (train. Embarked, prefix='Embarked').iloc[:, 1:].head(10))

print() #0, 0 means C 1,0 means Q 0, 1 means S

#reset the DataFrame

train = pd.read_csv('http://bit.ly/kaggletrain')

print("Dataframe: ")

print(train.head())

print()

#pass the DataFrame to 'get_dummies' and specify which columns to dummy (it drops

#the original columns)

print(pd.get_dummies (train, columns=['Sex', 'Embarked']).head())

print()

#use the 'drop_first' parameter (new in pandas 0.18) to drop the first dummy variable

#for each feature

print(pd.get_dummies(train, columns=['Sex', 'Embarked'], drop_first=True).head())