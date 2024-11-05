#Built-in functions

y=max(34,56,45,32)
print(y)
x=min(40,67,22)
print(x)

z=pow(2,3)
print("The result is",z)

#user-defined functions
def greeting():
    print("Hello there")
greeting()#calling the function

def multiply():
    a=42
    b=19
    print(a*b)
multiply()

#Parameters/variable and Argument/Value
def add(x,y):
    print(x+y)
add(4,5)
add(54,78)

def employee(fullnmae,age,postion,status):
    print(fullnmae,age,postion,status)
employee("Jeriko",21,"Software Engineer","single")
employee("Janet",23,"Cloud Engineer","dating")
employee("Laurent",31,"CEO","single")
employee("Glory",24,"Teacher","married")






