a = 5
b = 0
try:
    c = a / b

except ZeroDivisionError as e:
    print("Not possible becuse of ", e)

else:
    print(c)

finally:
    print("Always execute...")
