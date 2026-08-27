print(".................method 1...........")    
print("\n")

for i in range (1,6,1):
    for s in range (5,i,-1):
        print(" ",end=" ")
    for j in range (1,i+1,1):
        print(j%2,end=" ")
    print(" ")


print("\n")
print(".................method 2...........")    
print("\n")

for i in range (1,6,1):
    for s in range (5,i,-1):
        print(" ",end=" ")
    for j in range (1,i+1,1):
        if j % 2 == 0 :
            print("0",end=" ")
        else :
            print("1",end=" ")
    print(" ")
