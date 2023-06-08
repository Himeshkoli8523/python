# Write a function to count the occurrences of a specific element in a list.

list_ele =input("Enter the elements in the list").split()
list_ele = [int (num) for num in list_ele]
S_ele =int(input('Enter the specific element'))
x = lambda a ,b:a.count(b)
print("The number of count is :",x(list_ele,S_ele))