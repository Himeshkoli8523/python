str1 = input("Enter the sentence ")
count = {}
chars = str1.split()
for word in chars:
    if word in count:
        count[word]+=1
    else:
        count[word]=1
for word,con in count.items():
    print(word,count)