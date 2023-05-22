n=int(input())
lst=[]
a=0
b=1
for i in range(1,n+1):
    lst.append(a)
    c=a+b
    a=b
    b=c
if n in lst:
    print('True')
else:
    print('False')