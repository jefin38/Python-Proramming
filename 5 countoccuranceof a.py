firstnamelist=[]
len = int(input("how many names"))
for i in range(0,len):
    fname= input("enter name")
    firstnamelist.append(fname)
count_a = 0
for names in firstnamelist:
     count_a +=names.count("a")
     print(count_a)
