l=list(map(int,input().split()))
count=0
candidate=None
for i in l:
    if count==0:
        candidate=i
        count=1
    elif count==candidate:
        count=count+1
    else:
        count=count-1
print(candidate)
        
        