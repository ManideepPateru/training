n=10
q=[]
q.append("5")
q.append("6")
count=0
while count<n:
    t=q.pop(0)
    print(t,end=" ")
    q.append(t+"5")
    q.append(t+"6")
    count=count+1