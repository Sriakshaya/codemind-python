def last(n):
    temp=n
    while(1):
        temp1=temp
        for i in range(2,temp1//2):
            if temp1%i==0:
                temp=temp+1
                break
        else:
                break
    return temp1
def first(n):
    temp=n
    while(1):
        temp1=temp
        for i in range(2,temp1//2):
            if temp1%i==0:
                temp=temp-1
                break
        else:
            break
    return temp1
n=int(input())
for i in range(n):
    temp1=int(input())
    a=first(temp1)
    b=last(temp1)
    if(b-temp1>=temp1-a):
        print(a)
    elif(b-temp1<temp1-a):
        print(b)
 