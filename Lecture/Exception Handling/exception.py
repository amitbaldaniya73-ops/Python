"""

Two type of error :

1. Comiple Time Error:
    => Syntax Error


2. Run Time Error :
    => Logical mistake of code
    => Exception
"""

a = 25
b = 0

try:
    c = a / b
    # print(a / b)
except TypeError:
    print("This is type error")
except ZeroDivisionError as e:
    print("not possible because of ", e)
except ValueError:
    print("This is Value Error")
else:
    print(c)
finally:
    print("Always execute...")
