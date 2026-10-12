array = []

row = int(input("enter a row:"))
col = int(input("enter a column: "))
for i in range(0, row):
    arr = []
    for j in range(0, col):
        num = int(input(f"Enter array[{i}][{j}]: "))
        arr.append(num)
    print()
    array.append(arr)

    sum = 0
    length = 0

for arr in array:
    for element in arr:
        print(element, end=" ")
        length += 1
        sum += element

    print()

print("sum of elements:", sum)
print("length of elements:", length)
print("avg of elements: ", sum / length)
