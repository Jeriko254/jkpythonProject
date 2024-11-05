temptrature=15

if temptrature>25:
    print("It is too hot")
else:
    print("It is too cold")

#A python program that checks 3 numbers and returns the smallest number
num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
num3=int(input("Enter a third number: "))

if num1<num2 and num1<num3:
    print(num1,"is the smallest number")
elif num2<num1 and num2<num3:
    print(num2,"is the smallest number")
else:
    print(num3,"is the smallest number")

#A program that checks 3 numbers and prints out the greates
num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
num3=int(input("Enter a third number: "))

if num1>num2 and num1>num3:
    print(num1,"is the greatest number")
elif num2>num1 and num2>num3:
    print(num2,"is the greatest number")
else:
    print(num3,"is the greatest number")

