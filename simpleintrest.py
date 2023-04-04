def simint(p,t,r):
    SI=p*t*r/100
    return SI
p=int(input("enter the principal amount"))
t=int(input("enter the no of years"))
s=input("is customer is senior citizen(y/n)")
g=input("enter the gender (m/f)")
if(s=='y'):
     if(g=='f'):
        r=15
        print("intrest=" ,end=" ")
        print(simint(p,t,r))
        
     else:
         r=12
         print("intrest=" ,end=" ")
         print(simint(p,t,r))
else:
    r=10
    print("intrest=" ,end=" ")
    print(simint(p,t,r))
