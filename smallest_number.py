list1 = list(map(int, input("Enter the elements: ").strip().split()))

smallest = None 

for num in list1:
    if num >= 0:
        if smallest is None or num < smallest:
            smallest = num
            break

print("Smallest positive number:", smallest)
