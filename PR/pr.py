print("--------------------------------------------------------------------- ")
print("Welcome To The Interactive Personal Data Collector !")
print("   ")

name=input("please enter your name:")

age=int(input("please enter your age:"))

height=float(input("please enter your height in meters:"))

favourite_number=int(input("please enter your favourite number:"))
print("   ")

print("Thank You! Here Is The Information We Collected:")
print("   ")

print("Name: ",name,('type:',type(name),'Memory Address:' ,id(name)))

print("age: ",age,('type:',type(age),'Memory Address:' ,id(age)))

print("height: ",height,('type:',type(height),'Memory Address:' ,id(height)))

print("favourite_number: ",favourite_number,('type:',type(favourite_number),'Memory Address:' ,id(favourite_number)))
print("   ")

print("Your birth year is approximately:",2026-age,("based on your age to"),age)
print("   ")


print("Thank You For Using The Personal Data Collector. GoodBye!")
print("--------------------------------------------------------------------------- ")

