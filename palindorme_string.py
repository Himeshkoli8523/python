string = input("Enter the string :")
rev = string[::-1]
if rev == string:
    print('The given string is palindrome')
else:
    print('The given string is not palindrome')