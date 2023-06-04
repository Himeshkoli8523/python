# Write a Python program to create a tuple from a given list.
list1 = input("Enter a list of numbers, separated by spaces: ").split()
tuple1 = [int(element) for element in list1]
print(tuple1)