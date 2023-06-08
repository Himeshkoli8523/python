# Write a function to find the average of a list of numbers.

list1 = input("Enter the numbers in the list :").split()
list1 = [int (num) for num in list1]
x = lambda a : sum(a)
print("The sum of the elements in the lists is",x(list1))