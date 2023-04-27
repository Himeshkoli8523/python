n = input("Enter the list of numbers ").split()
n = [int(num) for num in n]
newnum = list(set(n))
print("After removig the dublicates",newnum)