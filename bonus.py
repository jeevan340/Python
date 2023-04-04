g=input("enter the grade (A/B)")
s= int(input("enter the salary"))
if (s<10000):
    s*=2/100
if(g=='A'):
    b=s*5/100
else:
    b=s*10/100

total_salary=s+b
print("bonus:",b)
print("total salary:",total_salary)
