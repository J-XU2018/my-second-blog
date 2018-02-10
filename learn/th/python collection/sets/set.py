set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5, 6}

# set1.add(4)
# print(set1)
# set1.update({4, 5, 6, 7, 9})
# set1.remove(6)
# set1.discard(5)
# print(set1.pop())
# print(set1)

# print(set1.union(set2))
print(set2 | set1)
print(set1 ^ set2)
print(set1.symmetric_difference(set2))
print(set2 ^ set1)
print(set1 & set2)
print(set2 & set1)
