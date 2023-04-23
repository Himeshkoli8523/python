marks = int(input("Enter the percentage"))
if marks < 40 :
    print("Fail")
elif(marks)>80 and marks <= 100:
    print("First class")
elif marks >70 and marks <=80:
    print("Second calss ")
elif marks > 60 and marks <= 70:
    print("Avarage")
elif marks >=40 and marks <= 60:
    print("Pass") 
else:
    print("Invalid marks")