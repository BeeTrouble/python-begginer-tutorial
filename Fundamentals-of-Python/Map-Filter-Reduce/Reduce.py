## Reduce( )

expenses1 = [
    ('Dinner', 80),
    ('Car repair', 120)
]

sum1 = 0

for expense in expenses1:
    sum += expense[1]

print(sum1)


from functools import reduce

expenses2 = [
    ('Dinner', 80),
    ('Car repair', 120)
]

sum2 = reduce(lambda a, b: a[1] + b[1], expenses2)


print(sum2)
