num1 = 24
num2 = 18
gcd = 1
for i in range(1, min(num1, num2)):
  if num1 % i == 0 and num2 % i == 0:
    gcd = i
print("GCD of", num1, "and", num2, "is", gcd)





print("Containers: Dictionaries")

d = dict()

d = {'cat': 'cute', 'dog': 'furry'}

print("Dictionary: ",d)

print("Is the dictionary has the key 'cat'? ", 'cat' in d)

d['fish'] = 'wet'

print("After adding new entry to 'd': ",d)

print("Get an element monkey: ",d.get('monkey', 'N/A'))

print("Get an element fish: ",d.get('fish', 'N/A')) del d['fish']

print("After deleting the newly added entry from 'd': ",d)

print("Demo of dictionary comprehension: ") squares={x:x*x for x in range(10)}

print("Squares of integers of range 10: ")

for k,v in squares.items():

print(k,":",v)





