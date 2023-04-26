num1 = int(input("Enter the 1st number "))
num2 = int(input("Enter the 2nd number "))
def square(arg1,arg2):
    arg1 = arg1*arg1
    arg2 = arg2*arg2
    return arg1+arg2
print("the sum of square of two numbers is ",square(num1,num2))