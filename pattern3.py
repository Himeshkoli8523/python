for i in range(7):
    for j in range(7-i-1):
        print(end = " ")
    for j in range(i+1):
        print("*",end=" ")
    print()