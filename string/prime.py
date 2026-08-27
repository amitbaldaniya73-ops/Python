num=int(input("Enter a number:"))
if num<=1:
    print(" it is a not prime number")
else :
    for i in range(2,num):
        if num % i==0:
            print("Not Number")
            break

    else :
        print("prime number")
   

    
