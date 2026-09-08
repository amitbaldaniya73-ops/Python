print("Welcome to the Student Data Organizer! \n\n")

allstudents=[]

while True :
    
    print("press 1 for add student")
    print("press 2 for display all students ")
    print("press 3 for update student information")
    print("press 4 for delete student")
    print("press 5 for display subjects offered")
    print("press 6 for exit.....")

    choice=int(input("\nEnter a choice : "))
    match choice :
        
        case 1 :
            print("\n\n")
            studentid=int(input("Enter student id  : "))
            name=input("Enter student name : ")
            age=input("Enter student age :")
            grade=input("Enter student grade :")
            dateofbirth=int(input("Enter date of birth(YYYY-MM-DD)  :"))
            subject=input("Enter subjects(comma-seprated) :")
            



            student={
                "studentid":studentid,
                "name":name,
                "age":age,
                "grade":grade,
                "dateofbirth": dateofbirth,
                "subjects":subject
                }
            allstudents.append(student)
            print("student add successfully..\n\n")

        case 2 :
            if len(allstudents)==0:
                print("\n \n  not a added student \n")
            else :
                print("all student \n")
                for i in range(0, len(allstudents)):
                    
                    print(f"studentid: {allstudents[i]['studentid']}")
                    print(f"name: {allstudents[i]['name']}")
                    print(f"age: {allstudents[i]['age']}")
                    print(f"grade: {allstudents[i]['grade']}")
                    print(f"dateofbirth: {allstudents[i]['dateofbirth']}")
                    print(f"subjects: {allstudents[i]['subjects']}\n")
      
        case 3 :
            if len(allstudents)==0:
                print("\n\n not a added employee \n")
            else :
                studentId=int(input("enter student id to update:"))
                for student in allstudents :
                    if  student["studentid"]==studentId:
                        student["studentid"]=input("Enter new studentid:")
                        student["name"]=input("Enter new name:")
                        student["age"]=input("Enter new age :")
                        student["grade"]=input("Enter new grade:")
                        student["dateofbirth"]=input("Enter new date of birth:")
                        student["subjects"]=input("Enter new subjects:")
                print("student updated successfully!")
                
        case 4 :
            if len(allstudents)==0:
                print("\n\n not a added student \n\n")
            else :
                print("delete student")
                sid=int(input("enter student id to delete: "))
                for i in range(len(allstudents)):
                    if allstudents[i]["studentid"] == sid:
                        allstudents.remove(allstudents[i])
                        break
                print("student deleted successfully!")      
           
        case 5:
            if len(allstudents)==0:
                if len(allstudents)==0:
                    print("\n\n not a added student \n\n")
            else :
                
                allNewSubjects = {}
                allNewSubjects = set(allNewSubjects)
                
                for i in range(0, len(allstudents)) :
                    newSub = allstudents[i]['subjects'].split(',')
                    for j in range(0, len(newSub)) :
                        allNewSubjects.add(newSub[j])
                allNewSubjects = list(allNewSubjects)


                print("Subjects :",allNewSubjects)
            
            
                

        case 6:
            print("Exit..........")
            break 
        case _ :
            print("invalied choice..")
            

                
            


