class persons:
    def __init__(self,name,gender,age):
        self.name= name
        self.gender=gender
        self.age=age

    def movement(self):
        print("person is walking")

person1=persons("Jerry","Male",21)
print(person1.name)

person2=persons("Korir","Male",22)
print(person2.name)

person3=persons("Faith","Female",25)
print(person3.name)