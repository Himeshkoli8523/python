def check_even(lst):
    inpt2 =[]
    for num in lst:
        if num%2==0:
            inpt2.append(num)
    return inpt2
lst = input("Enter the list of integers including comma")
lst= lst.split(',')
lst = [int(num) for num in lst]
numbers= check_even(lst)
print("Even numbers are",numbers)