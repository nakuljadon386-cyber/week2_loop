# print all factor/divisor of a given +ve number.
n=int(input("enter a no.="))
i=1
while(i<=n):
    if(n% i== 0):
        print(i)
    i+=1

