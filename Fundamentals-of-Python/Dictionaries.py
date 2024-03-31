## Dictionaries

dog = { "name": "Roger", "age": 8 }

print(dog["name"])

dog["name"] = "Syd"

print(dog)

dog = { "name": "Roger", "age": 8 , "color": "green" }

print(dog.get("name"))
print(dog.get("color"))
print(dog.get("color", "brown"))

print(dog.pop("name"))
print(dog)

print(dog.popitem())
print(dog)

dog = { "name": "Roger", "age": 8 , "color": "green" }

print("color" in dog)
print(dog.keys())
print(list(dog.keys()))
print(list(dog.values()))
print(list(dog.items()))

print(len(dog))

dog["faorite food"] = "Meat"

print(dog)

del dog['color']

print(dog)

dogCopy = dog.copy()

print(dog)
