def fun(arr,tar,i=0):
    if i==len(arr):
        return 0
    if tar==arr[i]:
        return 1+fun(arr,tar,i+1)
    return fun(arr,tar,i+1)
l=list(map(int,input().split()))
tar=int(input())
print(fun(l,tar))