def fun(n):
    fc=0
    if n==1:
        return 1
    for i in range(1,n+1):
        if(n%i==0):
            fc+=1
    if fc==2:
        return 0
    else:
        return 1
n=int(input())
c=0
for i in range(1,n+1):
    if(n%i==0):
        if(fun(i)):
            c+=1
print(c)
