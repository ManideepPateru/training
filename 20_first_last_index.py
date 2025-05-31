l=list(map(int,input().split()))
n=int(input())
start=0
end=len(l)-1
result=[-1,-1]
for i in range(len(l)):
    mid=(start+end)//2
    if n==l[mid]:
        result[0]=mid
        end=mid-1
    elif l[mid]<n:
        start=mid+1
    else:
        end=mid-1
start=0
end=len(l)-1
for i in range(len(l)):
    mid=(start+end)//2
    if n==l[mid]:
        result[1]=mid
        start=mid+1
    elif l[mid]<n:
        start=mid+1
    else:
        end=mid-1
print(result)


