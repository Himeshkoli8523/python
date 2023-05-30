# an array of integers num and an integer target,ruturns of the numbers such that they add up to target
lst = input("Enter the array of elements separated by space: ")
target = int(input("Enter the target element: "))
arry = list(map(int, lst.split()))  

def indices(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j

result = indices(arry)
if result is None:
    print("invalid target")
else:
    print("The indices are:", result)
