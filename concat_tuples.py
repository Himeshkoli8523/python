intstr =input("Enter the integer values of tuple seperated by space")
intstr2 = input("Enter the 2nd integer values of tuple seperated by space")
tuple1 = tuple(map(int,intstr.split()))
tuple2 = tuple(map(int,intstr2.split()))
con_tuple = tuple1+tuple2
print(con_tuple)
