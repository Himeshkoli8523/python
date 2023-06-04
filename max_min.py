# Write a Python program to find the maximum and minimum elements in a given list
list1 = input("Enter a list of numbers, separated by spaces: ").split()
list1 = [int(num) for num in list1]

maximum = list1[0]
minimum = list1[0]

for num in list1[1:]:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

print("Maximum:", maximum)
print("Minimum:", minimum)