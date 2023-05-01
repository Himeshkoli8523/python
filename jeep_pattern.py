# program for jeep_pattern

def jeep(warg):
    print(" "*6,"*"*20)
    print(" "*5,"*"," "*7,"*"," "*8,"*")
    print(" "*3,"*"," "*9,"*"," "*10,"*")
    print(" "*1,"*"," "*11,"*"," "*12,"*")
    for i in range(4):
        print("*"*50)
    wheels(warg)
def wheels(warg):
   if warg == 2:
       print(' '*6,'*    *',' '*14,'*    *')
       print(' '*6,' *  *',' '*14,'  *  *')
   elif warg == 4:
       print(' '*2,'*    *',' '*4,'*    *',' '*4,'*    *','  ','*    *')
       print(' '*2,' *  *',' '*4,'  *  *',' '*6 , '*  *',' '*3, ' *  *')
jeep(2)
jeep(4)