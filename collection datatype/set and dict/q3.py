student={"name":"Alice","age":"20","grade":"A"}

print(student.keys())
print(student.values())

student["city"]="Delhi"
student["age"]=21

print(student)

del student["grade"]
print(student)

