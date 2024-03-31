## Lists

dogs = ["Roger", 1, "Syd", True, "Quincy", 7]

print("Roger" in dogs)
print("Ali" in dogs)

print(dogs[0])

dogs[1] = "Pamuk"

print(dogs[1])
print(dogs[-1])
print(dogs[2:])
print(dogs[:3])

print(len(dogs))

dogs.append("Judah")
print(dogs)

dogs.extend(["Mahmut", 23 , "Kai"])
print(dogs)

dogs += ["White"]
print(dogs)

dogs.remove("Syd")
print(dogs)

print(dogs.pop())
print(dogs)


items = ["Roger" , 1, "Syd", True, "Quincy", 7]

items.insert(2, "Test")
print(items)

items[1:1] = ["Test1", "Test2"]

print(items)

## Sorting Lists

items = ["Roger" ,"syd","Quincy", "ali", "Kadir"]

items.sort()
print(items)

items.sort(key=str.lower)
print(items)

items = ["Roger" ,"syd","Quincy", "ali", "Kadir"]

itemscopy = items[:]
items.sort(key=str.lower)

print(items)
print(itemscopy)

items = ["Roger" ,"syd","Quincy", "ali", "Kadir"]

sorted(items, key=str.lower)

print(items)
