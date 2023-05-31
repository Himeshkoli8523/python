# roman_to_decimal
def rtd(S:str)-> int:
    lookup = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000 }
    N =len(S)
    i = N-1
    output = 0
    while i>=0:
        if i < N-1 and lookup[S[i]] <lookup[S[i+1]]:
         output -= lookup[S[i]]
        else:
           output += lookup[S[i]]
        i-=1
    return output
inpt = input("Enter the Roman number")
inpt= inpt.upper()
print(rtd(inpt))