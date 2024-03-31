## Functions

def hello(name=" my friend"):
    print('Hello!' + name)

hello(" Kadir")
hello(" Arda")
hello(" Ali")
hello()

def hello(name, age):
    print('Hello' + name + ", you are " + str(age) + " years old!")

hello(" Murat" , 39)

def change(value):
    value["name"] = "Berfin"

val = {"name": "kaan"}
change(val)

print(val)

def hello(name):
    print('Hello' + name + '!')
    return

def hello(name):
    if not name:
        return
    print('Hello ' + name + '!')

hello("Kaan")

def hello(name):
    print('Hello ' + name + '!')
    return name, "Kaan", 8

print(hello("Syd"))


## Variable Scope

age = 8 

def test():
    print(age)

print(age) # 8
test() # 8

def test():
    age = 8
    print(age)

print(age)
test()
