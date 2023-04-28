str1 = input("Enter the list ")
int_str = [int(x) for x in str1.split()]
list1 = []
for square1 in int_str:
   list1.append(square1 ** 2)
print(list1)