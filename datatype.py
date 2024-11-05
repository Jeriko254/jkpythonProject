
number=50 #integer
second=45.90 #float
greeting="hello there" #string
isPythoninteresting = True #boolean

#datastructure-multiple values stored in a single variable
cars=["toyota","nissan","bmw"]#list-ordered and changeable
fruits=("banana","apple","orange")#Tuple-ordered but unchangeable
countries={"kenya","United Kingdom","Algeria"}#set-elements are unordered and unchangeable
student={
    "firstname":"Jane",
    "lastname":"Doe",
    "age":23,
     "course":"computer science",
}#dictionary-key value pair

print(cars)
print(fruits)
print(countries)
print(student)
print(student["course"])


print(number)
print(second)
print(isPythoninteresting)

#determining a datatype
print(type(countries))
print(type(student))

#Typecasting-converting one datatype to another
print(float(number))
print(int(second))
