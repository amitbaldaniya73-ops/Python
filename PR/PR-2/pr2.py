while True:
    print("WELCOME TO THE PATTERN GENERATOR AND NUMBER ANALYZER!")
    print("\n\n")
    print("SELECT AN OPTION:")
    print("1.Right-angle Triangle")
    print("2.pyramid")
    print("3.Left-angle Triangle")
    print("4.Analyze a range of number")
    print("5.EXIT.......")

    choice  =int(input("Enter Your Choice:"))


    match choice:
        case 1:
            n=int(input("Enter The Number of rows for the pattern: "))
            print("\n\n PATTERN:")

            for i in range (1,n+1):
                for j in range (1,i+1,1):
                    print(j,end=" ")
                print("")
            print("\n")

        

        case 2:
            n=int(input("Enter The Number of rows for the pattern: "))
            print("\n\n PATTERN:")

            for i in range(1, n + 1,1):
               print(" " * (n - i) + "* " * i)
            print("\n")

               
        
        case 3:
            n=int(input("Enter The Number of rows for the pattern: "))
            print("\n\n PATTERN:")


            for i in range (1,n+1):
                for s in range(5,i,-1):
                    print(" ",end=" ")
                for j in range (1,i+1,1):
                    print(j,end=" ")
                print("")
            print("\n")

        case 4:
            n1=int(input("Enter the start of the range:"))
            n2=int(input("Enter the end of the range:"))

            for num in range (n1,n2+1):
                if num%2==0 :
                    print("Number",num,"is even")
                else :
                    print("Number",num,"is odd")
            sum=0
            for num in range(n1,n2+1):
                sum=sum+num
            print("sum of all number from",n1,"to",n2,"is :",sum)
            print("\n")
        case 5:
            print("Exit...")
            break












            


        
