filter = lambda num, arr : [element for element in arr if element > num]



print("\nWelcome To data Analyzer and Transformer Program\n\n")
while True :
    array = [34,12,56,78,43,21,90]
    print("---------------------------------------------------------\n")
    print("Main Menu: \n")
    
    print("1.Input data ")
    print("2.Display Data Summary")
    print("3.Calculate Factorial ")
    print("4.Filter Data by Threshold ")
    print("5.Sort Data ")
    print("6.Display Dataset Statistics ")
    print("7.Exit Program ")

    chioce=int(input("\n\n Please Enter Your Chioce :"))

    match chioce :
     case 1 :
         print("Enter data for 1D array : \n ",array)
         
         print("\n Data has been stored succesfully! \n\n")

     case 2  :
        print("\n Data Summary \n")
        print("Total elements: ",len(array))
        print("Minimum value : ",min(array))
        print("Maximum value : ",max(array))
        
        print("Sum of all value : ",sum(array))
        
        def average ():
            global array
            total=sum(array)
            avg=total/len(array)
            return avg
        ans=average()
            
             
        print("Average  value : ",ans)
        print("\n\n")
     case 3:
        
        def factorial(num):
            if num<=1:
                return 1
            else :
                return num*factorial(num-1)
        num=int(input("Enter a number to calculate its factorial : "))    
        ans=factorial(num)
        print("factorial of ",num,"is",ans)

     case 4:
         threshold=int(input("Enter a threshold value to filter out data above this value : "))

         print("\nFiltered Data(Values >=",threshold ,") ")
         print(filter(threshold, array))

     case 5 :
         
        while True :
             print("\nChoose sorting option : ")
             print("1.Ascending ")
             print("2.Descending")
             print("3.Exit \n")
             chioce = int(input("Enter your chioce : "))

             match chioce :
                case 1:
                 asort=sorted(array)
                 print("\n\n Sorted Data in Ascending order: \n",asort)
                 
                case 2:
                 dsort=sorted(array,reverse=True)
                 print("\n\n Sorted Data in descending order: \n",dsort)
                 
                case 3 :
                 print("Exit..")
                 print("\n\n")
                 break
     case 6:
         print("\nDataset Statistics: \n")
         def satistics():
             global array 
             return {"minimum Value": min(array),"maximum Value": max(array),"Sum of all values":sum(array),
                     "Avrage Value": sum(array)/len(array)}
    
         ans=satistics()
         for key, value in ans.items():
             print(key, ":", value)
         print(" ")
        




         
     case 7 :
        print("\nThank you for using tha Data Analyzer and Transformer program. Goodbye! \n")
        break

        













         
         
            





