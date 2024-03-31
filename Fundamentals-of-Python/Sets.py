# Sets

set1 = {"Roger", "Syd"}
set2 = {"Roger"}

intersect = set1 & set2

print(intersect)

mod1 = set1 | set2
print(mod1)

mod2 = set1 - set2
print(mod2)

mod3 = set1 < set2
print(mod3)

print(list(set1))

set1 = {"Roger", "Syd" , "Roger"}
set2 = {"Roger"}

print(list(set1))
