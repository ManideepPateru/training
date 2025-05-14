n=int(input())
l=list(map(int,input().split()))
police=0
unsolved=0
for e in l:
    if e==-1:
        if police>0:
            police-=1
        else:
            usolved+=1
    else:
        police+=e
print(unsolved)
        
        

