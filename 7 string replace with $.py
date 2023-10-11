string = input("enter a string")
char = string[0]
string = string.replace(char,'$')
print(char+string[1:])
