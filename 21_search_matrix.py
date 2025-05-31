matrix=[[1,2,3,4],
        [34 ,35,56,76]]
key=34
m=len(matrix)
n=len(matrix[0])
low=0
high=(n+m)-1
while low<=high:
    mid=(low+high)//2
    i=(mid//m)-1
    j=(mid%m)-1
    res=matrix[i][j]
    if res==key:
        print(True)
        break
    if res>mid:
        low=mid+1
    if res<mid:
        high=mid-1
        