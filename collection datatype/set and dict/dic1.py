student={ "name":input("Enter your name:"),"rollno":input("enter your rollno: "),
          "std": input("enter your std: ")}

print(student[(input("sarch for student daitail :  "))])

student["city"]="surat"
student["age"]="21"
print("update student daitail :",student)
del student[input("enter a delete fun:")]
print(student)
student.pop

for key,value in student.items():
    print(key,value)
