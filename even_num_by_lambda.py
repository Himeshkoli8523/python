# Write a lambda function to check if a number is even.

num = int(input("Enter the number :"))
x = lambda a: a % 2
if x(num) == 0:
    print("the number is even")
else:
    print("the number is odd")