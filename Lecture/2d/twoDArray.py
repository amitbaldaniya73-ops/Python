"""
Array :
    => An Collection of multiple elements of the integer (same) datatype.


1D Array :
    => An Collection of multiple elements of the integer datatype.

    array = [10,20,30,40,50]
    index    0  1  2  3  4

    array[0]

MD Array :
    2D, 3D, 4D ... ND

    =>  2D Array
    => An Collection of One Dimentional Array.
    => row and column
    => Matrix

    => Row is defiend number of 1D Array
    => Column is defiend 1D Array elements

    [
          0    1    2
      0  [10   20   30]
      1  [40   50   60]
      2  [70   80   90]  3*3
    ]
"""

# array = [ [10,20,30], [40,50,60], [70,80,90] ]

array = []

row = int(input("Enter row : "))
col = int(input("Enter column : "))

print("\n Array Input\n")

for i in range(0, row):
    arr = []
    for j in range(0, col):
        num = int(input(f"Enter array[{i}][{j}] : "))
        arr.append(num)

    print()
    array.append(arr)



arraySum = 0
length = 0

print("\n Array Output\n")

for arr in array:
    for element in arr:
        print(element, end=" ")
        length += 1
        arraySum += element

    print()


print("Sum : ", arraySum)
print("Length :", length)
print("Avg : ", arraySum / length)


    
