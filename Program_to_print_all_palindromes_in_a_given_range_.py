def fun(x):
    a=x
    rem=0
    while x:
        d=x%10
        rem=rem*10+d
        x=x//10
    if rem==a:
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if fun(i):
        print(i,end=' ')
