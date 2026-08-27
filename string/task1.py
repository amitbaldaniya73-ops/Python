while True:

    name=input("Enter the name:")
    rollno=int(input("Enter your roll no:"))
    print("-------enter the 3 subjects marks-----")
    sub1=int(input("enter the first subject marks:"))
    sub2=int(input("enter the second subject marks:"))
    sub3=int(input("enter the third subject marks:"))

    total_marks=sub1+sub2+sub3
    per=total_marks/3
    print("total marks:",total_marks)
    print("percentage:",per)
    match per:
        case per if per >=90:
            print("Grade A1")
        case  per if per>=80:
            print("Grade A2")
        case  per if per>=70:
            print("Grade B1")
        case  per if per>=60:
            print("Grade B2")
        case  per if per>=50:
            print("Grade C1")
        case  per if per>=40:
            print("Grade C2")
        case  per if per>=33:
            print("Grade D")
        case  per if per>=0:
            print("YOU ARE FAIL..")
    print("\n...................................\n")
            
    
