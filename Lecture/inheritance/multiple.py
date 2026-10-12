"""
Multiple Inheritance

Min : 3
Max : Unlimited

        Class A                    Class B
          |                            |
          |                            |
          ------------------------------
                        |
                        |
                     Class C
"""


class College:
    def learning(self):
        print("I am learn python language")


class Intitute:
    def learning(self):
        print("I am learn java language")


class Student(College, Intitute):
    pass
    # learning() => college
    # learning() => intitute


amit = Student()

amit.learning()
amit.learning()
