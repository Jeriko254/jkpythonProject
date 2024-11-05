try:
    number=4
    print(number)
except:
    print("An error occurred")

num1=6
num2=0
try:
    print(num1 / num2)
except:
    print("A zero division  error occurred")
finally:
    print("Success")
