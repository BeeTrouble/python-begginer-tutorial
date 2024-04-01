## filter( )

numbers1 = [1, 2, 3, 4, 5, 6]

def isEven(n):
    return n % 2 == 0

result1 = filter(isEven, numbers1)

print(list(result1))


numbers2 = [194, 56, 21, 3, 12, 1003]

result2 = filter(lambda n : n % 2 == 0, numbers2)

print(list(result2))
