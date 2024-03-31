## Control Statements
condition1 = True

if condition1 == True:
    print("The condition")
    print("was True")

print("outside if")

condition2 = False

if condition2 == True:
    print("The condition")
    print("was True")
else:
    print("The condition")
    print("was False")

condition3 = False
name = "Flavio"

if condition3 == True:
    print("The condition")
    print("was True")
elif name == "Roger":
    print("Hello Roger")
elif name == "Syd":
    print("Hello Syd")
elif name == "Flavio":
    print("Hello Flavio")
else:
    print("The condition")
    print("was False")
