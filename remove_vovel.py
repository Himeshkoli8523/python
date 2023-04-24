str1 = input("Enter the sentence or word: ")
vovel = "aeiouAEIOU"
for char in str1:
    if char in vovel:
     str1 = str1.replace(char,"")
print("string after removing vovels",str1)
