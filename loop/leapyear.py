year1 = int(input("enter starting year:"))
year2 = int(input("enter ending year:"))

while year1 <= year2:
    year1 += 1

if year1 % 4 == 0:
    print(year1)
