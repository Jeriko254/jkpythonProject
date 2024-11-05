courses=["MIT" ,"DATASCIENCE","CYBERSECURITY"]
print(courses)
#acccessing an element in an array.
print(courses[1])

#looping through an array
for y in  courses:
    print("Course is",y)

#adding a new element
courses.append("ANDROID DEVELOPMENT ")
print(courses)

#Deleting an element
courses.remove("MIT")
print(courses)