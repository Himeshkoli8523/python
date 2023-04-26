string = input("Enter the word or sentence")
def check_v(par1):
 vovel ="aeiouAEIOU"
 count = 0
 for char in string:
    if char in vovel:
     count +=1
 return count
count_vovels = check_v(string)
print(count_vovels,"vovel present in the given string")