inputFile = "file1.txt"
readFile = open(inputFile, "r")

# output text file path
outputFile = "file2.txt"
writeFile = open(outputFile, "w")
ReadFileLines = readFile.readlines()

# Traverse in each line of the read text file
for x in range(0, len(ReadFileLines)):
 if(x % 2 != 0):
   writeFile.write(ReadFileLines[x]) 
 
 # printing the odd line
 print(ReadFileLines[x])
writeFile.close()
readFile.close()
