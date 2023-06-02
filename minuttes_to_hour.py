minutes = int(input("Enter the number of minutes: "))
x = minutes // 60
hours = minutes / 60-x
y = hours*60
y =int(y)
print(x,"hours and",y,'minutes')