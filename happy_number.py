n=int(input())
t=n
s=0
while t!=0:
    r=t%10
    s=s+r*r
    t=t//10
    if t==0 and s>=10:
        t=s
        s=0
if s==1 or s==7:
    print("True")
else:
    print("False")
