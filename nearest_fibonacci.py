def first(n,a,b):
    while(n>=b):
        c=a+b
        a=b
        b=c
    return b
def last(n,a,b):
    while(n>=b):
        c=a+b
        a=b
        b=c
    return a
n=int(input())
m=first(n,0,1)
s=last(n,0,1)
if (m-n>n-s):
    print(s)
elif(m-n<n-s):
    print(m)
else:
    print(s,m,sep=" ")
