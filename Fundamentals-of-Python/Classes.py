## Classes

class Dog1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("hav!")

roger1 = Dog1("Roger", 8)

print(roger1.name)
print(roger1.age)

roger1.bark()

class Animal:
    def walk (self):
        print("Walking...")

class Dog2(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("hav!")

roger2 = Dog2("Roger", 8)

roger2.bark()
roger2.walk()
