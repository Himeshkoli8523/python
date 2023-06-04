# Write a Python program to find the union of two sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}


union_set1 = set1.union(set2)
print("Union using union() method:", union_set1)


union_set2 = set1 | set2
print("Union using | operator:", union_set2)
