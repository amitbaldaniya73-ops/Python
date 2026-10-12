"""
Class :
    => A blueprint of object.
    => Collection of data member and member function.

    Data Member == Attributes == Variable
    Member Function == Methods == Function (UDF)

Object :
    => Instance of class.


Class Syntax :

    class class_name:
        attributes
        methods
        constructors
        destructor

Object Syntax :

    obj = class_name()


Principle :

    1. Data Encpsulation : Write every code inside the class
        - Setter
        - Getter
        - Self Keyword
        - Del Keyword
        - Private Attributes
        - Constructor
        - Destructor
    2. Inheritance
    3.
    4. Data Abstraction.

"""

#  class Car:
#     # Attributes / Data Members

#     __company_name = None
#     __model = None
#     __color = None
#     __year = None

#     # setter
#     def setCarData(self):
#         print("\n")
#         self.__company_name = input("Enter car company name : ")
#         self.__model = input("Enter car modal name : ")
#         self.__color = input("Enter car color : ")
#         self.__year = int(input("Enter car realse year : "))

#     # getter
#     def getCarData(self):
#         print(
#             f"\nCompany Name : {self.__company_name} | Model : {self.__model} | Color : {self.__color} | Year : {self.__year}"
#         )


# cars = []

# size = int(input("Enter number of cars : "))

# for i in range(0, size):
#     c = Car()
#     cars.append(c)

# for obj in cars:
#     obj.setCarData()


# for obj in cars:
#     obj.getCarData()
#

#


# class City:

#     def __init__(self):
#         print("This is a constructor")

#     def greeting(self):
#         print("Welcome to the Surat City")


# c1 = City()
# c2 = City()
# c3 = City()
# c4 = City()


class Car:
    # Attributes / Data Members

    __company_name = None
    __model = None
    __color = None
    __year = None

    # Default Constructor
    def __init__(self):
        print("\n")
        self.__company_name = input("Enter car company name : ")
        self.__model = input("Enter car modal name : ")
        self.__color = input("Enter car color : ")
        self.__year = int(input("Enter car realse year : "))

    # Parameterized Constructor
    # def __init__(self, company_name, model, color, year):
    #   print("\n")
    #  self.__company_name = company_name
    # self.__model = model
    # self.__color = color
    # self.__year = year

    # Default Destructor
    def __del__(self):
        print("Thank you for Visit")

    # getter
    def getCarData(self):
        print(
            f"\nCompany Name : {self.__company_name} | Model : {self.__model} | Color : {self.__color} | Year : {self.__year}"
        )


# car1 = Car()
# car2 = Car("Tata", "Safari", "White", 2018)

# car2.getCarData()


cars = []

size = int(input("Enter number of cars : "))

for i in range(size):
    cars.append(
        Car(
            input("Enter car company name : "),
            input("Enter car model name : "),
            input("Enter car color : "),
            int(input("Enter car relase year : ")),
        )
    )

# for obj in cars:
#     obj.setCarData()


for obj in cars:
    obj.getCarData()
