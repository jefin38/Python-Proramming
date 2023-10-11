year= int(input("enter current year"))
fut= int(input("enter future year"))
print("leap years are ")
for year in range(year, fut+1,2):
    if((year % 4 ==0)and year % 100!=0 or year % 400 == 0):
        print(year)
