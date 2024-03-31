## Booleans

done1 = True

if done1:
    print("yes")
else:
    print("no")

done2 = 1

if done2:
    print("yes")
else:
    print("no")

done3 = ""

if done3:
    print("yes")
else:
    print("no")

done4 = "good"

if done4:
    print("yes")
else:
    print("no")

print(type(done1) == bool)

book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read])

ingredients_purchased = True
meal_cooked = False

ready_to_serve = all([ingredients_purchased, meal_cooked])
