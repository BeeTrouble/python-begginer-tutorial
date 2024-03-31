# Operators

age = 20

##Arithmetic Operators

1 + 1  # 2
2 - 2  # 1
2 * 2  # 4
4 / 2  # 2
4 % 3  # 1
4 ** 2 # 16
4 // 2 # 2

age = 12
age += 89 # age = age + 89 = 101
print(age)

number = 2000
number *= 2 # number = number * 2 = 4000
print(number)

## Comparison Operators

a = 1
b = 2

a == b # False
a != b # True
a > b  # False
a <= b # True

## Boolean Operators

condition1 = True
condition2 = False

not condition1 # False
condition1 and condition2 # False
condition1 or condition2 # True

print(0 or 1) ## 1
print(False or 'hey') ## 'hey'
print('hi' or 'hey') ## 'hi'
print([] or False) ## False
print(False or []) ## '[]'

print(0 and 1) ## 0
print(1 and 0) ## 0 
print( False and 'hey') ## False
print('hi' and 'hey') ## 'hey'
print([] and False) ## []
print(False and []) ## False

## Bitwise Operators

# &  performs AND
# |  perfroms OR
# ^  performs XOR
# ~  perform NOT
# >> performs shift right operation
# << performs shift left operation

## is & in Operators

# is Idenity Operator
# in Membership Operator

## Ternary Operator

def is_adult(age):
    if age > 18:
        return True
    else: 
        return False

def is_adult2(age):
    return True if age > 18 else False
