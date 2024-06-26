## String

"Ali"
'Ali'
name = "Ali"
name += " is my name"
age = str(39)
print(name)

print("""Ali is

24

years old
""")

## String Methods

# isalpha()
# isalnum()
# isdecimal()
# lower()
# islower()
# upper()
# isupper()
# title()
# startsswith()
# endswith()
# replace()
# split()
# strip()
# join()
# find()

name = "Ali"
print("ali".upper())
print("ALI".lower())
print("aLi ersoy".title())
print("ersoy".islower())
print(len(name))
print("li" in name)

## Escaping Characters

name1 = 'Ka"\dir'
print(name1)

name2 = 'Ka"\ndir'
print(name2)

name3 = 'Ka\\dir'
print(name3)

## String Characters & Slicing

name4 = 'John'

print(name4[1])  # o
print(name4[3])  # n
print(name4[-3]) # o

print(name4[1:2]) # o

sentence = ' I love swimming'

print(sentence[1:5])    # I lo
print(sentence[3:])     # love swimming
print(sentence[:3:-1])  # gnimmiws evo
