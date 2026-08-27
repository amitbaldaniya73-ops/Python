list=[]
print(list.append(int(input("Enter a number:"))))

copy_list=list.copy()
copy_list.reverse()

if(list == copy_list):
    print("pelindrome")
else :
    print("not pelindrome")
