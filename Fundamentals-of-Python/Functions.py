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


## Nested Functions 

def talk(phrase):
    def say(word):
        print(word)
    
    words = phrase.split(' ')
    for word in words:
        say(word)

talk('I am going to buy the milk')

def count():
    count = 0

    def  increment():
        nonlocal count
        count = count + 1
        print(count)
    
    increment()

count()


## Closures

def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count
    
    return increment

increment = counter()

print(increment()) # 1
print(increment()) # 2
print(increment()) # 3
