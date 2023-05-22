a=int(input())
for i in range(0,a):
    n=int(input())
    p=1
    for j in range(1,n+1):
        p*=j
    print(p)
