print("Hello World!!")


n = 10
result = 0
try:
    result = n / 0 # this will raise zerodivisionerro

except ZeroDivisionError:
    print("Division by zero is not possible")

print(result)