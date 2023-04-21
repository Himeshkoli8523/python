num = int(input("enter the number to which you want to print sum:"))
sum = 0
for i in range(1,num+1):
    if (i%3)== 0 or (i%5)==0:
     sum += i
print(sum)