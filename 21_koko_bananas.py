import math
piles=list(map(int,input().split()))
h=int(input())
start=1
end=max(piles)
result=end
while start<=end:
    mid=(start+end)//2
    t_hours=0
    for i in piles:
        t_hours+=math.ceil(i/mid)
    if t_hours<=h:
        result=mid
        end=mid-1
    else:
        start=mid+1
print(result)
        