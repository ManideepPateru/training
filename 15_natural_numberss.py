def fun(n,sum):
    if n<1:
        print(sum)
        return
    fun(n-1,sum+n)#`5+4+3+2+1
n=int(input())
fun(n,sum=0)