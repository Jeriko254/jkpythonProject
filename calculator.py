
def addition(x, y):
    print(x+y)

def subtraction(x, y):
    print(x-y)

def multiplication(x, y):
    print(x*y)

def division(x, y):
    print(x/y)

print("Select Operations")
print(
    "1. Addition\n" \
    "2. Subtraction\n" \
    "3. Multiplication\n" \
    "4. Division\n")

operation = int(input("Enter choice of operation 1,2,3 or 4: "))

x = int(input("Enter the First Number: "))
y = int(input("Enter the Second Number: "))

if operation == 1:
    print(x, "+", y, "=", addition(x, y))

elif operation == 2:
    print(x, "-", y, "=", subtraction(x, y))

elif operation == 3:
    print(x, "*", y, "=", multiplication(x, y))

elif operation == 4:
    print(x, "/", y, "=", division(x, y))

else:
    print("Invalid Input")