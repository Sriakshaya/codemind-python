n=int(input())
m=n*n
t=n
s=0
while t!=0:
    r=t%10
    s=s*10+r
    t=t//10
    n1=s*s
s1=0
while n1!=0:
    r1=n1%10
    s1=s1*10+r1
    n1=n1//10
print(m==s1)
