class Math:
    # def sum(self):
    #     num = 10
    #     print(f"Sum : {num+1}")

    # def sum(self, a, b):
    #     print(f"{a} + {b} = {a+b}")

    def sum(self, *args):
        # print(f"Sum of {a} and {b} and {c} ans is {a+b+c}")
        print(sum(args))

"""
Method Overloading

Class : Same
Method Name : Same
Parameters : Different


Method Overriding 

Class : Different
Method Name : Same
Parameters : Same
"""

obj = Math()

# obj.sum()
obj.sum(10, 20, 30)
