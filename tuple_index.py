intstr = input("Enter the 10 elements separated by space: ")
list2 = intstr.split()
if len(list2) == 10:
    tuple1 = tuple(map(int, list2))
    value = int(input("Enter the index of the element to delete: "))
    tuple1 = tuple1[:value]+tuple1[value+1:]
    print("After deleting the element:", tuple1)
else:
    print("Invalid input. Please enter 10 elements.")
