import os

path = input("Enter the path of the directory")
if os.path.exists(path):
 list1 = os.listdir(path)
 print(list1)
else:
 print("invalid path")