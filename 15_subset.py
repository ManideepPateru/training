def fun(arr,i=0,res=[]):
    if i==len(arr):
        print(res)
        return
    fun(arr,i+1,res+[arr[i]])
    fun(arr,i+1,res)
l=list(map(int,input().split()))
fun(l)