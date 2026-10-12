# Single Inheritance

# Max Class => 2
# Min Class => 2


class A:
    num1 = None

    def setDataA(self):
        self.num1 = int(input("Enter first number : "))

    def getDataA(self):
        print(f"Number 1 : {self.num1}")


class B(A):
    num2 = None

    # num1, setDataA(), setDataB()

    def setDataB(self):
        self.num2 = int(input("Enter second number : "))

    def getDataB(self):
        print(f"Number 2 : {self.num2}")

    def sumOfNumber(self):
        print(f"{self.num1} + {self.num2} = {self.num1 + self.num2}")


b1 = B()

b1.setDataA()
b1.setDataB()

b1.getDataA()
b1.getDataB()


b1.sumOfNumber()

