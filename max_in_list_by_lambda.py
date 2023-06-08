# Write a lambda function to find the maximum value from a list of numbers.

list1 = input("Enter the numbers in the list :").split()
list1 = [int (num) for num in list1]
value =  lambda a: max(list1)
print(value(list1))