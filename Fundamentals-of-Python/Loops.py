## Loops

## While loop

condition = True
while condition == True :
    print("The condition is True")
    condition = False

count = 0
while count < 10:
    print("The condition is True")
    count += 1

print("After the loop")


## For loop

items = [1, 2, 3, 4]
for item in items:
    print(item)

for item in range(15):
    print(item)

items = [1, 2, 3, 4]
for index, item in enumerate(items):
    print(index, item)

items = ["Kadir", "Helen", "Micheal", "Sophie"]
for index, item in enumerate(items):
    print(index, item)
