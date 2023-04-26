lst = []
n = int(input("Enter the number of elements"))
for i in range(n):
    ele = int(input())
    lst.append(ele)
def check_even(arg1):
    for num in arg1:
        if num%2==0:
            inpt2 = num
        print(inpt2)
    return inpt2
print("the list is ",check_even(lst))