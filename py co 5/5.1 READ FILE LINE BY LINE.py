with open('file.txt') as f:
 lines = [line for line in f]
print(lines)
# removing the new line characters
with open('file.txt') as f:
 lines = [line.rstrip() for line in f]
print(lines)
