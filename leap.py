year = int(input("Enter the year"))
if(year%4)==0:
 if(year%100)==0:
   if(year%400)==0:
     print("it is leap")
   else:
      print("it is not leap")
 else:
        print("it is leap")
else:
    print("it is not")    