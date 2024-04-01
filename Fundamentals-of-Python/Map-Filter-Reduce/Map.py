## map( )

numbers1 = [1, 2, 3]

def double1(a):
    return a * 2

result1 = map(double1, numbers1)

print(list(result1))


numbers2 = [9, 23, 17]

double2 = lambda a: a * 2

result2 = map(double2, numbers2)

print(list(result2))


numbers3 = [11, 36, 57]

result3 = map(lambda a: a * 2, numbers2)

print(list(result3))
