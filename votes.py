n=int(input())
vote=list(map(int,input().split()))
age=list(map(int,input().split()))
g=max(vote)*[0]
for i in range(n):
    if age[i]>=18:
        g[vote[i]-1]+=1
# m=max(g)
# print(g.index(m)+1)
temp=sorted(g,reverse=True)
if temp[0]==temp[1]:
    print(-1)
else:
    print(g.index(temp[0]+1))
        
    
        
       
       