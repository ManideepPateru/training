def fun(arr,tar,i=0,res=[]):
    if i==len(arr):
        if sum(res)==tar:
            print(res,end=" ")
        return
    fun(arr,tar,i+1,res+[arr[i]])
    fun(arr,tar,i+1,res)
l=list(map(int,input().split()))
tar=int(input())
fun(l,tar)
