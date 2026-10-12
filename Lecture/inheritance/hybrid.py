"""
Hybrid Inheritance :

    => Combination of two inheritance.

                class A
                   |
                   |
         ----------------------
         |                    |
         |                    |
        class B             class C
         |                     |
         |                     |
         ----------------------
                    |
                    |
                 Class D
"""


class A:
    def top(self):
        print("This is class A")


class B(A):
    def left(self):
        print("This is class B")


class C(A):
    def right(self):
        print("This is class C")


class D(B, C):
    def bottom(self):
        print("This is class D")


obj = D()

obj.top()
obj.left()
obj.right()
obj.bottom()
