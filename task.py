allemployees=[]
print("................Employeee Data.................")
while True :
    print("\n")
    print("press 1 for add employee")
    print("press 2 for view employee")
    print("press 3 for search employee")
    print("press 4 for update employee")
    print("press 5 for delete employee")
    print("press 6 for clear employee")
    print("press 7 for exit.....")

    choice=int(input("Enter a choice : "))
    match choice :
        
        case 1 :
            print("\n\n")
            empid=int(input("Enter employee id : "))
            name=input("Enter employee name : ")
            phone=input("Enter employee phone no:")
            email=input("Enter employee email :")
            role=input("Enter employee role :")
            salary=input("Enter employee salary :")
            address=input("Enter employee address :")

            employee={
                "id":empid,
                "name":name,
                "phone":phone,
                "email":email,
                "role":role,
                "salary":salary,
                "address":address
                }
            allemployees.append(employee)
            print("Employee add successfully..\n\n")

        case 2 :
            print("all employee ")
            for i in range(0, len(allemployees)):
                print(f"id: {allemployees[i]['id']}")
                print(f"name: {allemployees[i]['name']}")
                print(f"phone: {allemployees[i]['phone']}")
                print(f"email: {allemployees[i]['email']}")
                print(f"role: {allemployees[i]['role']}")
                print(f"salary: {allemployees[i]['salary']}")
                print(f"address: {allemployees[i]['address']}\n")
        case 3:
            print("search a employee")
            search=input("search a employee name: ")
            result=name.find(search)
            
            if result !=-1:
                print("search:",result)
            else :
                print("not found")
            



    
        case 4 :
            print("updated employee")
            id=input("enter employee id to update:")
            for i in employee:
                if  employee["id"]==id:
                    employee["id"]=input("Enter new id:")
                    employee["name"]=input("Enter new name:")
                    employee["phone"]=input("Enter new phone no:")
                    employee["email"]=input("Enter new email:")
                    employee["role"]=input("Enter new role:")

                    employee["salary"]=input("Enter new salary:")
            print("employee updated successfully!")
            
        case 5 :
            print("delete employee")
            id1=input("enter employee id to delete: ")
            for allemployees in employee:
                if  employee["id"]==id:
                    allemployees.remove(employee)
                    print("employee deleted successfully!")
        case 7:
            print("Exit..........")
            break 
        case _ :
            print("invalied choice..")
            

                
            

                    

                    
                
            


            
            












            
