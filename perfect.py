pn = int(input("Enter the number to check it is perfect or not: "))

sum = 0 
i = 1
while i<pn:
  if pn%i==0:
   sum = sum+i
  i = i+1

if sum==pn:
  print(pn,"is a perfect number:",)
else:
  print("not perfect number")