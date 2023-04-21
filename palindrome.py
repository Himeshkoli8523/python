i = int(input("enter the number:"))
num = i
rev = 0 
while(i>0):
    rev= (rev*10)+i%10
    i = i//10
if(rev == num):
    print("palindrome number")
else:
    print("not palindrome number")