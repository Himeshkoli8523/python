print("Enter the type of convertion you need: \n 1 For Farenhite to celsius \n 2 For celsius to farenhite")
choise1 =int(input())
if(choise1==1):
   far = float(input("Enter tempreture"))
   resultC = (far-32)*5/9
   print(resultC)
elif(choise1==2):
   cel = int(input("Enter the tempreture"))
   resultF = (cel*9/5)+32
   print(resultF)
else:
   print("invalid choise")
   