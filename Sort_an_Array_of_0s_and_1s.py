n=int(input())
a=list(map(int,input().split()[:n]))
k=sorted(a)
print(*k)
