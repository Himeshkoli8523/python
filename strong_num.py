n = int(input("Enter an integer: "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
num = 0
for digit in str(n):
    num += factorial(int(digit))
if num == n:
    print(n, "it is a strong number")
else:
    print(n, "it is not a strong number")