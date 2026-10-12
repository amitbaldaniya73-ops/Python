# f = open("demo.txt", "rt")

# # print(f.readline())
# # print(f.readlines())

# # for text in f.readlines():
# #     print(text, end="")

# # print(f.read())

# for text in f:
#     print(text, end="")

# f.close()


# f = open("demo.txt", "a")

# for i in range(1, 101):
#     f.write(f"{i}\t")

# f.close()


# open("test.txt", "x")


# f = open("test.txt", "a")

# data = input("Enter any message : ")
# f.write(f"{data}\n")

# print("\nWritten successfully...\n")

# print("\n====== Read File ========\n")
# f = open("test.txt", "r")

# print(f.read())

# f.close()


# with open("demo.txt", "at") as f:
#     f.write("Hello World\n")


# with open("demo.txt", "rt") as f:
#     print(f.read())


with open("image.png", "rb") as f:
    img_file = f.read()


with open("new_image.png", "wb") as f:
    f.write(img_file)
