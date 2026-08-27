a=int(input("enter a first number :"))
b=int(input("enter a second number :"))

#method 1
a,b = b,a

print("swap of A:",a)
print("swap of B:",b)

#method2
temp=a
a=b
b=temp
print("swap of A:",a)
print("swap of B:",b)
